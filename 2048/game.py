import random
import numpy as np

UP, RIGHT, DOWN, LEFT = range(4)
action_name = ["UP", "RIGHT", "DOWN", "LEFT"]

class IllegalAction(Exception):
    pass

class GameOver(Exception):
    pass

class Board:
    def __init__(self, board=None):
        self.board = np.zeros((16), dtype=int) if board is None else np.array(board, dtype=int)
        self.spawn_tile()   

    def spawn_tile(self):
        empty = [i for i in range(16) if self.board[i] == 0]
        if not empty:
            return
        i = random.choice(empty)
        self.board[i] = 2 if random.random() < 0.9 else 4

    def copyboard(self):
        return np.copy(self.board).reshape((16))

    def rotate_board(self, times):
        return np.rot90(self.board, -times)

    def act(self, action):
        rotated = np.rot90(self.board.reshape(4, 4), -action)
        moved, score = self._move_left(rotated)
        if moved is None:
            raise IllegalAction()
        
        self.board = np.rot90(moved, action).flatten()
        return score

    def _move_left(self, board):
        """
        TODO: Implement move logic to slide and merge tiles left.
        Return (new_board, score) if move is valid,
        or (None, None) if no tiles moved or merged.
        """
        score = 0
        new_board = np.zeros_like(board)
        moved = False

        # TODO: Fill in the logic to move and merge tiles to the left
        # Hint: iterate over rows, track last merged tile, update score, and set moved=True if any tile moves or merges

        # Example placeholder (remove this when implementing):
        # return None, None  # Uncomment to simulate illegal move for testing

        # After implementing, return new_board and score if moved, else None, None
        if not moved:
            return None, None

        return new_board, score
                    
    def is_game_over(self):
        """
        TODO: Implement game over check.
        Return True if no moves are possible and no empty tiles remain.
        Return False otherwise.
        """
        # Check for empty tiles
        if 0 in self.board:
            return False

        # Check if any move is possible in any direction
        # Hint: try all actions, if any act() does not raise IllegalAction, return False

        # Placeholder return True to simulate game over (remove when implementing)
        return True