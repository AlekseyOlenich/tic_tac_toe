import numpy as np


# Создаем пустое поле
def empty_field():
    return [['.' for _ in range(3)] for _ in range(3)]


# Отрисовываем поле
def print_field(field):
    print(f'{"Игровое поле":^17}')
    print(f'{"Столбец":10}  0 1 2 ')
    for y in range(3):
        print(f'{"Строка " + str(y) + " |":10} ', ' '.join(field[y]))


# Проверяем выиграл ли человек после устновки символа
def check_win(field, player):
    # создаем массив всех выигрышных кобинаций
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
    # разворачиваем двухмерный массив в одну строку для последующей провеки по выигрышным комбинациям
    check_str = ''.join(np.array(field).flatten())
    # если ходил игрок Х то сбрасываем все 0 в ., иначе все Х в точку, а нули в Х
    # нужно чтобы не рисовать два варианта выигрышных полей и не обращать внимание на ходы противника
    check_str = check_str.replace('0', '.') if player == 'X' else check_str.replace('X', '.').replace('0', 'X')
    # если комбинация находится в выигрышных, то возвращаем результат
    return True if check_str in win_combination else False


def check_player_input(player, field):
    player_input = input(f'Игрок ({player}) введите координаты или комманду:').upper().strip()
    check = False
    if player_input in ['END', 'NEW']:
        return True, player_input
    else:
        coordinate = player_input.split()
        if len(coordinate) != 2:
            print('Вы ввели больше или меньше чем 2-е координаты.')
            return False, ''
        elif not coordinate[0].isdigit() or not coordinate[1].isdigit():
            print('Вы ввели не цифровые значения координат.')
            return False, ''
        else:
            x, y = map(int, coordinate)
            if x < 0 or x > 2 or y < 0 or y > 2:
                print('Вы ввели координаты за границей поля.')
                return False, ''
            if field[y][x] != '.':
                print('Вы ввели координаты уже заполненного поля.')
                return False, ''
        return True, player_input


# обработчик ходов игрока
def player_step(player, field):
    # выводим доступные варианты для ввода игроком
    print('\nЕсли вы хотите начать новую игру введите NEW и нажмите ввод.')
    print('Если вы хотите выйти из игры введите END и нажмите ввод.')
    print("Введите координаты поля через пробел (пример '1 2') и нажмите ввод.\n")
    # установили переменную для начала цикла и начали цикл ввода значений, сделано, чтобы не уходить в рекурсию
    check_input = False
    while not check_input:
        check_input, player_input = check_player_input(player, field)
    # если игрок выбрал игру по новой, то формируем соответствующий ответ
    if player_input == 'NEW':
        return False, True, player
    # если игрок выбрал завершение игры, то формируем соответствующий ответ
    elif player_input == 'END':
        return True, True, player
    # иначе обрабатываем то, что ввел игрок и проверяем выигрыш
    else:
        x, y = map(int, player_input.split())
        field[y][x] = player
        # проверили и вернули информацию о выигрыше и вернули флаг начала новой игры в основной цикл работы игры
        win = check_win(field, player)
        if win:
            print_field(field)
            input(f'УРРРА!!!! Игрок {player} ПОБЕДИЛ! Нажимите Enter для начала новой игры')
            return False, True, player
        # сменили игрока
        player = '0' if player == 'X' else 'X'
    # вернули информацию о том, что ход состоялся и нового следующего игрока
    return False, False, player


# основной цикл работы игры
def start_game():
    exit_game = False
    # начали цикл пока клиент не ввел информацию о завершении игр
    while not exit_game:
        new_game = False
        # первый ходит игрок, который ставит Х
        player = 'X'
        # очистили поле перед началом игры
        game_field = empty_field()
        while not new_game:
            # отрисовали текущее состояние поля
            print_field(game_field)
            # вызвали функцию обработки ввода игрока
            exit_game, new_game, player = player_step(player, game_field)


if __name__ == '__main__':
    print('Добро пожаловать в игру крестики-нолики.')
    input('Для начала нажмите Enter:')
    start_game()
