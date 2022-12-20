""" Задача 14:
Напишите программу, которая принимает на вход 
вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11 """

import os


def get_sum(number):
    if float(number) < 0:
        number = float(number) * (-1)

    temp_num = 0
    for i in str(number):
        if i != '.':
            temp_num += int(i)
    return temp_num


os.system('cls||clear')

input_number = input('Введите число: ')

print(f'Сумма чисел равна {get_sum(input_number)}')
