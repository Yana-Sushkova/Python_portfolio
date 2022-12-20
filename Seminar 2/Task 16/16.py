""" Задача 16:
Задайте список из n чисел последовательности (1 + 1/n) ** n 
и выведите на экран их сумму.
Пример:
Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
Сумма 9.06 """

import os
os.system('cls||clear')

""" #Решение 1
input_number = int(input("Введите число: "))
def get_sequence(n):
    return [round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]

print(get_sequence(input_number))
print(round(sum(get_sequence(input_number)), 2))
 """
# Решение 2
n = int(input('Введите число n = '))


def get_sequence(n):
    print("{", end=" ")
    for i in range(1, n):
        print(i, ":", round((1+1/i)**i, 2), end=", ")
    print(n, ":", round((1+1/n)**n, 2), "}")


def get_sum(n):
    return [round((1 + 1 / x)**x, 2) for x in range(1, n + 1)]


get_sequence(n)
summ = round(sum(get_sum(n)), 2)
print(f"Сумма = {summ}")
