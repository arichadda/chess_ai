# Ari Chadda
# 9 October 2020
# Chess AI Assignment CS76 F20
from IterativeDeepeningMinimaxAI import IterativeDeepeningMinimaxAI
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame

if __name__ == "__main__":

    # To play, uncomment one player one and one player two of the algorithm of your choice. For the depth based
    # algorithms, you can also change the depth. The True or False corresponds to if the player is white or black
    # with a "True" corresponding to white (player1)

    # player1 = HumanPlayer()
    # player2 = HumanPlayer()
    # player1 = RandomAI()
    # player2 = RandomAI()
    # player1 = MinimaxAI(2, True)
    player2 = MinimaxAI(2, False)
    player1 = AlphaBetaAI(2, True)
    # player2 = AlphaBetaAI(2, False)
    # player1 = IterativeDeepeningMinimaxAI(3, True)
    # player2 = IterativeDeepeningMinimaxAI(2, False)

    game = ChessGame(player1, player2)

    while not game.is_game_over():
        print("GAME")
        print(game)
        game.make_move()

    game.exit_game()



