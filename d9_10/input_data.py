def input_data(player_token, tab):
    valid = False
    while not valid:
        player_answer = input(f"Куда поставим {player_token}? ")
        if player_answer.isdigit():
            player_answer = int(player_answer)
        else:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 9 >= player_answer >= 1:
            if str(tab[player_answer - 1]) not in "XO":
                tab[player_answer-1] = player_token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")
