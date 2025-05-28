
import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine

def test_article_creation():
    author = Author(name="Article Author")
    author.save()
    magazine = Magazine(name="Article Magazine", category="News")
    magazine.save()
    article = Article(title="Test Article", author_id=author.id, magazine_id=magazine.id)
    article.save()
   
