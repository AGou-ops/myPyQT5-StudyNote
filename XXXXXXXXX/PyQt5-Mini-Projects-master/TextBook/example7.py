import sys
from PyQt5.QtWidgets import QDialog,QApplication
from TextBook.exam7 import *

class Fonts(QDialog):
    def __init__(self):
        super(Fonts, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        myFont = QtGui.QFont(self.ui.comboBox.itemText(self.ui.comboBox.currentIndex()), 15)
        self.ui.lineEdit.setFont(myFont)
        self.ui.comboBox.currentFontChanged.connect(self.changeFont)
        self.show()

    def changeFont(self):
        myFont = QtGui.QFont(self.ui.comboBox.itemText(self.ui.comboBox.currentIndex()), 15)
        self.ui.lineEdit.setFont(myFont)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Fonts()
    w.show()
    sys.exit(app.exec())