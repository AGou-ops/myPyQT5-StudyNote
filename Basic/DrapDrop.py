'''
让控件支持拖拽动作
A.setDragEnabled(True)

B.setAcceptDrops(True)

B需要两个事件
1. dragEnterEvent   将A拖到B触发
2. dropEvent        在B的区域放下A时触发
'''
import sys
from PyQt5.QtWidgets import *


class myComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        print(e)
        # if e.mimeData().hasText():
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.addItem(e.mimeData().text())


class DrapDrop(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Drap Drop')
        formLayout = QFormLayout()
        formLayout.addRow(QLabel('Please Drag Left text to Right Combo Box'))
        self.lineEdit = QLineEdit()
        self.lineEdit.setDragEnabled(True)

        self.combox = myComboBox()
        self.combox.currentIndexChanged.connect(self.selectionChanged)
        formLayout.addRow(self.lineEdit, self.combox)
        self.setLayout(formLayout)
        self.show()

    def selectionChanged(self, i):
        print(self.combox.currentText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrapDrop()
    sys.exit(app.exec_())
