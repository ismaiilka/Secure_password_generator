from functions import *

while True:
    quantity = input('Введите количество паролей для генерации:\n')
    if quantity.isdigit():
        quantity = int(quantity)
        break
    else:
        print('Некорректный ответ')
        continue

while True:
    length = input('Длина одного пароля:\n')
    if length.isdigit():
        length = int(length)
        break
    else:
        print('Некорректный ответ')
        continue

while True:
    flag_digits = input('Включать ли цифры?\n')
    if flag_digits.lower() == 'да':
        chars += digits
        break
    elif flag_digits.lower() == 'нет':
        break
    else:
        print('Некорректный ответ')
        continue

while True:
    flag_lowercase_letters = input('Включать ли строчные буквы?\n')
    if flag_lowercase_letters.lower() == 'да':
        chars += lowercase_letters
        break
    elif flag_lowercase_letters.lower() == 'нет':
        break
    else:
        print('Некорректный ответ')
        continue

while True:
    flag_uppercase_letters = input('Включать ли прописные буквы?\n')
    if flag_uppercase_letters.lower() == 'да':
        chars += uppercase_letters
        break
    elif flag_uppercase_letters.lower() == 'нет':
        break
    else:
        print('Некорректный ответ')
        continue

while True:
    flag_special_symbols = input('Включать ли спецсимволы?\n')
    if flag_special_symbols.lower() == 'да':
        chars += punctuation
        break
    elif flag_special_symbols.lower() == 'нет':
        break
    else:
        print('Некорректный ответ')
        continue

while True:
    flag_ambiguous_symbols = input('Исключать ли неоднозначные символы il1Lo0O?\n')
    if flag_ambiguous_symbols.lower() == 'да':
        chars = chars.replace('i', '')
        chars = chars.replace('l', '')
        chars = chars.replace('1', '')
        chars = chars.replace('L', '')
        chars = chars.replace('o', '')
        chars = chars.replace('0', '')
        chars = chars.replace('O', '')
        break
    elif flag_ambiguous_symbols.lower() == 'нет':
        break
    else:
        print('Некорректный ответ')
        continue

for _ in range(quantity):
    generate_password(length, chars)