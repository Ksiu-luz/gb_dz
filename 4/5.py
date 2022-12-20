"""
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).
Пример того, что будет в итогвом файле: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0
"""


def parser(polinom):
    result = polinom.split('+ ')
    for m in range(len(result) - 1):
        result[m] = result[m].split('*')[0]
    result[-1] = result[-1].split()[0]
    return result


def create_sum_polynomial(file_name, odds_list, k):
    odds = odds_list.copy()
    odds.reverse()
    with open(file_name, 'w') as file:
        for j in range(k, 1, -1):
            file.write(f'{odds.pop()}*(x**{j}) + ')
        file.write(f'{odds.pop()}*x + {odds.pop()} = 0')


with open('polinom1.txt', 'r') as f:
    p1 = f.readline()

with open('polinom2.txt', 'r') as f:
    p2 = f.readline()

p1 = parser(p1)
p2 = parser(p2)

if len(p1) < len(p2):
    p1, p2 = p2, p1

sum_odds = []
diff = len(p1) - len(p2)

for i in range(diff):
    sum_odds.append(p1[i])

for i in range(diff, len(p1)):
    sum_odds.append(str(int(p1[i]) + int(p2[i - diff])))

create_sum_polynomial('sum_polinom.txt', sum_odds, len(sum_odds) - 1)
