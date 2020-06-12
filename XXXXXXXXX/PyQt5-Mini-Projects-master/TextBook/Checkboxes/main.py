import sys
from PyQt5.QtWidgets import QDialog, QApplication
from mainUi import *


class Menu(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.brisk.stateChanged.connect(self.menuOptions)
        self.ui.stoup.stateChanged.connect(self.menuOptions)
        self.ui.rochin.stateChanged.connect(self.menuOptions)
        self.ui.chicken.stateChanged.connect(self.menuOptions)
        self.ui.rice.stateChanged.connect(self.menuOptions)
        self.ui.potato.stateChanged.connect(self.menuOptions)
        self.ui.cake.stateChanged.connect(self.menuOptions)
        self.ui.ice_cream.stateChanged.connect(self.menuOptions)
        self.ui.pie.stateChanged.connect(self.menuOptions)
        self.show()

    def menuOptions(self):
        amount = 0

        if self.ui.brisk.isChecked() == True:
            amount = amount + 12
        if self.ui.stoup.isChecked() == True:
            amount = amount + 10
        if self.ui.rochin.isChecked() == True:
            amount = amount + 11
        if self.ui.chicken.isChecked() == True:
            amount = amount + 32
        if self.ui.rice.isChecked() == True:
            amount = amount + 26
        if self.ui.potato.isChecked() == True:
            amount = amount + 20
        if self.ui.cake.isChecked() == True:
            amount = amount + 5
        if self.ui.ice_cream.isChecked() == True:
            amount = amount + 6
        if self.ui.pie.isChecked() == True:
            amount = amount + 5

        self.ui.label_5.setText(f"Bill: {amount}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Menu()
    w.show()
    sys.exit(app.exec())
