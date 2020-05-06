# This Python file uses the following encoding: utf-8
import time
import threading
from .View import View
from typing import Callable


class Game:
  def __init__(self):
    print("eqwq")
    self.scene_width = 500
    self.scene_height = 500
    self.unit_width = 50
    self.unit_height = 50

    self.view = View(self.scene_width, self.scene_height, self.unit_width, self.unit_height)
    self.view.show()
