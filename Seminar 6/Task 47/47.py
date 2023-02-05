""" Задача 47: Старший и младший
Пользователь вводит число N. 
Затем он вводит личные данные (имя и возраст) своих N друзей. 
Создайте список friends и добавьте в него N словарей с ключами name и age. 
Найдите самого младшего из друзей и выведите его имя. 
Пример:
>> 3 # Количество друзей
>> Иван
>> 11
>> Саша
>> 12
>> Леша
>> 10
# Вывод:
>> Леша """

import sys
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

# print(friends)

# Выводим список друзей консоль

# """ # Выводим все словари друзей в консоль
# for friend in friends:
#     print(friend) """

min_age = sys.maxsize
min_fr = ()
for friend in friends[:]:
    # get возвращает значение по указанному ключу
    min_key = min(friend, key=friend.get)
    if min_age > friend.get(min_key):
        min_age = friend.get(min_key)
        min_fr = min_key

key (необязательно) ‒ ключевая функция, в которую передаются итерации, 
и выполняется сравнение на основе ее возвращаемого значения; 

print("Возраст самого младшего из друзей:", min_age)
print("Имя самого младшего друга:", min_fr) '''

''' # Решение 2 (ВЕРНОЕ)

N = int(input("Введите количество друзей: "))
friends = []
min_age = sys.maxsize
min_name =""
for friend_number in range(N):
    name = input("Введите имя друга: ")
    age = int(input("Введите возраст друга: "))
    if age < min_age:
        min_age = age
        min_name = name
    # Добавляем нового друга в список
    friends.append({"name": name, "age": age})
print(friends)
print(f"Имя самого младшего друга: {min_name}, \nВозраст самого младшего из друзей: {min_age}")   '''

# Решение 3 (ВЕРНОЕ)

N = int(input("Введите количество друзей: "))
friends = []

for friend_number in range(N):
    name = input("Введите имя друга: ")
    age = int(input("Введите возраст друга: "))
# Добавляем нового друга в список
    friends.append({"name": name, "age": age})
print(friends)
min_age = friends[0]['age'] # первый словарь, который нулевой элемент списка и в нем ключ "age"
for some_dict in friends:
    if some_dict['age'] < min_age: #значение меньше ли значение ключа 'age', чем мин.возраст
        min_age = some_dict['age'] # переприсваеваем минимальный возраст
for some_dict in friends:
        if some_dict['age'] == min_age:
            print(some_dict['name'])
            break
