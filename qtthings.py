from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor, QBrush
from PyQt5.QtCore import Qt
from PyQt5 import uic
from ui import Ui_MainWindow
from random import randint
import sys


class Test(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.circle)

        self.label = QLabel()
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, 1, 0)

    def circle(self):
        x, y = [randint(10, 500) for _ in range(2)]
        size = randint(10, 200)
        painter = QPainter(self.label.pixmap())
        painter.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        painter.drawEllipse(x, y, size, size)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
