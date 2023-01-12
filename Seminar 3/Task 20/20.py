""" Задача 20: Задайте список. Напишите программу, которая определит,
присутствует ли в заданном списке строк некое число. """

#Решение 1
string = input('Введите исходную строку с элементами через пробел:')
simbol = input('Введите значение для проверки его присутсвия в вышевведенной строке:')
word_list = string.split()

for i in word_list:
    for j in i:
        if j == simbol:
            print('Yes')
            exit()
print('No')


""" #Решение 2
a = input().split()
number = input()
for i in a:
    if number in i:
        print('yes')
        break
else: # этот else привязан к циклу for, блок с else будет выполняться когда не выполнится break
    print('no') """