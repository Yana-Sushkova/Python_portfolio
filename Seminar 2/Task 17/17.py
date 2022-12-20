# Задача №17: Реализуйте алгоритм перемешивания списка.

import random
import os
os.system('cls||clear')

lst = [1, 2, 3, 4, 5]
print(f"Исходный список:\n{lst}")
random.shuffle(lst)
print(f"Список после перемешивания:\n{lst}")
