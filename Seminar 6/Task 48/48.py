""" Задача 48:. Еще немного о друзьях
Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) 
своих N друзей. Создайте список friends и добавьте в него N словарей с 
ключами name и age. Выведите средний возраст всех друзей и самое длинное имя. """

from statistics import mean
import os
os.system('cls||clear')

''' # Решение 1 (НЕ ВЕРНОЕ, Т.К. ДОЖНО БЫТЬ {"name": name, "age":age})
# Создание пустого списка для хранения данных пользователей
friends = []

# Создание новых пользователей

N = int(input("Введите количество друзей: "))
for friend_number in range(N):
    name = input("Введите имя друга: ")
    age = int(input("Введите возраст друга: "))
    # Создаём словарь для нового друга
    new_friend = {name: age}
    # Добавляем нового друга в список
    friends.append(new_friend)

# Выводим список друзей консоль
print(friends)
# Выводим все словари друзей в консоль
#for friend in friends:
    #print(friend)

lst2 = []
lst5 = []
for friend in friends[:]:
    # dict1=friend.values()
    # list3=list(dict1)
    # first=list3[0]
    # lst2.append(first)
    lst2.append(list(friend.values())[0])

    # dict2=friend.keys()
    # lst4=list(dict2)
    # first2=lst4[0]
    # lst5.append(first2)
    lst5.append(list(friend.keys())[0])


# print(lst2)
# print(lst5)

print("Средний возраст друзей:", mean(lst2))
print("Самое длинное имя:", max(lst5, key=len)) '''


# Решение 2
N = int(input("Введите количество друзей: "))
dict_list = []
for friend_number in range(N):
    name = input("Введите имя друга: ")
    age = int(input("Введите возраст друга: "))
    dict_list.append({"name": name, "age": age})
print(dict_list)

summa = 0
max_name = dict_list[0]['name']
for i in dict_list:
    summa += i['age']
    if len(i['name']) > len(max_name): # сравнивать нужно именно длину, т.к. сравнение строк идет лексиграфически, т.е. по алфавиту
        max_name = i['name']
print("Средний возраст друзей:", summa / N)
print("Самое длинное имя:", max_name)

# или

name_list = [i["name"] for i in dict_list]
age_list = [i["age"] for i in dict_list]
print(sum(age_list)/N)

# Пример сборки словарей в один большой словарь

print(dict_list)
big_dict = {'name': [], 'age': []}
for el in dict_list:
    big_dict['name'].append(el['name'])
    big_dict['age'].append(el['age'])
print(big_dict)

# Вывод значений словарей в списки

print(list(big_dict.values()))
