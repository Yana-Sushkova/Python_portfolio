""" Задача 36: Дан список чисел. Создайте список, в который попадают числа, 
описываемые возрастающую последовательность. Порядок элементов менять нельзя. 
Выводим все возрастающие последовательности
*Пример:*
[1, 5, 2, 3, 4, 6, 1, 7] ⇒ [1,5] и [1,7] и [2,3,4,6] """

import random
some_list = [random.randint(1, 10) for i in range(10)]
print(some_list)
some_list.append(0)
ind = 0
res_list = []
temp_list = []
while ind < len(some_list) - 1:
    if some_list[ind] < some_list[ind + 1]:
        temp_list.append(some_list[ind])
    else:
        if len(temp_list) != 0:
            temp_list.append(some_list[ind])
            res_list.append(temp_list)
            temp_list = []
    ind += 1
print(res_list)

