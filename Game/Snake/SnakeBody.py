# This Python file uses the following encoding: utf-8
from PySide2.QtWidgets import QGraphicsRectItem


class SnakeBody(QGraphicsRectItem):
  def __init__(self, width: int, height: int):
    super().__init__()
    self.width = width
    self.height = height
    self.setRect(0, 0, width, height)

  def move(self):
    self.moveBy(0, self.width)
