from typing import List
from book import Book
from utils import load_books, save_books


class Library:
    """
    Класс для управления библиотекой книг.

    Атрибуты:
        BOOKS_FILE (str): Имя файла для хранения данных книг.
        books (List[Book]): Список книг в библиотеке.
    """
    BOOKS_FILE = 'books.json'

    def __init__(self):
        """
        Инициализирует экземпляр библиотеки и загружает книги из файла.
        """
        self.books = load_books(self.BOOKS_FILE)

    def save_books(self) -> None:
        """
        Сохраняет текущий список книг в файл.
        """
        save_books(self.BOOKS_FILE, self.books)

    def add_book(self, title: str, author: str, year: int) -> None:
        """
        Добавляет новую книгу в библиотеку.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
        """
        new_id = max((book.id for book in self.books), default=0) + 1
        new_book = Book(book_id=new_id, title=title, author=author, year=year)
        self.books.append(new_book)
        self.save_books()
        print(f'Книга "{title}" добавлена с ID {new_id}.')

    def delete_book(self, book_id: int) -> None:
        """
        Удаляет книгу из библиотеки по её ID.

        Args:
            book_id (int): Уникальный идентификатор книги.
        """
        book_to_delete = next((book for book in self.books if book.id == book_id), None)
        if book_to_delete:
            self.books.remove(book_to_delete)
            self.save_books()
            print(f'Книга с ID {book_id} удалена.')
        else:
            print(f'Книга с ID {book_id} не найдена.')

    def search_books(self, query: str, field: str) -> List[Book]:
        """
        Ищет книги по заданному полю и запросу.

        Args:
            query (str): Строка запроса для поиска.
            field (str): Поле для поиска (title, author, year, status).

        Returns:
            List[Book]: Список книг, соответствующих запросу.
        """
        query = query.strip().lower()
        return [book for book in self.books if query in str(getattr(book, field, '')).lower()]

    def display_books(self) -> None:
        """
        Выводит список всех книг в библиотеке.
        """
        for book in self.books:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")

    def update_status(self, book_id: int, status: str) -> None:
        """
        Обновляет статус книги.

        Args:
            book_id (int): Уникальный идентификатор книги.
            status (str): Новый статус книги ("в наличии" или "выдана").
        """
        book_to_update = next((book for book in self.books if book.id == book_id), None)
        if book_to_update:
            book_to_update.status = status
            self.save_books()
            print(f'Статус книги с ID {book_id} обновлен на "{status}".')
        else:
            print(f'Книга с ID {book_id} не найдена.')


