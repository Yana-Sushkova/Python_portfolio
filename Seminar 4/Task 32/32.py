""" 
Задача 32: Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности. 
Пример: [2,2,3,5] => [3,5] """

""" # Решение 1
lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
#[new_lst.append(i) for i in lst if i not in new_lst] упрощенная запись
print(f"Список из неповторяющихся элементов: {new_lst}") """

""" # Решение 2
lst = [1, 3, 5, 4, 9, 14, 5, 1]
new_lst = []
new_lst = list(set(lst))
print(new_lst) """

""" # Решение 3
from random import randint

def create_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def get_unic_value(list):
    return [i for i in set(list)]

size = 10
m = 1
n = 10

origin = create_list(size, m, n)
print(origin)
print(get_unic_value(origin)) """

#предыдущие решения не убирают повторы из конечного списка, согласно примеру, который привели на семинаре
# Решение 4 (верное)

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
for i in range (0, len(lst)):
   duplicate = 0
   for j in range(0, len(lst)):
       if i != j:
           if lst[i] == lst[j]:
               duplicate = 1
   if duplicate == 0:
       new_lst.append(lst[i])

print(f"Список без повторов: {new_lst}")
