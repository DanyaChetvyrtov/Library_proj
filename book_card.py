from datetime import datetime
from help_func import text_format


class BookCard:
    def __init__(self, reader_name: str, reader_number: int, was_granted_by: str):
        self.__reader_name = reader_name
        self.__reader_number = reader_number
        # Сотрудник выдавший книгу
        self.__was_granted_by = was_granted_by
        # Книги, которые читатель ещё не вернул
        self.__books = list()
        # Общее количество книг взятых за всё время
        self.book_quantity = 0
        # Время создания карточки
        self.__book_card_was_taken = datetime.now()

    # Свойство доступно только для чтения
    @property
    def reader_name(self):
        return self.__reader_name

    # Свойство доступно только для чтения
    @property
    def reader_number(self):
        return self.__reader_name

    def __str__(self):
        reader_info = [f'Имя читателя: {self.__reader_name}',
                       f'Контактный номер: {self.__reader_number}',
                       f'Карточка была выдана: {self.__book_card_was_taken}',
                       f'Взято книг за всё время: {self.book_quantity}', '',
                       f'Нужно вернуть: {len(self.__books)}', '',
                       f'Создатель карты: {self.__was_granted_by}']
        return text_format(reader_info)

    # Взятие книги
    def take_book(self, book):
        self.__books.append(book)
        self.book_quantity += 1

    # Возвращение книги
    def return_book(self, book_title: str):
        assert type(book_title) is str, TypeError(f'Некорректный тип данных {type(book_title)}')

        reader_books = [book.book_title for book in self.__books]
        if book_title in reader_books:
            searched_index = self.__books.index(book_title)
            return self.__books.pop(searched_index)
        else:
            raise ValueError(f'Данный пользователь не брал книгу {book_title!r}')

    def get_books(self):
        return self.__books
