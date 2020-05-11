import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
                             QColorDialog, QApplication, QVBoxLayout, QLabel)
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ColorDialog2(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Set Color For Font')
        layout = QVBoxLayout()
        self.colorBtn = QPushButton('Set Color')
        self.colorBtn.clicked.connect(self.setColor)
        layout.addWidget(self.colorBtn)

        self.testLabel = QLabel('Test Font!')
        layout.addWidget(self.testLabel)

        self.setLayout(layout)
        self.setGeometry(300, 300, 250, 180)
        self.show()

    def setColor(self):
        color = QColorDialog.getColor()
        # 调用调色板
        p = QPalette()
        p.setColor(QPalette.WindowText, color)
        self.testLabel.setPalette(p)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorDialog2()
    sys.exit(app.exec())
