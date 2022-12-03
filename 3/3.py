# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 10.01] => 0.19
from random import uniform

array = list((round(uniform(0, 10), 3) for _ in range(5)))
temp_array = list(round(array[i] % 1, 3) for i in range(len(array)))
print(array)
print(round(max(temp_array) - min(temp_array), 3))
