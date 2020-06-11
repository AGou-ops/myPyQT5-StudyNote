import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QDialog, QApplication
#from PyQt5.QtWebEngineWidgets import QWebEngineView

from TextBook.exam11 import *


class Browser(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.go)
        self.show()

    def go(self):
        self.ui.widget.load(QUrl(self.ui.lineEdit.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Browser()
    w.show()
    sys.exit(app.exec())
