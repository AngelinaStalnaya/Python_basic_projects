from tic_tac_toe import *


def play_hard():
    print('Игра "Крестики-нолики."')
    my_board = Board()
    player_1 = Player(input('Введите имя игрока: '), 'X')
    player_2 = Player(input('Введите имя игрока: '), 'O')
    steps = 0
    winner = False

    while not winner:
        my_board.visual_board()
        if steps % 2 == 0:
            player_1.input_move(my_board)
        else:
            player_2.input_move(my_board)
        steps += 1
        if steps > 4:
            check_winner = my_board.check_winner()
            print(check_winner)
            if check_winner:
                print(f'\nВ данной игре победил: {player_1.name if check_winner == player_1.symbol else player_2.name}\n')
                winner = True
            elif steps > 8:
                print(f'\nУ игроков {player_1.name} и {player_2.name} ничья.\n')
                break

    my_board.print_board_info(player_1, player_2)


play_hard()