# Ari Chadda
# 9 October 2020
# Chess AI Assignment CS76 F20
from PyQt5 import QtGui, QtSvg
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QWidget
import sys
import chess, chess.svg

from IterativeDeepeningMinimaxAI import IterativeDeepeningMinimaxAI
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame

import random


class ChessGui:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.game = ChessGame(player1, player2)

        self.app = QApplication(sys.argv)
        self.svgWidget = QtSvg.QSvgWidget()
        self.svgWidget.setGeometry(50, 50, 400, 400)
        self.svgWidget.show()


    def start(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.make_move)
        self.timer.start(10)

        self.display_board()

    def display_board(self):
        svgboard = chess.svg.board(self.game.board)

        svgbytes = QByteArray()
        svgbytes.append(svgboard)
        self.svgWidget.load(svgbytes)


    def make_move(self):

        print("making move, white turn " + str(self.game.board.turn))

        if not self.game.exit_game():
            self.game.make_move()
            self.display_board()

if __name__ == "__main__":

    random.seed(1)

    # The gui cannot handle human players

    # To play, uncomment one player one and one player two of the algorithm of your choice. For the depth based
    # algorithms, you can also change the depth. The True or False corresponds to if the player is white or black
    # with a "True" corresponding to white (player1)

    # player1 = RandomAI()
    player2 = RandomAI()
    # player1 = MinimaxAI(2, True)
    # player2 = MinimaxAI(2, False)
    player1 = AlphaBetaAI(2, True)
    # player2 = AlphaBetaAI(2, False)
    # player1 = IterativeDeepeningMinimaxAI(3, True)
    # player2 = IterativeDeepeningMinimaxAI(2, False)

    game = ChessGame(player1, player2)
    gui = ChessGui(player1, player2)
    gui.start()
    sys.exit(gui.app.exec_())
