""" Задача 1: Напишите программу, которая принимает на вход два числа 
и проверяет, является ли одно число квадратом другого.
Примеры:
- 5, 25 -> да
- 4, 16 -> да
- 25, 5 -> да
- 8,9 -> нет """

import os
os.system('cls||clear')

number1 = int (input('Введите первое число: '))
number2 = int (input('Введите второе число: '))

if number1**2==number2 or number2**2==number1:
    print('Да, одно число квадрат другого')
else: 
    print('Нет, одно число не квадрат другого')