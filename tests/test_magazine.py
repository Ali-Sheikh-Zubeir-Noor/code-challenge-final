
import pytest
from lib.models.magazine import Magazine
from lib.models.author import Author

def test_magazine_creation():
    magazine = Magazine(name="Test Magazine", category="Health")
    magazine.save()
    assert magazine.id is not None

def test_find_magazine_by_name():
    magazine = Magazine(name="Find Magazine", category="Science")
    magazine.save()
    found = Magazine.find_by_name("Find Magazine")
    assert found is not None
    assert found.name == "Find Magazine"

def test_contributors_relationship():
    author = Author(name="Contributor Author")
    author.save()
    magazine = Magazine(name="Contributor Magazine", category="Lifestyle")
    magazine.save()
    author.add_article(magazine, "Contributor Article")
    contributors = magazine.contributors()
    assert any(c["name"] == "Contributor Author" for c in contributors)

