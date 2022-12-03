# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint
from math import ceil

array = list(randint(0, 10) for _ in range(5))
result = []

for i in range(ceil(len(array) / 2)):
    result.append(array[i] * array[len(array) - 1 - i])
print(array)
print(result)
