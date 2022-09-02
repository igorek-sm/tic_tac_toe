def helloGamers():
    print('======================')
    print('   Приветствуем вас   ')
    print('        в игре        ')
    print('   КРЕСТИКИ-НОЛИКИ!   ')
    print('======================')
    print('     Формат ввода     ')
    print('      координат:      ')
    print(' два числа от 0 до 2, ')
    print(' разделённые пробелом ')
    print(' (№ строки № столбца).')
    print()


def showGameBoard(field):
    print('| # | 0 | 1 | 2 |')

    for line in range(len(field)):
        print('-----------------')
        print('|', line, '|', ' | '.join(field[line]), '|')

    print()


def nextTurn():
    while True:
        coords_list = input('Введите координаты: ').split()

        if len(coords_list) != 2:
            print('Введите ДВЕ координаты!')
            continue

        x, y = coords_list

        if not x.isdigit() or not y.isdigit():
            print('Введите числа!')
            continue

        x, y = int(x), int(y)

        if not (0 <= x <= 2) or not (0 <= y <= 2):
            print('Введите координаты в диапазоне от 0 до 2!')
            continue

        if field[x][y] != ' ':
            print('Клетка занята!')
            continue

        break

    return x, y


def checkWinner():
    win_cells = (((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)),
                 ((0, 2), (1, 2), (2, 2)),
                 ((0, 0), (0, 1), (0, 2)),
                 ((1, 0), (1, 1), (1, 2)),
                 ((2, 0), (2, 1), (2, 2)),
                 ((0, 0), (1, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)))
    for three_cells in win_cells:
        sym_list = []
        for sym in three_cells:
            sym_list.append(field[sym[0]][sym[1]])
        if sym_list == ['X', 'X', 'X']:
            print('Выиграл крестик!')
            showGameBoard(field)
            return True
        if sym_list == ['O', 'O', 'O']:
            print('Выиграл нолик!')
            showGameBoard(field)
            return True
    return False


def continueGame():
    answer = input('Сыграете ещё раз? (y/n)')
    if answer == 'y':
        continue_game = True
    elif answer == 'n':
        continue_game = False
        print('Тогда до встречи!')

    return continue_game

count = 0
field = [[' '] * 3 for _ in range(3)]
helloGamers()
continue_game = True

while continue_game:
    showGameBoard(field)
    count += 1

    if count % 2 == 1:
        print('Ход крестика...')
    else:
        print('Ход нолика...')

    x, y = nextTurn()

    if count % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'

    if checkWinner():
        continue_game = continueGame()
        if continue_game:
            field = [[' '] * 3 for _ in range(3)]
            count = 0
        else:
            break

    if count == 9:
        print('Ничья!')
        showGameBoard(field)
        continue_game = continueGame()
        if continue_game:
            field = [[' '] * 3 for _ in range(3)]
            count = 0
        else:
            break
