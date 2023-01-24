# Метод разбирающий вводимую строку на составляющие
def processing (some_str):
   some_list = some_str.split() 
   # записываем элементы списка в операнды  с помощью параллельного присваивания
   a, b, symbol = float(some_list[0]), float(some_list[2]), some_list[1]
   return a, b, symbol # вернется кортеж