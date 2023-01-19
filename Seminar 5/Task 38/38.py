""" Задача 38: Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
На семинаре говорилось или а или б или в """

import os
os.system ("cls||clear")

#Решение 1
words = ('«Человека определяют не заложенные в нем качества, а только его выбор», – Альбус Дамблдор').split(" ")
words2=[]
for word in words:
    if  "а" not in word and "б" not in word and "в" not in word:
        words2.append(word)
result_words = " ".join(words2)
print(result_words)   

#Решение 2
words = ('«Злых людей нет на свете, есть только люди несчастливые». - Га-Ноцри. М. А. Булгаков, "Мастер и Маргарита"').split(" ")
words2=list(filter(lambda word: "а" not in word and "б" not in word and "в" not in word, words))
result_words = " ".join(words2)
print(result_words)   