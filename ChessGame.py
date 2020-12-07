# Ari Chadda
# 9 October 2020
# Chess AI Assignment CS76 F20
import chess


class ChessGame:
    def __init__(self, player1, player2):
        self.board = chess.Board()
        self.players = [player1, player2]

    def make_move(self):
        player = self.players[1 - int(self.board.turn)]
        move = player.choose_move(self.board)
        self.board.push(move)  # Make the move

    def is_game_over(self):
        return self.board.is_game_over()

    # added this terminal states handler to give better information at the end of a game as well as quit when a
    # terminal state was reached
    def exit_game(self):
        if self.board.is_game_over():
            if self.board.is_insufficient_material():
                print("Stalemate, neither side has the pieces to win the game")
                print(self.board.result())
            elif self.board.is_variant_draw():
                print("Stalemate, variant draw")
                print(self.board.result())
            elif self.board.is_stalemate():
                print("Stalemate, neither side can win the game")
                print(self.board.result())
            elif self.board.is_fivefold_repetition():
                print("Stalemate, Fivefold technicality")
                print(self.board.result())
            elif self.board.is_fifty_moves():
                print("Stalemate, Fifty moves rule")
                print(self.board.result())
            elif self.board.is_seventyfive_moves():
                print("Stalemate, Seventy-Five moves rule")
                print(self.board.result())
            elif self.board.is_checkmate():
                print("Checkmate")
                print(self.board.result())
            print(str(self.board))
            print(hash(str(self.board)))
            exit(0)

    def __str__(self):

        column_labels = "\n----------------\na b c d e f g h\n"
        board_str =  str(self.board) + column_labels

        # did you know python had a ternary conditional operator?
        move_str = "White to move" if self.board.turn else "Black to move"

        return board_str + "\n" + move_str + "\n"
