import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem

from mainUi import *

class Add(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.addItem)
        self.ui.pushButton_2.clicked.connect(self.editItem)
        self.ui.pushButton_3.clicked.connect(self.deleteItem)
        self.ui.pushButton_4.clicked.connect(self.clear)

        self.listIsNull()

        self.show()

    def listIsNull(self):
        # 判断列表是否为空
        listNum = int(self.ui.listWidget.count())
        if listNum == 0:
            self.ui.pushButton_2.setEnabled(False)
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(False)
        else:
            self.ui.pushButton_2.setEnabled(True)
            self.ui.pushButton_3.setEnabled(True)
            self.ui.pushButton_4.setEnabled(True)

    def addItem(self):
        self.ui.listWidget.addItem(self.ui.lineEdit.text())
        self.ui.lineEdit.setText('')
        self.ui.lineEdit.setFocus()
        self.ui.label_2.setText(str(self.ui.listWidget.count()))
        self.listIsNull()

    def editItem(self):
        row = self.ui.listWidget.currentRow()
        newtext, ok = QInputDialog.getText(self, 'Enter new text', 'enter new text')
        if ok and (len(newtext)) != 0:
            self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
            self.ui.listWidget.insertItem(row, QListWidgetItem(newtext))

    def deleteItem(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
        self.ui.label_2.setText(str(self.ui.listWidget.count()))
        self.listIsNull()

    def clear(self):
        self.ui.listWidget.clear()
        self.listIsNull()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Add()
    w.show()
    sys.exit(app.exec())