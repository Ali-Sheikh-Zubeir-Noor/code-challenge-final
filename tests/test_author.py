
import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine

def test_author_creation():
    author = Author(name="Test Author")
    author.save()
    assert author.id is not None

def test_find_author_by_name():
    author = Author(name="Find Me")
    author.save()
    found = Author.find_by_name("Find Me")
    assert found is not None
    assert found.name == "Find Me"

def test_articles_relationship():
    author = Author(name="Article Author")
    author.save()
    magazine = Magazine(name="Test Magazine", category="Tech")
    magazine.save()
    article = author.add_article(magazine, "Article Title")
    articles = author.articles()
    assert any(a["title"] == "Article Title" for a in articles)

