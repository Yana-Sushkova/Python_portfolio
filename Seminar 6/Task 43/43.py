""" Задача 43: Создайте список из случаных чисел. 
Найдите максимальное количество его одинаковых элементов. """

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

#Решение 1
""" dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
for i in lst:
    dict[i]=dict[i]+1
print(dict)

count = 0
for i in range(0, len(dict)):
    if dict[i] > count:
        count = dict[i]
print("Максимальное количество одинаковых элементов", count) """

#Решение 2
max_count = 0 
for i in range (0,len(lst)):
    if lst.count(lst[i]) > max_count: # count показывает количсетво вхождений элемента в список
        max_count=lst.count(lst[i])
print("Максимальное количество одинаковых элементов", max_count)
