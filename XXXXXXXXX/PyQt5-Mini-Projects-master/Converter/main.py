import os
from PyQt5 import QtWidgets, uic


def converter():
    dlg.lineEdit_2.setText(str(float(dlg.lineEdit.text()) * 1.23))



app = QtWidgets.QApplication([])
dlg = uic.loadUi('main.ui')

dlg.pushButton.clicked.connect(converter)

dlg.show()
app.exec()

os.exit()