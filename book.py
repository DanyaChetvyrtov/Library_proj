from abc import ABC, abstractmethod
from help_func import text_format


class Book(ABC):
    def __init__(self, book_title='None', amount_of_copies=0, author=None, amount_of_pages=None):
        self.book_title = book_title
        self.amount_of_copies = amount_of_copies
        self.__author = author
        self.__amount_of_pages = amount_of_pages

    @property
    def amount_of_copies(self):
        return self._amount_of_copies

    @amount_of_copies.setter
    def amount_of_copies(self, value: int):
        # Свойство amount_of_copies может быть только числом
        # и не может иметь отрицательное значение
        assert type(value) is int, TypeError(f'Некорректный тип данных: {type(value)}')
        assert value >= 0, ValueError('Значение не может быть меньше нуля')
        self._amount_of_copies = value

    @property
    def book_title(self):
        return self._book_title

    @book_title.setter
    def book_title(self, value: str):
        # Свойство может быть только строкой
        assert type(value) is str, TypeError(f'Некорректный тип данных: {type(value)}')
        self._book_title = value.strip().title()

    @abstractmethod
    def book_type(self):
        pass

    def __str__(self):
        info = [f'Название книги: {self.book_title!r}', f'Количество копий: {self.amount_of_copies}']
        return text_format(info)

    def __add__(self, other):
        assert self.book_title == other.book_title, \
            f'Операцию можно выполнить только с такой же книгой: {self._book_title!r}'

        self.amount_of_copies += other.amount_of_copies
        return self

    def __sub__(self, other):
        assert self.book_title == other.book_title, \
            f'Операцию можно выполнить только с такой же книгой: {self._book_title!r}'

        self.amount_of_copies -= other.amount_of_copies
        return self

    def get_info(self):
        info = [f'Название: {self.book_title!r}', f'Жанр: {self.book_type()}',
                f'Количество копий: {self.amount_of_copies}', f'Автор: {self.__author}',
                f'Количество страниц: {self.__amount_of_pages}']
        return text_format(info)


class Fantasy(Book):
    def book_type(self):
        return 'Fantasy'


class Roman(Book):
    def book_type(self):
        return 'Romans'


class Horror(Book):
    def book_type(self):
        return 'Horror'


class BookFactory:
    def __init__(self):
        self.__genres = {'Романы': Roman,
                         'Фэнтези': Fantasy,
                         'Ужасы': Horror}

    # Выводит возможные жанры
    def __str__(self):
        return ''.join([f'* {genre}\n' for genre in self.__genres])

    # Создание новой книги
    def create_book(self):
        book_genre = input('Укажите жанр который вас интересует:\n->: ').strip().title()

        if book_genre in self.__genres:
            current_book_title = input('Введите название: ').strip().title()
            number_of_copies_of_this_book = input('Введите количество копий: ').strip()
            author_name = input('Введите автора: ').strip().title()
            book_size = input('Введите размер книги: ').strip()

            assert number_of_copies_of_this_book.isdigit(), TypeError('Нужно ввести число.')
            assert book_size.isdigit(), TypeError('Нужно ввести число.')

            number_of_copies_of_this_book = int(number_of_copies_of_this_book)
            book_size = int(book_size)

            new_book = self.__genres[book_genre](current_book_title,
                                                 number_of_copies_of_this_book,
                                                 author_name,
                                                 book_size)
            return new_book
        else:
            raise Exception('У нас нет такого жанра.')
