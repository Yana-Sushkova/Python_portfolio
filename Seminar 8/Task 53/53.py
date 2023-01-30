''' Задача 53.
Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром
Цезаря и возвращает его. Шифр Цезаря заменяет каждую букву в тексте на букву, которая
отстоит в алфавите на некоторое фиксированное число позиций.
В функцию передается сообщение и сдвиг алфавита. Если сдвиг не указан, то пусть ваша
функция кодирует сдвиг алфавита на 3 позиции:
А→Г,А→Г,
Б→Д,Б→Д,
В→Е,В→Е,
......
Э→А,Э→А,
Ю→Б,Ю→Б,
Я→ВЯ→В
Все символы, кроме русских букв должны остаться неизменными. Маленькие буквы должны
превращаться в маленькие, большие — в большие.
Напишите также функцию декодирования decrypt_caesar(msg, shift), также
использующую сдвиг по умолчанию. При написании функции декодирования используйте
вашу функцию кодирования. '''

def encrypt_caesar(message, shear):
    alphabet_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
    encrypted_Message = ''
    for i in message:
        place = alphabet_RU.find(i)
        new_place = place + shear
        if i in alphabet_RU:
            encrypted_Message += alphabet_RU[new_place]
        else:
            encrypted_Message += i
    return encrypted_Message


def decrypt_caesar(message, shear):
    alphabet_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
    decrypted_Message = ''
    for i in message:
        place = alphabet_RU.find(i)
        new_place = place - shear
        if i in alphabet_RU:
            decrypted_Message += alphabet_RU[new_place]
        else:
            decrypted_Message += i
    return decrypted_Message


msg = "Да здравствует салат Цезарь!"
shift = 3
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)