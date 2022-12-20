"""
Создайте программу для игры в ""Крестики-нолики"".
"""

from random import randint


def print_desk(desk):
    print('   1    2    3')
    for i in range(len(desk)):
        print(i + 1, desk[i])


def step(player, desk, symb):
    print(f'ходит {player}')
    stop = 0
    while not stop:
        row, column = map(int, input('введите координаты через пробел: ').split())
        if desk[row - 1][column - 1] is None:
            desk[row - 1][column - 1] = symb
            stop = 1
        else:
            print('эта ячейка уже занята')
    print_desk(desk)


def is_win(desk):
    for i in range(3):
        if desk[0][i] == desk[1][i] == desk[2][i] and desk[0][i] is not None:
            return True
        if desk[i][0] == desk[i][1] == desk[i][2] and desk[i][0] is not None:
            return True
    if (desk[0][0] == desk[1][1] == desk[2][2] or desk[0][2] == desk[1][1] == desk[2][0]) and desk[1][1] is not None:
        return True
    return False


desk = [[None, None, None],
        [None, None, None],
        [None, None, None]]

player1 = input('Имя первого игрока: ')
player2 = input('Имя второго игрока: ')

print_desk(desk)
flag = randint(0, 1)
win = False
while not win:
    if flag:
        step(player1, desk, 'X')
        flag = False
    else:
        step(player2, desk, 'O')
        flag = True
    win = is_win(desk)

if flag:
    print(f'Выиграл {player2}')
else:
    print(f'Выиграл{player1}')
