from PyQt5 import QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtWidgets import *
import sys


class Printer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Printer')

        layout = QVBoxLayout()

        self.button = QPushButton('Print TextEdit Content',self)
        self.editor = QTextEdit('Something here.',self)
        layout.addWidget(self.button)
        layout.addWidget(self.editor)
        self.button.clicked.connect(self.print)
        self.setLayout(layout)
        self.show()

    def print(self):
        printer = QtPrintSupport.QPrinter()

        painter = QtGui.QPainter()
        # 将绘制的目标重定向到打印机
        painter.begin(printer)
        screen = self.editor.grab()
        painter.drawPixmap(10,10,screen)
        painter.end()
        print("print")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Printer()
    sys.exit(app.exec_())
