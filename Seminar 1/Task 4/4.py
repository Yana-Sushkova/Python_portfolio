""" Задача 4: Напишите программу, которая будет принимать на вход дробь и 
 показывать первую цифру дробной части числа.
    
    *Примеры:*
    
    - 6,78 -> 7
    - 5 -> нет
    - 0,34 -> 3 """

""" 
Решение 1
number = input('')

commePos=number.find(',')

if ',' not in number:
    print('нет')
else:
    print (number[commePos+1]) """

""" #Решение 2
a = float(input())
if a % 1 == 0:  # условие проверки, что число целое
    print('нет')
else:
    print(int(a*10) % 10) """

#Решение 3
a = input()
if "," in a:
    #ind = a.index(",")
    #print(a[ind+1])
    print(a[a.index(",")+1])
else:
    print('нет')
