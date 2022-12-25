# Функция для форматирования рамок
def text_format(menu_strings):
    max_len = max([len(x) for x in menu_strings])
    menu_strings = [f'| {string}{" " * (max_len - len(string) + 2)} |\n' for string in menu_strings]
    menu = f'+{"-" * (max_len + 4)}+\n' \
           f'{"".join(menu_strings)}' \
           f'+{"-" * (max_len + 4)}+\n'
    return menu
