## Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
## Пример: 0,56 -> 11

number = (input()).replace(',', '').replace('.', '')
result = 0

for num in number:
    result += int(num)

print(result)
