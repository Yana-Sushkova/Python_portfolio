""" 
Задача 28: Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    1)	с помощью математических формул нахождения корней квадратного уравнения;
    2)	с помощью дополнительных библиотек Python. """

# 1 Вариант
with open('input28.txt', 'r', encoding='utf-8') as file:
    line = file.readline().split()
    a, b, c = int(line[0]), int(line[1]), int(line[2])
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('Корней нет')
    elif d == 0:
        print(-b / 2 * a)
    else:
        print((-b + d ** 0.5) / 2 * a)
        print((-b - d ** 0.5) / 2 * a)

# 2 Вариант
"""terminal -> pip install sympy""" #скачиваем стороннюю бибилиотеку
a = 5
b = 1
c = 6
import sympy
x = sympy.Symbol('x')
print(sympy.solve(f'{a}* x ** 2 + {b} * x + {c}'))