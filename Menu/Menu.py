# This Python file uses the following encoding: utf-8
from PySide2.QtWidgets import QWidget
from .ui_menu import Ui_Menu
from Game import Game


class Menu(QWidget):
  def __init__(self):
    super(Menu, self).__init__()
    self.ui = Ui_Menu()
    self.ui.setupUi(self)
    self.ui.startButton.clicked.connect(self.start_game)

  def start_game(self):
    self.game = Game()
    self.close()
