""" Задача 2: Напишите программу, которая на вход принимает 5 чисел 
и находит максимальное из них.
    
    Примеры:
    
    - 1, 4, 8, 7, 5 -> 8
    - 78, 55, 36, 90, 2 -> 90
 """

import os
os.system('cls||clear')

""" Решение 1
some_list = []
for _ in range(5):
    x = int (input())
    some_list.append(x) # Функции append() и extend() в Python 
#добавляют элемент в конец списка или в другой список, подробно разберем методы на примерах
#print(f"Максимальное значение - {max(some_list)}") #такое решение не хорошее т.к. используется 2 цикла """

""" Решение 2
some_list = []
for _ in range(5):
    x = int (input())
    some_list.append(x)
maxx = some_list[0]
for el in some_list:
    if el > maxx:
        maxx=el
print (f"{maxx} max")
 """
"""Решение 3
some_list = []
for _ in range(5):
    x = int (input())
    some_list.append(x)
maxx = some_list[0]
for ind in range(5):
    if some_list[ind] > maxx:
        maxx = some_list [ind]
print(maxx) """

#Решение 4
maxx = int(input())
for _ in range(4):
    x = int(input())
    if x > maxx:
        maxx = x

print (f"{maxx} max")
