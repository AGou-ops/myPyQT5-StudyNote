import sys
from PyQt5.QtWidgets import QDialog, QApplication
from TextBook.InputDialog.mainUi import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.showMessage)
        self.show()

    def showMessage(self):
        self.ui.label_2.setText("what cha up to " +
                                self.ui.lineEdit.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
