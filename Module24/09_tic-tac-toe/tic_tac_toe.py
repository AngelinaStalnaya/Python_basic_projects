
class Cell:

    def __init__(self, index):
        self.status = False
        self.index = index
        self.cell_symbol = index + 1

    def print_cell_info(self):
        print(f'Клетка {self.index + 1} {"свободна" if self.status == False else "занята"}')
        return self.status


class Board:

    def __init__(self):

        self.board = [Cell(index) for index in range(0, 9)]

    def visual_board(self):
        print('-' * 13)
        for i in range(3):
            print('|', self.board[0 + i * 3].cell_symbol,
                  '|', self.board[1 + i * 3].cell_symbol,
                  '|', self.board[2 + i * 3].cell_symbol, '|')
            print('-' * 13)

    def check_cell(self, index):
        return self.board[index].print_cell_info()

    def change_cell(self, index, players_symbol):
        self.board[index].status = True
        self.board[index].cell_symbol = players_symbol

    def check_winner(self):
        right_moves = ((0, 1, 2),
                       (3, 4, 5),
                       (6, 7, 8),
                       (0, 3, 6),
                       (1, 4, 7),
                       (2, 5, 8),
                       (0, 4, 8),
                       (2, 4, 6))

        for i_tuple in right_moves:
            if self.board[i_tuple[0]].cell_symbol == self.board[i_tuple[1]].cell_symbol == self.board[i_tuple[2]].cell_symbol:
                return self.board[i_tuple[0]].cell_symbol

    def print_board_info(self, player_1, player_2):
        player_1.print_info()
        player_2.print_info()
        self.visual_board()


class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.moves = []

    def input_move(self, board):

        answer = int(input(f'{self.name}, куда хотите поставить "{self.symbol}"? '))
        if 1 <= answer <= 9:
            if not board.check_cell(answer - 1):
                board.change_cell(answer - 1, self.symbol)
                print(f'Игрок {self.name} занял клетку {answer}')
                self.moves.append(answer)
            else:
                print('Неверный выбор, Вы пропустили свой ход.')
        else:
            print('Ошибка выбора клетки.')

    def print_info(self):
        print(f'Имя игрока: {self.name}\n'
              f'Символ игрока: "{self.symbol}"\n'
              f'Ходы игрока: {self.moves}\n')
