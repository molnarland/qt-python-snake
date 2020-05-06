# This Python file uses the following encoding: utf-8
from PySide2.QtWidgets import QGraphicsScene, QGraphicsView
from PySide.QtCore import QTimerEvent
from .Snake import SnakeBody


class View(QGraphicsView):
  def __init__(self, width: int, height: int, unit_width: int, unit_height: int):
    super().__init__()
    self.unit_width = unit_width
    self.unit_height = unit_height

    self.scene = self.get_scene(width, height)
    self.setScene(self.scene)
    self.timer_id = self.startTimer(1000)


  def get_scene(self, width: int, height: int) -> QGraphicsScene:
    self.body = self.add_body()
    scene = Scene(width, height)
    scene.addItem(self.body)
    return scene

  def add_body(self):
    return SnakeBody(self.unit_width, self.unit_height)

  def timerEvent(self, event: QTimerEvent):
    self.body.move()


class Scene(QGraphicsScene):
  def __init__(self, width: int, height: int):
    super().__init__(0, 0, width, height)

  def contextMenuEvent(self, event):
    print("event")
