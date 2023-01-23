""" Задача 44: Создайте список из случаных чисел. Найдите второй максимум.
Пример:
а=[1,2,3] #Первый максимум == 3, второй ==2 """

import random
n = int(input("Сколько элементов? "))
lst = []
for i in range(n):
    lst.append(random.randint(1,10)) # random.randint - функция возвращает случайное целое число из указанного диапазона
print("Сформирован список: ", lst)

""" или 
from random import randint
lst=[]
for el in range(10):
    lst.append(randint(1, 10))
print(lst)  """

max_num = max (lst)
lst2 = []
for i in range(0,len(lst)):
    if lst[i] != max_num:
        lst2.append(lst[i])

max_num = max (lst2)
print(lst2, max_num)
