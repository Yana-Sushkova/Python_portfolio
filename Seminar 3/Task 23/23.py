""" Задача 23: Напишите программу, которая найдёт 
произведение пар чисел списка. Парой считаем первый и 
последний элемент, второй и предпоследний и т.д.
Пример:
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]
 """

import os
os.system('cls||clear')

lst = []
for i in input("Введите числа через пробел:\n").split():  # в split по умолчанию пробел
    lst.append(int(i))
print(lst, end=" ")

""" 
другой способ вывода списка
lst = input("Введите числа через пробел:\n").split() #в split по умолчанию пробел 
lst1 = []
for i in range(1, len(lst)+1):
    lst1.append(int(lst[i-1]))
print(lst1, end=" ") """

# Решение 1
new_lst = []
for start in range(0, (len(lst)-1)//2+1):
    new_lst.append(int(lst[start])*int(lst[len(lst)-start-1]))
print(f"=> {new_lst}")

""" #Решение 2
new_lst=[]
if len(lst)%2==0:
    middle = len(lst)//2
else:
    middle = len(lst)//2+1
for start in range(0, middle):
    new_lst.append(int(lst[start])*int(lst[len(lst)-start-1]))
print(f"=> {new_lst}") """
