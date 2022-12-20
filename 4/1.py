"""
Вычислить число c заданной точностью d

Пример:

- при d = 0.001, π = 3.141
Ввод: 0.01
    Вывод: 3.14

    Ввод: 0.001
    Вывод: 3.141
"""

from math import pi, floor


def get_pi(x):
    accuracy = x.split('.')
    if len(accuracy) < 2:
        return int(pi)
    mult = int('1' + "0" * len(accuracy[1]))
    return floor(pi * mult) / mult


if __name__ == "__main__":
    d = input('Введите количество знаков после запятой: ')
    print(get_pi(d))
