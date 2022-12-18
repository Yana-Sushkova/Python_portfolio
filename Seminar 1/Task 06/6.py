""" Задача 6: Напишите программу, которая принимает на 
вход цифру, обозначающую день недели, и проверяет, 
является ли этот день выходным.
Примеры:
- 6 -> да
- 7 -> да
- 1 -> нет """

import os
os.system('cls||clear')

day_of_the_week = int(
    input('Введите номер дня недели, чтобы узнать выходной это день или нет: '))

while day_of_the_week > 7 or day_of_the_week < 1:
    print('Дней недели 7. Введите число от 1 до 7: ')
    day_of_the_week = int(
        input('Введите номер дня недели, чтобы узнать выходной это день или нет: '))

if day_of_the_week == 6 or day_of_the_week == 7:
    print('Да, это выходной день')
else:
    print('Нет, это НЕ выходной день')