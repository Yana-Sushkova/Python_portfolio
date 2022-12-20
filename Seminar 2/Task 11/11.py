""" Задача 11: Напишите программу, которая принимает на вход число N и 
выдаёт последовательность из N членов.
Пример:
- Для N = 5: 1, -3, 9, -27, 81 """


""" 
Решение 1
N = 5

for i in range(N):
    print((-3) ** i, end=',') """

""" 
Решение 2
N = int(input())

for i in range(N - 1):
    print((-3) **i, end=", ")
print((-3) **(N - 1)) """

#Решение 3
n = int(input())
out_list = []
for i in range(n):
    out_list.append((-3) **i)
print(*out_list, sep=", ")
