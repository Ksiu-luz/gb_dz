# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

from random import randint

n = int(input())
array = list(randint(-n, n) for _ in range(n))
result = 1
indices = list(map(int, input().split()))

for i in range(len(indices)):
    result *= array[indices[i]]

print(result)
