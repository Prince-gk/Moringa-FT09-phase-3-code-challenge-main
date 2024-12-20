from database.connection import get_db_connection
from models.author import Author
from models.magazine import Magazine
from models.article import Article


def seed_data():
    # Seed authors
    authors = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown"]

    # Seed magazines
    magazines = [
        ("Tech Monthly", "Technology"),
        ("Fashion Weekly", "Lifestyle"),
        ("Health Today", "Health"),
        ("Sports Daily", "Sports"),
    ]

    # Seed articles
    articles = [
        (
            "The Future of AI",
            "Artificial Intelligence is revolutionizing the world.",
            1,
            1,
        ),
        ("Fashion Trends in 2024", "What are the upcoming trends in fashion?", 2, 2),
        (
            "Top 10 Health Tips",
            "Learn how to improve your health with these simple steps.",
            3,
            3,
        ),
        (
            "Football World Cup Highlights",
            "A recap of the most exciting moments in the World Cup.",
            4,
            4,
        ),
    ]

    # Insert authors into the database
    with get_db_connection() as conn:
        cursor = conn.cursor()

        for author_name in authors:
            cursor.execute("INSERT INTO authors (name) VALUES (?)", (author_name,))

        conn.commit()

        # Insert magazines into the database
        for magazine_name, magazine_category in magazines:
            cursor.execute(
                "INSERT INTO magazines (name, category) VALUES (?, ?)",
                (magazine_name, magazine_category),
            )

        conn.commit()

        # Insert articles into the database
        for article_title, article_content, author_id, magazine_id in articles:
            cursor.execute(
                "INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)",
                (article_title, article_content, author_id, magazine_id),
            )

        conn.commit()
