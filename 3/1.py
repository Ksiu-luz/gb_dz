# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной идексах.
#
# Пример:
#
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

from random import randint

array = list(randint(0, 100) for _ in range(10))
result = 0
for i in range(1, len(array), 2):
    result += i

print(result)
