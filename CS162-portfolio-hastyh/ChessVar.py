# Name: Hamilton Hasty
# GitHub username: hastyh
# Date: 6/9/2024
# Description: A class representing a game of chess following the rules for atomic chess

class ChessVar:
    """a class representing a game of chess following the rules for atomic chess"""

    def __init__(self):
        """
        initializes data members holding the game board
        (with lower case pieces being black and upper case being white),
         the turn and the state of the game
        """
        self._board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
        ]
        self._turn = 'white'
        self._game_state = 'UNFINISHED'

    def get_game_state(self):
        """returns game state"""
        return self._game_state

    def make_move(self, from_pos, to_pos):
        """function to move pieces"""
        # returns invalid move if game state is finished
        if self._game_state != 'UNFINISHED':
            return False

        from_row, from_col = 8 - int(from_pos[1]), ord(from_pos[0]) - ord('a')
        to_row, to_col = 8 - int(to_pos[1]), ord(to_pos[0]) - ord('a')
        piece = self._board[from_row][from_col]
        target = self._board[to_row][to_col]

        # returns invalid move if try to move an
        # empty space, or it is white's turn and
        # try to move a black piece and vice versa
        if piece == ' ' or (self._turn == 'white' and piece.islower()) or (self._turn == 'black' and piece.isupper()):
            return False

        # checks if move is valid using func valid_move
        if not self.valid_move(piece, from_row, from_col, to_row, to_col):
            return False

        # sets empty square from where piece leaves and
        # calls explode func or sets piece in new square
        # depending on if it is empty or not
        self._board[from_row][from_col] = ' '
        if target != ' ':
            self.explosion(to_row, to_col)
        else:
            self._board[to_row][to_col] = piece

        # if a piece hits a king, game state changes to reflect who wins
        if target.lower() == 'k':
            if self._turn == 'white':
                self._game_state = 'WHITE_WON'
            else:
                self._game_state = 'BLACK_WON'

        # switches turn
        if self._turn == 'white':
            self._turn = 'black'
        else:
            self._turn = 'white'

        # returns true if valid move
        return True

    def valid_move(self, piece, from_row, from_col, to_row, to_col):
        """function to determine if move is valid chess move and utilizes helper function"""
        # returns false if king tries to take a piece as move is not allowed in atomic chess
        if piece.lower() == 'k' and self._board[to_row][to_col] != ' ':
            return False
        return self.chess_moves(piece, from_row, from_col, to_row, to_col)

    def chess_moves(self, piece, from_row, from_col, to_row, to_col):
        """function that keeps a list of valid chess moves"""
        # pawn
        if piece.lower() == 'p':
            if piece.isupper():
                move = -1
            else:
                move = 1
            if from_col == to_col:
                if self._board[to_row][to_col] != ' ':
                    return False
                if from_row + move == to_row:
                    return True
                if (
                        (from_row == 1 and move == 1 or from_row == 6 and move == -1)
                        and from_row + 2 * move == to_row and
                        self._board[from_row + move][from_col] == ' '):
                    return True
            elif (abs(from_col - to_col) == 1 and
                  from_row + move == to_row and
                  self._board[to_row][to_col] != ' '):
                return True
            return False

        # rook
        if piece.lower() == 'r':
            if from_row != to_row and from_col != to_col:
                return False
            return self.path(from_row, from_col, to_row, to_col)

        # knight
        if piece.lower() == 'n':
            return (abs(from_row - to_row) == 2 and abs(from_col - to_col) == 1 or
                    abs(from_row - to_row) == 1 and abs(from_col - to_col) == 2)

        # bishop
        if piece.lower() == 'b':
            if abs(from_row - to_row) != abs(from_col - to_col):
                return False
            return self.path(from_row, from_col, to_row, to_col)

        # queen
        if piece.lower() == 'q':
            if abs(from_row - to_row) == abs(from_col - to_col) or from_row == to_row or from_col == to_col:
                return self.path(from_row, from_col, to_row, to_col)

        # king
        if piece.lower() == 'k':
            return abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1

        return False

    def path(self, from_row, from_col, to_row, to_col):
        """function to determine if a move has a clear path or not"""
        step_row = (to_row - from_row) // max(1, abs(to_row - from_row))
        step_col = (to_col - from_col) // max(1, abs(to_col - from_col))
        current_row, current_col = from_row + step_row, from_col + step_col
        while current_row != to_row or current_col != to_col:
            if self._board[current_row][current_col] != ' ':
                return False
            current_row += step_row
            current_col += step_col
        return True

    def explosion(self, row, col):
        """
        Explodes pieces immediately surrounding the 8 tiles around a captured piece except for pawns.
        If one of those pieces is a king the game state changes to reflect the winner
        """
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < 8 and 0 <= j < 8 and (i != row or j != col) and self._board[i][j] != ' ':
                    if self._board[i][j].lower() != 'p':
                        if self._board[i][j].lower() == 'k':
                            if self._board[i][j].islower():
                                self._game_state = 'WHITE_WON'
                            else:
                                self._game_state = 'BLACK_WON'
                        self._board[i][j] = ' '
        self._board[row][col] = ' '

    def print_board(self):
        """prints out game board and the x and y coordinates of the board"""
        print('  a b c d e f g h')
        for i in range(8):
            print(8 - i, end=' ')
            for j in range(8):
                print(self._board[i][j], end=' ')
            print(8 - i)
        print('  a b c d e f g h')

    def get_turn(self):
        """returns current turn"""
        return self._turn
