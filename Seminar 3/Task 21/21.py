""" Задача 21: Напишите программу, которая определит позицию второго вхождения 
строки в списке либо сообщит, что её нет.
Пример:
- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1 #неверный пример
- список: [], ищем: "123", ответ: -1 """

""" #Решение 1
string = input('Введите исходную строку:')
simbol = input()
test_list = ''
test_item = string.split()

def check_list(test_list, test_item):
    count = 0
    for i in range(len(test_list)):
        if test_list[i] == test_item:
            count += 1
            if count == 2:
                return i
    else:
        return -1

print(f"ответ: {check_list(test_list, test_item)}") """

#Решение 2
a = input().split()
find_str = input()
count = 0
for i in range(len(a)):
    if a[i] == find_str:
        count += 1
        if count == 2:
            print(i)
            break
else:
    print(-1)