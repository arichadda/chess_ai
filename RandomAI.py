# Ari Chadda
# 9 October 2020
# Chess AI Assignment CS76 F20
import datetime
import random


class RandomAI():
    def __init__(self):
        pass

    def choose_move(self, board):

        moves = list(board.legal_moves)
        # changed the seed so it would randomize differently
        random.seed(int(datetime.datetime.utcnow().timestamp()) * 299)
        move = random.choice(moves)

        # added to help avoid the loops resulting in the 5 repeated states stalemate
        board.push(move)
        if self.cuttoff_test(board) and len(moves) > 1:
            board.pop()
            moves.remove(move)
            move = random.choice(moves)
        else:
            board.pop()

        print("Random AI recommending move " + str(move))
        return move

    def cuttoff_test(self, board):
        # checks if the game is entering a stalemate state that would end the game
        if board.is_stalemate():
            return True
        elif board.is_fivefold_repetition():
            return True
        elif board.is_fifty_moves():
            return True
        elif board.is_seventyfive_moves():
            return True
        elif board.is_insufficient_material():
            return True
        else:
            return False
