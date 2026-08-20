import sqlite3
from datetime import datetime


DATABASE_NAME = "newsense.db"


def get_connection():
    """Create and return a database connection."""
    return sqlite3.connect(DATABASE_NAME)


def create_table():
    """Create the news table if it doesn't already exist."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            headline TEXT NOT NULL,
            article TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            polarity REAL NOT NULL,
            subjectivity REAL NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_news(headline, article, sentiment, polarity, subjectivity):
    """Save analyzed news into the database."""

    connection = get_connection()
    cursor = connection.cursor()

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO news
        (headline, article, sentiment, polarity, subjectivity, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        headline,
        article,
        sentiment,
        polarity,
        subjectivity,
        created_at
    ))

    connection.commit()
    connection.close()


def get_all_news():
    """Return all analyzed news."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            headline,
            article,
            sentiment,
            polarity,
            subjectivity,
            created_at
        FROM news
        ORDER BY id DESC
    """)

    news = cursor.fetchall()

    connection.close()

    return news


def delete_all_news():
    """Delete all stored news."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM news")

    connection.commit()
    connection.close()


# Create the table when this file is executed
if __name__ == "__main__":

    create_table()

    print("===================================")
    print("     NewsSense Database Setup")
    print("===================================")

    print("\nDatabase created successfully!")
    print("Table 'news' is ready.")