import numpy as np


def empty_field():
    return [['.' for _ in range(3)] for _ in range(3)]


# func for print the game field
def print_field(field):
    print(f'{"Игровое поле":^17}')
    print(f'{"Столбец":10}  0 1 2 ')
    for y in range(3):
        print(f'{"Строка " + str(y) + " |":10} ', ' '.join(field[y]))


# func check win or not
def check_win(field, player):
    win_combination = [
        'XXX......',
        '...XXX...',
        '......XXX',
        'X..X..X..',
        '.X..X..X.',
        '..X..X..X',
        'X...X...X',
        '..X.X.X..'
    ]
    check_str = ''.join(np.array(field).flatten())
    check_str = check_str.replace('0', '.') if player == 'X' else check_str.replace('X', '.').replace('0', 'X')
    return True if check_str in win_combination else False


# func for entering of player
def player_step(player, field):
    print('\nЕсли вы хотите начать новую игру введите NEW и нажмите ввод.')
    print('Если вы хотите выйти из игры введите END и нажмите ввод.')
    print("Введите координаты поля через пробел (пример '1 2') и нажмите ввод.\n")
    player_input = input(f'Игрок ({player}) введите координаты или комманду:')
    if player_input.upper() == 'NEW':
        return False, True, player
    elif player_input.upper() == 'END':
        return True, True, player
    else:
        # TODO: добить проверку на правильность ввода
        x, y = map(int, player_input.split())
        field[y][x] = player
        win = check_win(field, player)
        if win:
            input(f'УРРРА!!!! Игрок {player} ПОБЕДИЛ! Нажимите Enter для начала новой игры')
            return False, True, player
        player = '0' if player == 'X' else 'X'
    return False, False, player


# func starting game
def start_game():
    exit_game = False
    while not exit_game:
        new_game = False
        player = 'X'
        game_field = empty_field()
        while not new_game:
            print_field(game_field)
            exit_game, new_game, player = player_step(player, game_field)


if __name__ == '__main__':
    print('Добро пожаловать в игру крестики-нолики.')
    input('Для начала нажмите Enter:')
    start_game()
