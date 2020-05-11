import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtCore import Qt


class DrawLines(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Draw Lines')
        self.setGeometry(300, 300, 350, 300)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)

        pen = QPen(Qt.black, 3, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(20, 40, 300, 40)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 60, 300, 60)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 80, 300, 80)

        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrawLines()
    window.show()
    sys.exit(app.exec_())
