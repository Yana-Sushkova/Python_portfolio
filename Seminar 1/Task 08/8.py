"""   Задача 8: Напишите программу, которая принимает на вход координаты точки (X и Y),
    причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
    в которой находится эта точка (или на какой оси она находится).

    Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3 """

def GetPointArea(x, y):
    if x == 0 and y == 0:
        print("Некорректные данные, X ≠ 0 и Y ≠ 0")
    elif x == 0:
        print("Ось Y")
    elif y == 0:
        print("Ось X")
    elif x > 0 and y > 0:
        print("1 четверть")
    elif x < 0 and y > 0:
        print("2 четверть")
    elif x < 0 and y < 0:
        print("3 четверть")
    else:
        print("4 четверть")

import os
os.system('cls||clear')

x, y = int(input('Введите X: ')), int(input('Введите Y: '))

GetPointArea(x, y)
