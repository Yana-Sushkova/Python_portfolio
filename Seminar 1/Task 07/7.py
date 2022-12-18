""" # Задача 7: Напишите программу для проверки истинности 
утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

Предикат-это переменная, которая принимает значение либо истина либо ложь (0-False, 1-True)
¬ иверсия, отрицание, логическое НЕ
⋁ - or
⋀ - and
"""
import os
os.system('cls||clear')

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z, end=" -> ")
            print(not (x or y or z) == (not x and not y and not z))
