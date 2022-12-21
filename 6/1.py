"""
Занятие 4
Задайте последовательность чисел. Напишите программу,
которая выведет список неповторяющихся элементов исходной последовательности.
Ввод: [1, 1, 2, 3, 4, 4, 4]
Вывод: [2, 3]
"""


def unique_elems(array):
    result = []
    for elem in array:
        if array.count(elem) == 1:
            result.append(elem)
    return result


if __name__ == "__main__":
    elems_list = list(map(int, input('введите последовательность чисел через пробел: ').split())) # <---
    print(unique_elems(elems_list))

"""
Занятие 4
Задана натуральная степень k.
Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
- k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
"""
from random import randint


def create_polynomial(file_name, k):
    odds = list(randint(0, 100) for _ in range(k + 1)) # <----
    with open(file_name, 'w') as f:
        for i in range(k, 1, -1):
            f.write(f'{odds.pop()}*(x**{i}) + ')
        f.write(f'{odds.pop()}*x + {odds.pop()} = 0')


if __name__ == "__main__":
    k = int(input('введите степень k: '))
    create_polynomial('polinom1.txt', k)
    k = int(input('введите степень k: '))
    create_polynomial('polinom2.txt', k)

# Занятие 3
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной идексах.
#
# Пример:
#
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

array = list(randint(0, 100) for _ in range(10)) # <---
result = 0
for i in range(1, len(array), 2):
    result += i

print(result)
