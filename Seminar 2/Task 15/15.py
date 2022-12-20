""" Задача 15:
Напишите программу, которая принимает на вход число 
N и выдает набор произведений чисел от 1 до N.
Пример:
Пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

import os
os.system('cls||clear')


""" #Решение 1
input_number = int(input('Введите число N = '))

print("[",  end=" ")
product = 1
for i in range (input_number):
    product *= i+1
    print(product, end=' ') 
print("]",  end=" ") """

# Решение 2
input_number = int(input('Введите число: '))
product_list = [1]

for i in range(1, input_number):
    product_list.append((i+1) * product_list[i-1])

print(product_list)
