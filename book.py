from typing import Dict, Union


class Book:
    """
    Класс для представления книги в библиотеке.

    Атрибуты:
        id (int): Уникальный идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
        status (str): Статус книги ("в наличии" или "выдана").
    """

    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = 'в наличии'):
        """
        Инициализирует экземпляр книги.

        Args:
            book_id (int): Уникальный идентификатор книги.
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
            status (str): Статус книги (по умолчанию "в наличии").
        """
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> Dict[str, Union[int, str]]:
        """
        Преобразует объект книги в словарь.

        Returns:
            Dict[str, Union[int, str]]: Словарь с данными книги.
        """
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }

    @staticmethod
    def from_dict(data: Dict[str, Union[int, str]]) -> 'Book':
        """
        Создает объект книги из словаря.

        Args:
            data (Dict[str, Union[int, str]]): Словарь с данными книги.

        Returns:
            Book: Экземпляр класса Book.
        """
        return Book(
            book_id=data['id'],
            title=data['title'],
            author=data['author'],
            year=data['year'],
            status=data['status']
        )
