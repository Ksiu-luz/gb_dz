# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from collections import deque
k = int(input('Задайте число k: '))
fib = deque([0, 1])

for i in range(k - 1):
    fib.append(fib[i] + fib[i + 1])

for i in range(k):
    fib.appendleft((abs(fib[0]) + abs(fib[1])) * (-1) ** i)

print(list(fib))
