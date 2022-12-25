from library import Library
from librarian import Librarian
from help_func import text_format


lib = Library()
lib_worker = Librarian('Татьяна Викторовна')  # Пароль NewLib14


main_menu = ['1. Добавить новую книгу в библиотеку', '2. Посмотреть список всех доступных книг',
             '3. Проверить наличие книги', '4. Удалить книгу из базы', '5. Добавить читателя',
             '6. Выдать книгу/и', '7. Вернуть книгу', '', '0. Завершить работу программы']


while True:
    print(lib)
    user_choose = int(input(text_format(main_menu) + '->: ').strip())

    # Добавление новой книги в библиотеку
    if user_choose == 1:
        enter_pas = input('Введите пароль: \n->: ')
        if enter_pas == lib_worker.password:
            lib.add_book_to_storage()
        else:
            raise ValueError('Неверный пароль')

    # Вывод всех книг в библиотеке
    elif user_choose == 2:
        sorting_option = ['1. Алфавитный порядок(R)', '2. По количеству копий',
                          '3. По количеству копий(R)', '4. По жанрам', '', 'Enter для стандартного вывода:',
                          '\'Алфавитный порядок\'']
        sorting_option = input(text_format(sorting_option) + '->: ').strip()

        if len(sorting_option) == 0:
            sorting_option = 0
        elif sorting_option.isdigit():
            sorting_option = int(sorting_option)
        else:
            raise TypeError('Нужно вводить целое число.')

        lib.get_books(sorting_option)

    # Проверка наличия книги в библиотеке
    elif user_choose == 3:
        current_book_title = input('Название искомой книги: \n->: ').strip().title()
        # Выводится подробная информация о книге
        print(lib.find_book(current_book_title).get_info())

    # Удаление книги из базы
    elif user_choose == 4:
        enter_pas = input('Введите пароль: \n->: ')
        if enter_pas == lib_worker.password:
            unnecessary_book = input('Введите название книги которую вы хотите удалить:\n->: ').strip().title()
            lib.del_book_from_storage(unnecessary_book)
            print('Книга была успешно удалена.')
        else:
            raise ValueError('Неверный пароль.')

    # Добавление читателя в базу
    elif user_choose == 5:
        enter_pas = input('Введите пароль: \n->: ')
        if enter_pas == lib_worker.password:
            cust_name = input('Введите имя читателя:\n->: ').strip().title()
            cust_num = input('Введите номер читателя:\n->: ').strip()

            lib.add_reader(lib_worker.lend_book_card(cust_name, cust_num))
            print('Читатель был успешно добавлен.')
        else:
            raise ValueError('Неверный пароль')

    # Выдать книгу читателю
    elif user_choose == 6:
        enter_pas = input('Введите пароль: \n->: ')
        if enter_pas == lib_worker.password:
            necessary_book = input('Введите название книги которую вы хотите взять:\n->: ').strip().title()
            reader_name = input('Введите имя читателя:\n->: ').strip().title()
            lib.take_book(reader_name, necessary_book)
        else:
            raise ValueError('Неверный пароль')

    # Вернуть книгу
    elif user_choose == 7:
        enter_pas = input('Введите пароль: \n->: ')
        if enter_pas == lib_worker.password:
            necessary_book = input('Введите название книги которую вы хотите взять:\n->: ').strip().title()
            reader_name = input('Введите имя читателя:\n->: ').strip().title()
            lib.return_book(reader_name, necessary_book)
        else:
            raise ValueError('Неверный пароль')

    elif user_choose == 0:
        break
