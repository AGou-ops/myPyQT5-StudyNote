import sys
from PyQt5.QtWidgets import QDialog, QApplication
from mainUi import *


class Calculator(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.add.clicked.connect(self.calculateAdd)
        self.ui.subtract.clicked.connect(self.calculateSubtract)
        self.ui.multiply.clicked.connect(self.calculateMultiply)
        self.ui.divide.clicked.connect(self.calculateDivide)
        self.show()

    def calculateAdd(self):
        if len(self.ui.lineEdit.text()) != 0:
            a = int(self.ui.lineEdit.text())
        else:
            a = 0

        if len(self.ui.lineEdit_2.text()) != 0:
            b = int(self.ui.lineEdit_2.text())
        else:
            b = 0

        addition = a + b

        self.ui.results.setText(str(f'addition of numbers is: {addition}'))

    def calculateSubtract(self):
        if len(self.ui.lineEdit.text()) != 0:
            a = int(self.ui.lineEdit.text())
        else:
            a = 0

        if len(self.ui.lineEdit_2.text()) != 0:
            b = int(self.ui.lineEdit_2.text())
        else:
            b = 0

        subtraction = a - b

        self.ui.results.setText(str(f'subtraction of numbers is: {subtraction}'))

    def calculateMultiply(self):
        if len(self.ui.lineEdit.text()) != 0:
            a = int(self.ui.lineEdit.text())
        else:
            a = 0

        if len(self.ui.lineEdit_2.text()) != 0:
            b = int(self.ui.lineEdit_2.text())
        else:
            b = 0

        multiplication = a * b

        self.ui.results.setText(f'multiplication of numbers is: {multiplication}')

    def calculateDivide(self):
        if len(self.ui.lineEdit.text()) != 0:
            a = int(self.ui.lineEdit.text())
        else:
            a = 0

        if len(self.ui.lineEdit_2.text()) != 0:
            b = int(self.ui.lineEdit_2.text())
        else:
            b = 0

        division = a / b

        self.ui.results.setText(f'division of numbers is: {division}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Calculator()
    w.show()
    sys.exit(app.exec())
