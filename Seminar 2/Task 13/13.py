""" Задача 13: Напишите программу, в которой пользователь будет задавать две строки,
а программа - определять количество вхождений одной строки в другой."""

""" 
Решение 1 через словари
n = int(input('введите число '))
slovar = {}
for i in range(1, n+1):
    slovar.update({i:3*i+1})
     
print(slovar) """

""" Решение 2
firstString = input("Первая строка: ")
secondString = input("Вторая строка: ")

max = firstString
min = secondString
if len(firstString) < len(secondString):
    max = secondString
    min = firstString

# Находим количество вхождений одной строки в другую.
print(max.count(min)) """

#Решение 3
"""аармем мем ываывамем"""
"""мем"""
str1 = input()
str2 = input()
i = 0
count = 0
""" while i < len(str1):
    if str1[i:i + len(str2)] == str2:
        count += 1
        i += len(str2)
    else:
        i += 1
print(count) """


while i < len(str1):
    sub_str=str1[i:i + len(str2)]
    tmp=str1[0:1]
    print({sub_str}, {i}, i+len(str2), tmp)
    if  sub_str == str2:
        count += 1
        i += len(str2)
    else:
        i += 1
print(count)

