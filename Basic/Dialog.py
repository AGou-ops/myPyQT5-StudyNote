'''

对话框：QDialog

QMessageBox
QColorDialog
QFileDialog
QFontDialog
QInputDialog

QMainWindow
QWidget
QDialog

'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class myDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Show Dialog')
        self.resize(300, 150)

        self.btn = QPushButton('show dialog box', self)
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.showDialog)

        self.show()

    def showDialog(self):
        dialog = QDialog()
        okBtn = QPushButton('OK', dialog)
        okBtn.clicked.connect(dialog.close)
        okBtn.move(50, 50)
        dialog.setWindowTitle('Dialog')
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = myDialog()
    sys.exit(app.exec_())






