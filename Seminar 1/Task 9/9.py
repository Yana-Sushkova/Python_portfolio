"""   Задача 9: Напишите программу, которая по заданному номеру четверти, 
показывает диапазон возможных координат точек в этой четверти (x и y).

Пример:
нет """

def GetXYArea(chetvert):
    if chetvert == 1:
        return print("x > 0 and y > 0")
    elif chetvert == 2:
        return print("x < 0 and y > 0")
    elif chetvert == 3:
        return print("x < 0 and y < 0")
    elif chetvert == 4:
        return print("x > 0 and y < 0")
    else:
        return print("Такой четверти нет, должно быть число от 1 до 4")

import os
os.system('cls||clear')

chetvert = int(input('Введите номер четверти: '))

GetXYArea(chetvert)
