"""
Задана натуральная степень k.
Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
- k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
"""
from random import randint


def create_polynomial(file_name, k):
    odds = list(randint(0, 100) for _ in range(k + 1))
    with open(file_name, 'w') as f:
        for i in range(k, 1, -1):
            f.write(f'{odds.pop()}*(x**{i}) + ')
        f.write(f'{odds.pop()}*x + {odds.pop()} = 0')


if __name__ == "__main__":
    k = int(input('введите степень k: '))
    create_polynomial('polinom1.txt', k)
    k = int(input('введите степень k: '))
    create_polynomial('polinom2.txt', k)
