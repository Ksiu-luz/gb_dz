# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# ну, если прям по простому, то:


def decimal_to_binary(num):
    return bin(num)[2:]


number = int(input('Введите число: '))
print(decimal_to_binary(number))

# а если создавать велосипед, то:


def decimal_to_binary2(num):
    res = []
    while num != 0:
        res.append(str(num % 2))
        num //= 2
    res = reversed(res)
    return ''.join(res)


print(decimal_to_binary2(number))
