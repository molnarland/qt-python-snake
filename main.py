# This Python file uses the following encoding: utf-8
import sys
import time

from PySide2.QtWidgets import QGraphicsScene, QGraphicsItem, QGraphicsView, QApplication, QWidget
from PySide2.QtCore import QRectF
from Menu import Menu


class Item(QGraphicsItem):
  def __init__(self):
    super().__init__()

  def boundingRect(self):
    penWidth = 1.0
    return QRectF(-10 - penWidth / 2, -10 - penWidth / 2, 20 + penWidth, 20 + penWidth)

  def paint(self, painter, option, widget):
    painter.drawRoundedRect(-10, -10, 20, 20, 5, 5)

  def mousePressEvent(self, event):
    pos = self.pos()
    self.setPos(pos.x() + 10, pos.y() + 10)
    print("a")

  def mouseDoubleClickEvent(self, event):
    self.hide()


class MainWindow(QWidget):
  def __init__(self):
    super().__init__()

  def mousePressEvent(self, event):
    window = QWidget()
    window.show()
#    scene = QGraphicsScene()
#    view = QGraphicsView(scene)
#    view.show()
#    scene.addItem(Item(view))



class View(QGraphicsView):
  def __init__(self):
    super().__init__()
    self.show_menu()

  def show_menu(self):
    self.setScene(Menu(self.click))

  def click(self):
    self.setScene(QGraphicsScene())


def show():
  view = View()
  view.show()


if __name__ == "__main__":
  app = QApplication()

  menu = Menu()
  menu.show()

  app.exec_()




