from book_card import BookCard


class Librarian:
    __instance = None
    __instance_amount = 0

    # В библиотеке может работать не более 3х библиотекарей
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None or cls.__instance_amount < 3:
            cls.__instance = super().__new__(cls)
            cls.__instance_amount += 1
            return cls.__instance
        else:
            raise Exception('У данного класса может быть только 3 экземпляра')

    def __init__(self, name):
        self.name = name
        self.__password = 'NewLib14'

    @property
    def password(self):
        return self.__password

    def __str__(self):
        return self.name

    # Создание книжной карты
    def lend_book_card(self, customer_name, customer_num):
        assert customer_name.isdigit() is False, f'Нужно ввести имя, а не число.'
        assert customer_num.isdigit(), f'Нужно ввести номер читателя.'
        customer_num = int(customer_num)

        book_card = BookCard(customer_name, customer_num, self.name)
        return book_card
