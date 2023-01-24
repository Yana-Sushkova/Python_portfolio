def inp_mod():
    mod = input('Введите режим работы (поиск или экспорт): ')
    return mod


def inp_import():
    surname = input('Введите Фамилию для поиска: ').lower()
    return surname


def view_import(result):
    print(*result, sep='\n')


def inp_export():
    surname = input('Введите Фамилию: ').lower()
    name = input('Введите Имя: ').lower()
    sec_name = input('Введите Отчество: ').lower()
    phone = input('Введите телефон: ').lower()
    comment = input('Введите тип телефона (домашний, рабочий): ').lower()
    return '\n', surname, name, sec_name, phone, comment


def view_import_no():
    print(f'Данные не найдены.')


def view_export():
    print(f'\nВведенные данные успешно сохранены.')
