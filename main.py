from library import Library


def main():
    """
    Основная функция для взаимодействия с пользователем.
    """
    library = Library()
    while True:
        print("\nСистема управления библиотекой")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отображение всех книг")
        print("5. Изменить статус книги")
        print("6. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == '1':
            title = input("Введите название книги: ").strip()
            author = input("Введите автора книги: ").strip()
            while True:
                try:
                    year = int(input("Введите год издания книги: ").strip())
                    break
                except ValueError:
                    print("Некорректный год. Пожалуйста, введите числовое значение.")
            library.add_book(title, author, year)
        elif choice == '2':
            try:
                book_id = int(input("Введите ID книги для удаления: ").strip())
                library.delete_book(book_id)
            except ValueError:
                print("Некорректный ID. Пожалуйста, введите числовое значение.")
        elif choice == '3':
            while True:
                field = input("Введите поле для поиска (title, author, year, status): ").strip().lower()
                if field not in ['title', 'author', 'year', 'status']:
                    print(f"Некорректное поле для поиска: {field}. Пожалуйста, введите одно из следующих полей: title, author, year, status.")
                else:
                    break
            query = input("Введите запрос: ").strip()
            results = library.search_books(query, field)
            if results:
                for book in results:
                    print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
            else:
                print("Книги по вашему запросу не найдены.")
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            try:
                book_id = int(input("Введите ID книги: ").strip())
                status = input("Введите новый статус (в наличии, выдана): ").strip()
                if status in ['в наличии', 'выдана']:
                    library.update_status(book_id, status)
                else:
                    print("Некорректный статус. Пожалуйста, введите 'в наличии' или 'выдана'.")
            except ValueError:
                print("Некорректный ID. Пожалуйста, введите числовое значение.")
        elif choice == '6':
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == '__main__':
    main()


