""" Задача 24: Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между 
максимальным и минимальным значением дробной части элементов.
Пример:
[1.1, 1.2, 3.1, 5, 10.01] => 0.19
 """

import os
os.system('cls||clear')

""" 
#1 вариант преобразования элементов списка
lst = []
for i in input("Введите числа через пробел:\n").split(): #в split по умолчанию пробел 
    lst.append(float(i))
print(lst, end=" ") """

""" 
# 2 вариант преобразования элементов списка
# map () используется для применения функции к каждому элементу итерируемого объекта (например, списка или словаря) и возврата нового итератора для получения результатов
lst = list(map(float, input("Введите числа через пробел:\n").split()))
print(lst, end=" ") """

""" #Решение 1
lst = input("Введите числа через пробел:\n").split()
maxx = 0
minn = 1
for el in lst:
    if "." in el:
        number = el.split(".")[1]
        if int(number) != 0:
            if float("0." + number) < minn:
                minn = float("0." + number)
            elif float("0." + number) > maxx:
                maxx = float("0." + number)
print(maxx-minn)
 """

#Решение 2
# map () используется для применения функции к каждому элементу итерируемого объекта (например, списка или словаря) и возврата нового итератора для получения результатов
lst = list(map(float, input("Введите числа через пробел:\n").split()))
print(lst, end=" => ") 

new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
print(max(new_lst) - min(new_lst))

