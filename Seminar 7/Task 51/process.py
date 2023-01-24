def search(sn):
    res_list = []
    path = 'Seminar 7\Task 51\data.txt'
    with open(path, 'r', encoding='utf-8') as file:
        while True:
            # сперва мы считываем данные до того момента, как дойдем до двух переходов строк (# если в файле нет пустых строчек, то он всё равно их читает, как пустые, останавливаемся по двум пустым строчкам в конце перечня)
            my_book = file.readline()
            # другой вариант записи if my_book == "" (равно пустой строке). Пустая строка это False
            if not my_book:
                if not file.readline():
                    break
            if my_book.rstrip() == sn:  # Метод str.rstrip () в Python, обрезает символы на конце строки, а их нужно обрезать, т.к. там есть непечатные символы переходов на следующую строку
                res_list.append(sn.capitalize())
                for i in range(1, 5):
                    res_list.append(file.readline().rstrip().capitalize())
                res_list.append('')
    if len(res_list) > 0:
        print()
        return res_list
    return 'Таких людей не найдено'


def export(res):
    path = 'Seminar 7\Task 51\data.txt'
    with open(path, 'a', encoding='utf-8') as file:
        # file.write('\n')
        for ind in range(5):
            file.write(res[ind] + '\n')
        file.write(res[5])
