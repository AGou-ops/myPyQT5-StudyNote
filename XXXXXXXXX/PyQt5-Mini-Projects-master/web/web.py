from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QUrl 
import sys
 
class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('web.ui', self)
        self.btnGo.clicked.connect(self.onClick)
        self.btnBack.clicked.connect(self.goBack)

    def goBack(self):
        self.webView.back()

    def onClick(self):
        newUrl = self.url.text()
        self.webView.setUrl(QUrl(newUrl))

app = QtWidgets.QApplication([])
win = Example()
win.show()
sys.exit(app.exec())
