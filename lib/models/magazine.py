from lib.db.connection import get_connection

class Magazine:
    def __init__(self, id=None, name=None, category=None):
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            if self.id is None:
                cursor.execute(
                    "INSERT INTO magazines (name, category) VALUES (?, ?)",
                    (self.name, self.category)
                )
                self.id = cursor.lastrowid
            else:
                cursor.execute(
                    "UPDATE magazines SET name = ?, category = ? WHERE id = ?",
                    (self.name, self.category, self.id)
                )
            conn.commit()

    @classmethod
    def find_by_name(cls, name):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
            row = cursor.fetchone()
        return cls(id=row['id'], name=row['name'], category=row['category']) if row else None

    @classmethod
    def find_by_category(cls, category):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM magazines WHERE category = ?", (category,))
            rows = cursor.fetchall()
        return [cls(id=row['id'], name=row['name'], category=row['category']) for row in rows]

    @classmethod
    def find_by_id(cls, id_):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM magazines WHERE id = ?", (id_,))
            row = cursor.fetchone()
        return cls(id=row['id'], name=row['name'], category=row['category']) if row else None

    def articles(self):
        from lib.models.article import Article
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
            rows = cursor.fetchall()
        return [Article(id=row['id'], title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id']) for row in rows]

    def contributors(self):
        from lib.models.author import Author
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT DISTINCT authors.id, authors.name FROM authors
                JOIN articles ON authors.id = articles.author_id
                WHERE articles.magazine_id = ?
            """, (self.id,))
            rows = cursor.fetchall()
        return [Author(id=row['id'], name=row['name']) for row in rows]

    def article_titles(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title FROM articles WHERE magazine_id = ?", (self.id,))
            return [row['title'] for row in cursor.fetchall()]

    def contributing_authors(self):
        from lib.models.author import Author
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT authors.id, authors.name, COUNT(articles.id) AS article_count
                FROM authors
                JOIN articles ON authors.id = articles.author_id
                WHERE articles.magazine_id = ?
                GROUP BY authors.id
                HAVING article_count > 2
            """, (self.id,))
            rows = cursor.fetchall()
        return [Author(id=row['id'], name=row['name']) for row in rows]

    @classmethod
    def with_multiple_authors(cls):
        """Magazines that have at least 2 distinct authors contributing articles."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT magazines.id, magazines.name, magazines.category
                FROM magazines
                JOIN articles ON magazines.id = articles.magazine_id
                GROUP BY magazines.id
                HAVING COUNT(DISTINCT articles.author_id) >= 2
            """)
            rows = cursor.fetchall()
        return [cls(id=row['id'], name=row['name'], category=row['category']) for row in rows]

    @classmethod
    def article_counts(cls):
        """All magazines with their article counts (LEFT JOIN ensures 0-count magazines are included)."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT magazines.id, magazines.name, magazines.category, COUNT(articles.id) AS article_count
                FROM magazines
                LEFT JOIN articles ON magazines.id = articles.magazine_id
                GROUP BY magazines.id
            """)
            rows = cursor.fetchall()
        return [cls(id=row['id'], name=row['name'], category=row['category']) for row in rows]

    @classmethod
    def top_publisher(cls):
        """Returns the magazine with the highest number of articles published."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT magazines.id, magazines.name, magazines.category, COUNT(articles.id) AS article_count
                FROM magazines
                LEFT JOIN articles ON magazines.id = articles.magazine_id
                GROUP BY magazines.id
                ORDER BY article_count DESC
                LIMIT 1
            """)
            row = cursor.fetchone()
        return cls(id=row['id'], name=row['name'], category=row['category']) if row else None
