import sys

import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPixmap, QPen
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

SCREEN_SIZE = [400, 400]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(800, 650)
        self.pushButton.clicked.connect(self.generateyellowcircle)

    def generateyellowcircle(self):
        x = random.randint(0, 850)
        y = random.randint(0, 500)
        diam = random.randint(30, 200)
        canvas = QPixmap(800, 600)
        self.label.setPixmap(canvas)
        circle = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setColor(QColor(255, 255, 0))
        pen.setWidth(3)
        circle.setPen(pen)
        circle.drawEllipse(x, y, diam, diam)
        circle.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
