""" Задача 26: Задайте число. Составьте список чисел Фибоначчи, 
в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи] """

""" #Решение 1
def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
userNumber = int(input('Введите число: '))
for e in range(1, userNumber + 1):
    list.append(Fibonacci(e))
    list.insert(0, NegaFibonacci(e))
print(list) """

""" # Решение 2
n = int(input('Введите число: '))
negofibonacci = [1,-1]
fibonacci = [1,1]

for i in range(2,n):
    list = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(list)
    list2 = negofibonacci[i-2] - negofibonacci[i-1]
    negofibonacci.append(list2)

negofibonacci.reverse()
fibonacci.insert(0, 0) #принимает в качестве первого аргумента позицию, на которую нужно вставить элемент, а вторым — сам элемент.

print(f' Для {n} => {negofibonacci+fibonacci}') """

# Решение 3

k = int(input())
some_list = [0] * (k * 2 + 1)
some_list[k + 1] = 1
some_list[k - 1] = 1
for ind in range(k + 2, k * 2 + 1):
    some_list[ind] = some_list[ind - 1] + some_list[ind - 2]
for ind in range(k - 2, -1, -1): #шаг -1
    some_list[ind] = some_list[ind + 2] - some_list[ind + 1]
print(some_list)