import sys
from random import *
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        uic.loadUi('yellow_circles.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def run(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 216, 0))
        a = randint(0, 519)
        qp.drawEllipse(randint(0, 519), randint(0, 519), a, a)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    sys.excepthook = except_hook
    w.show()
    sys.exit(app.exec())
