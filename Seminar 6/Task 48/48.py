""" Задача 48:. Еще немного о друзьях
Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) 
своих N друзей. Создайте список friends и добавьте в него N словарей с 
ключами name и age. Выведите средний возраст всех друзей и самое длинное имя.
# Ввод:
>> 3 # Количество друзей
>> Иван
>> 12
>> Иннокентий
>> 20
>> Леша
>> 10
# Вывод:
>> 14
>> Иннокентий """

from statistics import mean
import os
os.system('cls||clear')

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

''' # Выводим список друзей консоль
print(friends) '''
""" # Выводим все словари друзей в консоль
for friend in friends:
    print(friend) """

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


''' print(lst2)
print(lst5)
 '''

print("Средний возраст друзей:", mean(lst2))
print("Самое длинное имя:", max(lst5, key=len))
