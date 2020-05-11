import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt

class DrawText(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Draw Text')
        self.setGeometry(300, 300, 350, 300)
        self.text = 'Text Text Text'

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)

        painter.setPen(QColor(150, 55, 5))
        painter.setFont(QFont('Ubuntu', 25))

        painter.drawText(event.rect(), Qt.AlignCenter, self.text)
        print('Painter Actived')
        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrawText()
    window.show()
    sys.exit(app.exec_())
