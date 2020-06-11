import sys
from PyQt5.QtWidgets import QDialog, QApplication
from TextBook.RadioDialog.mainUi import *


class Shopper(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButton.toggled.connect(self.selOption)
        self.ui.radioButton_2.toggled.connect(self.selOption)
        self.ui.radioButton_3.toggled.connect(self.selOption)
        self.ui.radioButton_4.toggled.connect(self.selOption)
        self.ui.radioButton_5.toggled.connect(self.selOption)
        self.ui.radioButton_6.toggled.connect(self.selOption)
        self.ui.radioButton_7.toggled.connect(self.selOption)
        self.show()

    def selOption(self):
        select = "";
        select2 = ""

        if self.ui.radioButton.isChecked():
            select = 'S'
        if self.ui.radioButton_2.isChecked():
            select = 'M'
        if self.ui.radioButton.isChecked():
            select = 'XL'
        if self.ui.radioButton_3.isChecked():
            select = 'X'
        if self.ui.radioButton_4.isChecked():
            select = 'S'

        if self.ui.radioButton_5.isChecked():
            select2 = 'MasterCard'
        if self.ui.radioButton_6.isChecked():
            select2 = 'VisaCard'
        if self.ui.radioButton_7.isChecked():
            select2 = 'NetExpress'

        self.ui.label_2.setText('you have pick shirt size ' + select + ' and payment method ' + select2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Shopper()
    w.show()
    sys.exit(app.exec())
