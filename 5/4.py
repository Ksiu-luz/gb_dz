"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
"""


def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt) - 1):
        if txt[i] == txt[i + 1]:
            count += 1
        else:
            res += str(count) + txt[i]
            count = 1
    if count > 1 or (txt[-2] != txt[-1]):
        res += str(count) + txt[-1]
    return res


def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if txt[i].isdigit():
            number += txt[i]
        else:
            res += txt[i] * int(number)
            number = ''
    return res


text = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(text)}")
print(f"Текст после дешифровки: {decoding(coding(text))}")
