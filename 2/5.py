from random import randint
n = int(input())
array = list(i for i in range(n))
print(array)

for i in range(n):
    k = randint(0, n - 1)
    array[i], array[k] = array[k], array[i]

print(array)
