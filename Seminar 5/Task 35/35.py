""" Задача 35: В файле находится N натуральных чисел, записанных через пробел.
Среди чисел не хватает одного, 
чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число. """

with open('file35.txt', 'r', encoding='utf-8') as file:
    some_list = file.read().split()
print(some_list)

some_list = list(map(int, some_list))
""" new_list = [some_list[i]+1 for i in range(len(some_list)-1) if some_list[i]+1 != some_list[i+1]]
print(new_list) """

new_list =[]
for i in range(len(some_list)-1):
    #if some_list[i]+1 != some_list[i+1]:
    #if some_list[i] != some_list[i+1]-1:
    if some_list[i+1]-1 != some_list[i]:
        new_list.append(some_list[i]+1)
print(new_list)

