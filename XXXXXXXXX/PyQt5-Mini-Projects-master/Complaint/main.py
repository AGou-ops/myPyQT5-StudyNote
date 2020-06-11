from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import sys


class Complaint(QtWidgets.QMainWindow):
    def __init__(self):
        super(Complaint, self).__init__()
        uic.loadUi('main.ui', self)



app = QtWidgets.QApplication([])
win = Complaint()
win.show()
sys.exit(app.exec())
