'''

输入对话框：QInputDialog

QInputDialog.getItem
QInputDialog.getText
QInputDialog.getInt

'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class InputDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Input Dialog')
        layout = QFormLayout()

        self.btn1 = QPushButton('Get Items Value')
        self.btn1.clicked.connect(self.getItem)
        self.lineEdit1 = QLineEdit()

        self.btn2 = QPushButton('Get String')
        self.btn2.clicked.connect(self.getText)
        self.lineEdit2 = QLineEdit()

        self.btn3 = QPushButton('Get Integer')
        self.btn3.clicked.connect(self.getInt)
        self.lineEdit3 = QLineEdit()

        layout.addRow(self.btn1, self.lineEdit1)
        layout.addRow(self.btn2, self.lineEdit2)
        layout.addRow(self.btn3, self.lineEdit3)
        self.setLayout(layout)
        self.show()

    def getItem(self):
        items = ('C++', 'Python', 'Java', 'Go')
        item, ok = QInputDialog.getItem(self, 'Please Choose a Language', 'Item List', items)
        if ok and item:
            self.lineEdit1.setText(item)

    def getText(self):
        text, ok = QInputDialog.getText(self, 'Input your Language', 'Language')
        if ok and text:
            self.lineEdit2.setText(text)

    def getInt(self):
        integer, ok = QInputDialog.getInt(self, 'Input a Number', 'Number')
        if ok and integer:
            self.lineEdit3.setText(str(integer))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputDialog()
    sys.exit(app.exec_())
