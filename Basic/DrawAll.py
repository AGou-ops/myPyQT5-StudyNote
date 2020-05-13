import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtCore import Qt


class DrawLines(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Draw All')
        self.setGeometry(300, 300, 350, 300)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)

        painter.setPen(Qt.darkYellow)

        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrawLines()
    window.show()
    sys.exit(app.exec_())
