import json
import os
from typing import List
from book import Book


def load_books(filename: str) -> List[Book]:
    """
    Загружает книги из файла.

    Args:
        filename (str): Имя файла для загрузки данных.

    Returns:
        List[Book]: Список загруженных книг.
    """
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                books_data = json.load(file)
                return [Book.from_dict(book) for book in books_data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []


def save_books(filename: str, books: List[Book]) -> None:
    """
    Сохраняет книги в файл.

    Args:
        filename (str): Имя файла для сохранения данных.
        books (List[Book]): Список книг для сохранения.
    """
    with open(filename, 'w') as file:
        json.dump([book.to_dict() for book in books], file, indent=4)
