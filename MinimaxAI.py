# Ari Chadda
# 9 October 2020
# Chess AI Assignment CS76 F20
import datetime
import sys
import random
import chess


class MinimaxAI():

    def __init__(self, depth, is_white):
        # class constructor
        self.depth = depth
        self.is_max_player = True
        self.next_move = None
        self.is_white = is_white
        self.visited_moves = {} # move options
        self.nodes_visited = 0 # number of times minimax was called

    def choose_move(self, board):

        self.minimax(board, self.depth) # call minimax for the first time
        minimum_score = None

        if self.next_move is None:
            # shuffle options to avoid repeat moves
            dummy_list = list(self.visited_moves.items())
            random.seed(int(datetime.datetime.utcnow().timestamp()))
            random.shuffle(dummy_list)
            self.visited_moves = dict(dummy_list)

            for key, value in self.visited_moves.items():
                # iterate through the options to find the one with the best score
                if minimum_score is None or value > minimum_score:
                    minimum_score = value
                    self.next_move = key

            print("Minimax AI recommending move " + str(self.next_move) + " set at a max depth of " + str(self.depth)
                  + " and has visited minimax " + str(self.nodes_visited) + " times")
            move = chess.Move.from_uci(str(self.next_move))
            # after assignment reset
            self.next_move = None
            self.visited_moves = {}
            self.is_max_player = True

            return move

    def minimax(self, board, max_depth):

        self.nodes_visited += 1 # visits counter

        if max_depth == 0: # if depth is reached just evaluate the board as score
            return self.heuristic_eval(board)
        elif self.is_max_player:
            max_score = sys.maxsize * -1 # max starts as very large negative number
            moves = list(board.legal_moves) # get the legal moves

            for move in moves:
                self.is_max_player = False # switch to min player after

                board.push(move) # add the move
                if self.cuttoff_test(board): # if the move causes a stalemate
                    if move is moves[-1] and not self.visited_moves: # if that's the only move add it with score 0
                        self.visited_moves[move] = 0
                    board.pop() # reset the board
                else:
                    current_score = self.heuristic_eval(board) # score the board
                    max_score = max(current_score, self.minimax(board, max_depth - 1)) # go a layer deeper
                    board.pop() # reset the board

                    if not self.is_white: # if black score should be reversed
                        self.visited_moves[move] = (current_score * -1)
                    else:
                        self.visited_moves[move] = current_score

            return max_score # return the max score for that node
        else:
            min_score = sys.maxsize # min player starts at very high number
            moves = list(board.legal_moves) # get options

            for move in moves:
                board.push(move) # add the option
                if self.cuttoff_test(board): # if the move causes a stalemate ignore it
                    board.pop()
                else:
                    current_score = self.heuristic_eval(board) # score the board
                    min_score = min(current_score, self.minimax(board, max_depth - 1)) # go a layer deeper
                    board.pop() # reset the board

            return min_score # return the min score

    def heuristic_eval(self, board):

        score_one = 0 # board score starts at 0
        for letter in range(0, 8):
            for number in range(0, 8):
                current_square = letter * 8 + number # iterate over all the squares on the board
                current_piece = board.piece_at(chess.SQUARES[current_square]) # get the current piece
                score_one = self.piece_score(current_piece, score_one) # add that piece to the board total
        return score_one

    def piece_score(self, piece, score_one): # material scoring from the book
        # inital score should evaluate to 0

        piece = str(piece) # string conversion to compare

        if piece == "P": # pawn worth 1
            score_one += 1
        if piece == "p":
            score_one -= 1
        if piece == "R": # rook worth 5
            score_one += 5
        if piece == "r":
            score_one -= 5
        if piece == "N": # knight worth 3
            score_one += 3
        if piece == "n":
            score_one -= 3
        if piece == "B": # bishop worth 3
            score_one += 3
        if piece == "b":
            score_one -= 3
        if piece == "Q": # queen worth 9
            score_one += 9
        if piece == "q":
            score_one -= 9
        if piece == "K": # king worth 100 - objective
            score_one += 100
        if piece == "k":
            score_one -= 100
        return score_one

    def cuttoff_test(self, board):
        # checks if stalemate conditions - game termination handled by function added to ChessGame.py
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






