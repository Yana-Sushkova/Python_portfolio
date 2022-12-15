""" Задача 3: Напишите программу, которая будет на вход принимать 
число N и выводить числа от -N до N
    
    *Примеры:* 
    
    - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5 """


""" 
Решение 1
number = int (input('Введите число: '))
numbers = list(range(-number,number+1))
print(*numbers, sep=', ') """

""" 
Решение 2
number = int (input('Введите число: ')) 
for i in range(-number,number): 
    print(i, end=', ')
print(number) #ухищрение, чтобы не было , после последнего числа """

""" 
Решение 3
number = int (input('Введите число: '))
print(*list(range(-number,number+1)), sep=', ') """

"""
Решение 4
number = int (input('Введите число: '))
some_list = []
for i in range(-number,number+1):
    some_list.append(i)
print(*some_list, sep=', ') """

#Решение 5
number = int (input('Введите число: '))
print(*range(-number,number+1), sep=', ') #*нужна для распаковки
