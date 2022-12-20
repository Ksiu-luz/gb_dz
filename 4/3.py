"""
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
    elems_list = list(map(int, input('введите последовательность чисел через пробел: ').split()))
    print(unique_elems(elems_list))
