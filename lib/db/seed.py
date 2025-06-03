from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

def reset_tables():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.executescript("""
            DELETE FROM articles;
            DELETE FROM authors;
            DELETE FROM magazines;

            DELETE FROM sqlite_sequence WHERE name='articles';
            DELETE FROM sqlite_sequence WHERE name='authors';
            DELETE FROM sqlite_sequence WHERE name='magazines';
        """)
        conn.commit()

def seed_data():
    # Authors
    alice = Author(name="Alice")
    bob = Author(name="Bob")
    carol = Author(name="Carol")
    dave = Author(name="Dave")

    alice.save()
    bob.save()
    carol.save()
    dave.save()

    # Magazines
    tech = Magazine(name="Tech Times", category="Technology")
    health = Magazine(name="Health Weekly", category="Health")
    travel = Magazine(name="Travel World", category="Travel")
    education = Magazine(name="EduDigest", category="Education")

    tech.save()
    health.save()
    travel.save()
    education.save()

    # Articles (Ensure Alice has the most, and Tech Times has multiple authors)
    alice.add_article(tech, "AI Revolution")
    alice.add_article(tech, "Machine Learning Basics")
    alice.add_article(health, "Healthy Living Tips")

    bob.add_article(tech, "Cybersecurity Tips")
    bob.add_article(travel, "Exploring Kenya")

    carol.add_article(education, "Digital Learning")
    carol.add_article(education, "Reforming Schools")
    carol.add_article(education, "Motivating Students")

    dave.add_article(health, "Home Workouts")

if __name__ == "__main__":
    reset_tables()
    seed_data()

