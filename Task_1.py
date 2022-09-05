# Task_3

table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in table:
    print (' | '.join(list(map(str, row))))
    print('_'*10)


def vvod(player):

    player1 = int(input('Куда поставить '+player+'?'))
    if player1 == 1:
        table[player1-1][player1-1] = player
    elif player1 == 2:
        table[player1-2][player1-1] = player
    elif player1 == 3:
        table[player1-3][player1-1] = player
    elif player1 == 4:
        table[player1-3][player1-4] = player
    elif player1 == 5:
        table[player1-4][player1-4] = player
    elif player1 == 6:
        table[player1-5][player1-4] = player
    elif player1 == 7:
        table[player1-5][player1-7] = player
    elif player1 == 8:
        table[player1-6][player1-7] = player
    elif player1 == 9:
        table[player1-7][player1-7] = player
    else:
        print('Введите корректное число, чтобы сделать ход')

    for row in table:
        print (' | '.join(list(map(str, row))))
        print('_'*10)


counter = 0
win = False
while not win:
    vvod('X') if counter % 2 == 0 else vvod('O')
    counter += 1
    if counter > 4:
        if table[0][0]==table[0][1]==table[0][2] or \
            table[1][0]==table[1][1]==table[1][2] or \
            table[2][0]==table[2][1]==table[2][2] or \
            table[0][0]==table[1][0]==table[2][0] or \
            table[0][1]==table[1][1]==table[2][1] or \
            table[0][2]==table[1][2]==table[2][2] or \
            table[0][0]==table[1][1]==table[2][2] or \
            table[0][2]==table[1][1]==table[2][0]:
            win == True
            print('Вы выиграли')
            break
    if counter == 9:
        print('Ничья')
        break

