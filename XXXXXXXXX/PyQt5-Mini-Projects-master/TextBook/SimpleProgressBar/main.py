import sys
from PyQt5.QtWidgets import QDialog,QApplication
from mainUi import *
import time

class Fonts(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.update)
        self.show()

    def update(self):
        k = 0

        while k < 100:
            k += 0.00001
            self.ui.progressBar.setValue(k)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Fonts()
    w.show()
    sys.exit(app.exec())