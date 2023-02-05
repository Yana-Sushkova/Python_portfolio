""" Задача 45:  Создайте список из случайных чисел. 
Найдите количество различных элементов в нем.
Пример:
В числе 3734 количество различных элементов = 3. """

from random import randint
import os
os.system('cls||clear')

lst = []
for el in range(5):
    lst.append(randint(1, 10))
print(lst)

# или 
# import random
# lst = [random.randit(1,10) for _ in range(5)]

# Решение 1

count = 0
unique_lst = []
for el in lst:
    if el not in unique_lst:
        count += 1
        unique_lst.append(el)
print(len(unique_lst))

# Решение 2
print(len(set(lst)))

# или 
# some_set = set(lst)
# print(len(some_set))

