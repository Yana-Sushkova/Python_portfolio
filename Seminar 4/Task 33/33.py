""" Задача 33: Задана натуральная степень k. 
Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен 
степени k. 
Пример:
k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
import random


def write_file1(st):
    with open('file33_1.txt', 'w') as data:
        data.write(st)

def write_file2(st):
    with open('file33_2.txt', 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0, 101) #  возвращает случайное целое число из указанного диапазона


def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst


def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

# Создаю 2 файла для того, чтобы взять их в качестве исходных данных к задаче 34
k1 = int(input("Введите натуральную степень k1 = "))
koef1 = create_mn(k1)
write_file1(create_str(koef1))

k2 = int(input("Введите натуральную степень k2 = "))
koef2 = create_mn(k2)
write_file2(create_str(koef2))

with open('file33_1.txt', 'r') as data:
    st1 = data.readlines()
with open('file33_2.txt', 'r') as data:
    st2 = data.readlines()

print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")