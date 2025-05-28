# Code Challenge Final

## Project Overview

This project models the relationship between **Authors**, **Magazines**, and **Articles** using SQLite and Python. It demonstrates creating, reading, and managing data with raw SQL queries wrapped in Python classes, simulating an ORM.

---

## Folder Structure
code-challenge-final/
│
├── lib/
│ └── models/
│ ├── author.py # Author model class
│ ├── magazine.py # Magazine model class
│ ├── article.py # Article model class
│ └── db/
│ └── connection.py # Database connection utility
│
├── tests/
│ ├── test_author.py # Unit tests for Author model
│ ├── test_magazine.py # Unit tests for Magazine model
│ └── test_article.py # Unit tests for Article model
│
├── README.md # Project documentation and setup instructions
└── setup.sql # SQL script to create database schema

markdown


---

## Models Description

### Author

- **Attributes**: `id`, `name`
- **Key Methods**:
  - `save()`: Save author to the database.
  - `find_by_id(id)`: Find author by ID.
  - `find_by_name(name)`: Find author by name.
  - `articles()`: Retrieve articles written by the author.
  - `magazines()`: Get magazines where the author contributed.
  - `add_article(magazine, title)`: Add a new article.
  - `topic_areas()`: List magazine categories the author contributed to.

### Magazine

- **Attributes**: `id`, `name`, `category`
- **Key Methods**:
  - `save()`: Save magazine to the database.
  - `find_by_id(id)`: Find magazine by ID.
  - `find_by_name(name)`: Find magazine by name.
  - `find_by_category(category)`: Find magazines by category.
  - `articles()`: Get all articles in the magazine.
  - `contributors()`: Get authors who contributed.
  - `article_titles()`: List all article titles.
  - `contributing_authors()`: Authors with >2 articles in magazine.

### Article

- **Attributes**: `id`, `title`, `author_id`, `magazine_id`
- **Key Methods**:
  - `save()`: Save article to the database.
  - `find_by_id(id)`: Find article by ID.
  - `find_by_title(title)`: Find article by title.
  - `find_by_author(author_id)`: Articles by a specific author.
  - `find_by_magazine(magazine_id)`: Articles in a magazine.

---

## Database Setup

Run the following SQL schema (`setup.sql`) to create the required tables:

```sql
CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE magazines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    category TEXT NOT NULL
);

CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    magazine_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (magazine_id) REFERENCES magazines(id)
);

Database Connection
Managed in lib/db/connection.py using SQLite.

Returns connection objects with named column access enabled.

Testing
Tests use pytest and cover:

Author creation and queries

Magazine creation and queries

Article creation and queries

Relationship queries between models

Run tests with:

bash:
pytest
