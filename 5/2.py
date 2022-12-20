"""
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
"""

from random import randint


def input_candy_count(name):
    x = int(input(f"{name}, сколько конфет (от 1 до 28) вы возьмете? "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, вы можете взять только от 1 до 28 конфет: "))
    return x


def print_step(name, count, all_players_candy, count_candy_on_table):
    print(f"{name} взял {count} конфет, всего конфет {all_players_candy}. На столе {count_candy_on_table} конфет.")


def bot_calc(value):
    if value <= 28:
        return value
    take_candy = randint(1, 28)
    if 30 <= value <= 57:
        return value - 29
    return randint(1, 28)


def play_step(player, candy_count, value):
    if player == 'Bot':
        take_candy = randint(1, 28)
    elif player == 'Smart Bot':
        take_candy = bot_calc(value)
    else:
        take_candy = input_candy_count(player)
    if take_candy > value:
        print('На столе не так много конфет, заберите оставшиеся.')
        take_candy = value
    candy_count += take_candy
    value -= take_candy
    return candy_count, value, take_candy


who_play_with = int(input('Вы будете играть с другом(1) или с ботом(0)? Введите число: '))
player1 = input("Имя первого игрока: ")
if who_play_with:
    player2 = input("Имя второго игрока: ")
else:
    smart_flag = int(input('Наделим бота разумом? Да(1)/Нет(0): '))
    if smart_flag:
        player2 = 'Smart Bot'
    else:
        player2 = 'Bot'
    print(f'С вами сыграет {player2}')

value = 2021
flag = randint(0, 1)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

candy_count_1 = 0
candy_count_2 = 0

while value > 0:
    if flag:
        candy_count_1, value, take_candy = play_step(player1, candy_count_1, value)
        flag = False
        print_step(player1, take_candy, candy_count_1, value)
    else:
        candy_count_2, value, take_candy = play_step(player2, candy_count_2, value)
        flag = True
        print_step(player2, take_candy, candy_count_2, value)

if flag:
    print(f"Выиграл {player2}")
else:
    print(f"Выиграл {player1}")
