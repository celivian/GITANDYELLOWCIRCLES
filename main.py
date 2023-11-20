import sys

import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPixmap, QPen
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from ui import *

SCREEN_SIZE = [400, 400]


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800, 650)
        self.pushButton.clicked.connect(self.generateyellowcircle)

    def generateyellowcircle(self):
        x = random.randint(0, 850)
        y = random.randint(0, 500)
        diam = random.randint(30, 200)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        canvas = QPixmap(800, 600)
        self.label.setPixmap(canvas)
        circle = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setColor(color)
        pen.setWidth(3)
        circle.setPen(pen)
        circle.drawEllipse(x, y, diam, diam)
        circle.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
