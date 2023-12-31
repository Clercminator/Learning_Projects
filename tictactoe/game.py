class Tictactoe:
    def __init__(self):
        self.board = [' ' for _ in range{9}]#we'll use a single list to represent a 3x3 board
        self.current_winner = None #keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range {3}]
            print('| '+' | '.join(row)+' |')
    
    @staticmethod
    def print_board_nums():
        #it tells us what number correspond to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range (3)]
        for row in number_board:
            print('| '+' | '.join(row)+' |')

    def available_moves(self):
        return []