"""
Author: Richard Matthew Samonte Tan (rickytan-AA@github.com)
Version: 2021.04.23
License: MIT
"""

# ---------------------------------------------------------- Imports
# chess
import chess

# common & scientific libraries
import random

# ---------------------------------------------------------- Class Definition
class ChessEnv:
    """
    Creates an instance of a chessboard environment
    """
    def __init__(self):
        self.board = self.reset()

    # ------------------------------------------------------ Methods
    def reset(self):
        """
        Returns a new chessboard with the default piece layout.
        """
        return chess.Board()
        

# ---------------------------------------------------------- Main
if __name__ == '__main__':
    env = ChessEnv()
    print(env.board)

    env.board.push_san("e4")
    print("\n")
    print(env.board)
