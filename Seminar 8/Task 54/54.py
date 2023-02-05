#Задача 54: Напишите игру "крестики-нолики"с двумя игроками.

# список внутри списков - матрица - двумерный массив
# сперва ходят крестики

def check_win_draw(some_field):
    a1 = some_field[0][0]
    a2 = some_field[0][1]
    a3 = some_field[0][2]
    b1 = some_field[1][0]
    b2 = some_field[1][1]
    b3 = some_field[1][2]
    c1 = some_field[2][0]
    c2 = some_field[2][1]
    c3 = some_field[2][2]
    if a1 == a2 == a3 != '-':
        return f'Победа {a1}'
    elif b1 == b2 == b3 != '-':
        return f'Победа {b1}'
    elif c1 == c2 == c3 != '-':
        return f'Победа {c1}'
    elif a1 == b1 == c1 != '-':
        return f'Победа {a1}'
    elif a2 == b2 == c2 != '-':
        return f'Победа {a2}'
    elif a3 == b3 == c3 != '-':
     return f'Победа {a3}'
    elif a1 == b2 == c3 != '-':
        return f'Победа {a1}'
    elif a3 == b2 == c1 != '-':
        return f'Победа {a3}'
    elif field[0].count('-') == 0 and field[1].count('-') == 0 and field[2].count('-') == 0: # условия что количества элементов в указанных строках равны нулю
        return 'Ничья'
    else:
        return False

field = [['-' for _ in range(3)] for _ in range(3)]
# вывод поля без скобочек
for row in field: # проходим списки строк
    for col in row: # берем  элементы внутри строк
        print(col, end=" ") # выводим элементы через пробел
    print() # после строки выводим пробел
# вывод поля со скобками
print(*field, sep='\n')
letter_number = {'a': 0, 'b': 1, 'c': 2}
while True:
    x = input('Ходит Х. Введите номер клетки в формате "букву строки : номер столбца": ')
    # проверка на невозможность ввода на уже введенные позиции
    if field[letter_number[x[0]]][int(x[-1]) - 1] != '-':
        print('Эта клетка уже занята')
        continue
    field[letter_number[x[0]]][int(x[-1]) - 1] = 'X'
    if check_win_draw(field):
        print(check_win_draw(field))
        break  
    o = input('Ходит 0. Введите номер клетки в формате "букву строки : номер столбца": ') 
    while field[letter_number[o[0]]][int(o[-1]) - 1] != '-':
        print('Эта клетка уже занята')
        o = input('Ходит 0. Введите номер клетки в формате "букву строки : номер столбца": ') 
    field[letter_number[o[0]]][int(o[-1]) - 1] = '0'
    if check_win_draw(field):
        print(check_win_draw(field))
        break
    print(*field, sep='\n')
    print('Играем дальше')
