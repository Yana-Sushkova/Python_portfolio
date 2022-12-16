"""   Задача 10: Напишите программу, которая принимает на вход координаты двух 
точек и находит расстояние между ними в 2D пространстве.

Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
 """


def Distance(x1, x2, y1, y2):
    result = (pow(x2 - x1, 2) + pow(y2 - y1, 2))**0.5
    return result


print('Введите координаты первой точки X1, Y1: ')
x1 = int(input())
y1 = int(input())

print('Введите координаты второй точки X2, Y2: ')
x2 = int(input())
y2 = int(input())

result = Distance(x1, x2, y1, y2)

print(round(result, 2))
