"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""


def prime_mult(n):

    def is_simple(x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    result = []
    simple_mult = 2

    while n != 1:
        if n % simple_mult == 0:
            result.append(simple_mult)
            n //= simple_mult
        else:
            simple_mult += 1
            while not is_simple(simple_mult):
                simple_mult += 1
    return result


if __name__ == "__main__":
    numb = int(input('введите N: '))
    print(*prime_mult(numb))
