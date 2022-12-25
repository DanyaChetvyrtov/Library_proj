from book import BookFactory
from copy import deepcopy
from book_card import BookCard


class Library:
    __instance = None

    # Используем паттерн Синглтон. У нас может быть только один
    # экземпляр класса библиотека.
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            raise Exception('У данного класса может быть только один экземпляр')

    def __init__(self, lib_title='Библиотека им. В.В.Маяковского'):
        self.lib_title = lib_title
        # Книги в базе
        self.storage = list()
        self.all_quantity_of_book = 0
        # Читатели в базе
        self.readers = list()

    def __str__(self):
        return f'\t  +{(len(self.lib_title) + 2) * "-"}+\n' \
               f'\t  | {self.lib_title} |\n' \
               f'\t  +{(len(self.lib_title) + 2) * "-"}+\n'

    # Добавление книги в базу
    def add_book_to_storage(self):
        new_book = BookFactory().create_book()
        # Создаём массив с названиями всех книг в базе
        book_titles_from_storage = [book_obj.book_title for book_obj in self.storage]

        # Добавляем копии к книге в базе
        if new_book.book_title in book_titles_from_storage:
            current_book_index = book_titles_from_storage.index(new_book.book_title)
            self.all_quantity_of_book += new_book.amount_of_copies
            self.storage[current_book_index] += new_book
            del new_book
        # Или просто добавляем книгу в базу если её ранее там не было
        else:
            self.all_quantity_of_book += new_book.amount_of_copies
            self.storage.append(new_book)

    # Удаление книги из базы
    def del_book_from_storage(self, unnecessary_book: str):
        assert type(unnecessary_book) is str, TypeError(f'Неверный тип данных: {type(unnecessary_book)}')

        book_titles_from_storage = [book_obj.book_title for book_obj in self.storage]

        if unnecessary_book in book_titles_from_storage:
            current_book_index = book_titles_from_storage.index(unnecessary_book)
            self.all_quantity_of_book -= self.storage[current_book_index].amount_of_copies
            del self.storage[current_book_index]
        else:
            raise ValueError(f'ОШИБКА\nКнига {unnecessary_book!r} отсутствует в базе.')

    # Пытался использовать паттерн Стратегии для вариации сортировки
    # объектов при выводе.
    # -> R-Reverse
    # * Алфавитный порядок(по названию книги) -> R
    # * По количеству копий -> R
    # * По жанру
    def get_books(self, print_strategy=0):
        if type(print_strategy) is not int:
            raise TypeError(f'Неверный тип данных: {type(print_strategy)}')

        if print_strategy == 0:
            self.storage.sort(key=lambda book_obj: book_obj.book_title, reverse=False)
        elif print_strategy == 1:
            self.storage.sort(key=lambda book_obj: book_obj.book_title, reverse=True)
        elif print_strategy == 2:
            self.storage.sort(key=lambda book_obj: book_obj.amount_of_copies, reverse=False)
        elif print_strategy == 3:
            self.storage.sort(key=lambda book_obj: book_obj.amount_of_copies, reverse=True)
        elif print_strategy == 4:
            self.storage.sort(key=lambda book_obj: book_obj.book_type(), reverse=True)
        else:
            raise ValueError(f'Нет варианта {print_strategy!r}')

        for book_from_storage in self.storage:
            print(book_from_storage)

    # Поиск подробной информации о книге
    def find_book(self, searched_book: str):
        assert type(searched_book) is str, TypeError(f'Неверный тип данных: {type(searched_book)}')

        book_titles_from_storage = [book_obj.book_title for book_obj in self.storage]
        if searched_book in book_titles_from_storage:
            searched_book_index = book_titles_from_storage.index(searched_book)
            return self.storage[searched_book_index]
        else:
            raise ValueError('Данная книга отсутствует.')

    # Выдача книги читателю
    def take_book(self, reader_name: str, hired_book_title: str):
        if type(reader_name) is not str or type(hired_book_title) is not str:
            raise TypeError(f'Аргументы должны быть типа: {type(str)}\n'
                            f'Использовались {type(reader_name)} и {type(hired_book_title)}')
        readers_name_from_storage = [reader_obj.reader_name for reader_obj in self.readers]

        if reader_name in readers_name_from_storage:
            # 
            searched_reader_index = readers_name_from_storage.index(reader_name)
            cur_book = self.find_book(hired_book_title)
            book_for_reader = deepcopy(cur_book)
            cur_book.amount_of_copies -= 1
            book_for_reader = book_for_reader - cur_book
            self.readers[searched_reader_index].take_book(book_for_reader)
            self.all_quantity_of_book -= 1

        else:
            raise ValueError(f'Карточки читателя с именем {reader_name} не было найдено.')

    # Возвращение книги читателем
    def return_book(self, reader_name: str, hired_book_title: str):
        if type(reader_name) is not str or type(hired_book_title) is not str:
            raise TypeError(f'Аргументы должны быть типа: {type(str)}\n'
                            f'Использовались {type(reader_name)} и {type(hired_book_title)}')
        readers_name_from_storage = [reader_obj.reader_name for reader_obj in self.readers]

        if reader_name in readers_name_from_storage:
            searched_reader_index = readers_name_from_storage.index(reader_name)
            current_book_card = self.readers[searched_reader_index]
            book = current_book_card.return_book(hired_book_title)
            same_book_from_lib = self.find_book(hired_book_title)
            same_book_from_lib += book
            self.all_quantity_of_book += 1
        else:
            raise ValueError(f'Карточки читателя с именем {reader_name} не было найдено.')

    # Добавление читателя
    def add_reader(self, reader: BookCard):
        if isinstance(reader, BookCard):
            self.readers.append(reader)
        else:
            raise AttributeError(f'Некорректный тип данных.')
