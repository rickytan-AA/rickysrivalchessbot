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
    Creates an instance of a chessboard environment.
    """
    def __init__(self):
        self.board = None # initialized by reset()

    # ------------------------------------------------------ RL Methods
    def reset(self):
        """
        Returns a new chessboard with the default piece layout.
        """
        self.board = chess.Board()

        # return board state and done status
        return self.board, self.board.outcome() is not None


    def step(self,a):
        """
        Moves a piece on the board according to action a.
        """
        a = self.board.parse_san(a) # SAN move representation
        if a not in self.board.legal_moves: # check if illegal
            print("%s is an illegal move!"%a)
            return
        env.board.push(a) # perform if legal

        # return board state and done status
        return self.board, self.board.outcome() is not None


    # ------------------------------------------------------ RL Methods
    def step_seq(self,seq):
        """
        Plays a predetermined sequence of actions from a list.
        """
        # start board
        current_board, done = self.reset()
        print("---------------- \n")
        print(current_board, "\n Done? %s"%done)

        # begin sequence
        for i,a in enumerate(seq):
            current_board, done = self.step(a)
            print("---------------- \n")
            print(current_board, "\n Done? %s"%done)

            if done:
                print("Sequence ended in checkmate at move %s in index %s"%(a,i))
                print(current_board.outcome())
                return current_board, done
                
        print("Sequence finished.")
        return current_board, done


# ---------------------------------------------------------- Main
if __name__ == '__main__':
    env = ChessEnv()

    # scholar's mate
    seq = ["e4", "e5", "Qh5", "Nc6", "Bc4", "Nf6", "Qxf7"]
    current_board,done = env.step_seq(seq)
    


