import numpy as np

ROWS = 6
COLUMNS = 7
EMPTY = 0
PLAYER_MAX = 1
PLAYER_MIN = -1

class ConnectFour:
    """
    Manages the game state, moves, transitions, and terminal checks.
    """
    def __init__(self):
        self.board = self.create_board()
        self.current_player = PLAYER_MAX
        self.move_count = 0

    def create_board(self):
        """Initial State: Returns a 6x7 board initialized to 0 (EMPTY)."""
        return np.zeros((ROWS, COLUMNS), dtype=int)

    def get_valid_moves(self, board=None):
        """Actions / Moves: Returns a list of column indices that are not full."""
        if board is None:
            board = self.board
        moves = []
        for col in range(COLUMNS):
            if board[0][col] == EMPTY:
                moves.append(col)
        return moves

    def drop_piece(self, board, row, col, piece):
        """Transition Function Helper: Places a piece on the board."""
        new_board = board.copy()
        new_board[row][col] = piece
        return new_board

    def get_next_open_row(self, board, col):
        """Finds the lowest available row in a given column."""
        for r in range(ROWS - 1, -1, -1):
            if board[r][col] == EMPTY:
                return r
        return

    def transition_state(self, board, col, piece):
        """Transition Function: Applies a move and returns the new board state."""
        row = self.get_next_open_row(board, col)
        if row != -1:
            return self.drop_piece(board, row, col, piece), row
        return None, -1

    def is_terminal_state(self, board):
        """Terminal States: Checks for win/loss/draw conditions."""
        return self.check_win(board, PLAYER_MAX) or \
               self.check_win(board, PLAYER_MIN) or \
               len(self.get_valid_moves(board)) == 0

    def check_win(self, board, piece):
        """Defines win/loss conditions by checking 4-in-a-row."""
        for c in range(COLUMNS - 3):
            for r in range(ROWS):
                if all(board[r][c+i] == piece for i in range(4)):
                    return True

        for c in range(COLUMNS):
            for r in range(ROWS - 3):
                if all(board[r+i][c] == piece for i in range(4)):
                    return True

        for c in range(COLUMNS - 3):
            for r in range(ROWS - 3):
                if all(board[r+i][c+i] == piece for i in range(4)):
                    return True

        for c in range(COLUMNS - 3):
            for r in range(3, ROWS):
                if all(board[r-i][c+i] == piece for i in range(4)):
                    return True
        return False

    # --------------------------------------------------------------------------
    # HEURISTIC EVALUATION FUNCTION
    # --------------------------------------------------------------------------

    def evaluate_window(self, window, piece):
        """Scores a 4-cell window (row, col, or diag) for potential threats."""
        score = 0
        opp_piece = -piece

        piece_count = np.count_nonzero(window == piece)
        empty_count = np.count_nonzero(window == EMPTY)
        opp_count = np.count_nonzero(window == opp_piece)

        if piece_count == 4:
            return 1000000 
        elif piece_count == 3 and empty_count == 1:
            score += 5000 
        elif piece_count == 2 and empty_count == 2:
            score += 10
        
        if opp_count == 3 and empty_count == 1:
            score -= 4000 
        elif opp_count == 2 and empty_count == 2:
            score -= 9

        return score

    def score_position(self, board, piece):
        """Scores the entire board by checking all 4-cell windows."""
        score = 0

        center_array = board[:, COLUMNS // 2]
        center_count = np.count_nonzero(center_array == piece)
        score += center_count * 10

        for r in range(ROWS):
            row_array = board[r, :]
            for c in range(COLUMNS - 3):
                window = row_array[c:c + 4]
                score += self.evaluate_window(window, piece)

        for c in range(COLUMNS):
            col_array = board[:, c]
            for r in range(ROWS - 3):
                window = col_array[r:r + 4]
                score += self.evaluate_window(window, piece)

        for r in range(ROWS - 3):
            for c in range(COLUMNS - 3):
                window = [board[r + i][c + i] for i in range(4)]
                score += self.evaluate_window(window, piece)

        for r in range(3, ROWS):
            for c in range(COLUMNS - 3):
                window = [board[r - i][c + i] for i in range(4)]
                score += self.evaluate_window(window, piece)

        return score