import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine
from seed import seed_data


class TestModels(unittest.TestCase):
    seed_data()

    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly")
        self.assertEqual(magazine.name, "Tech Weekly")


if __name__ == "__main__":
    unittest.main()
