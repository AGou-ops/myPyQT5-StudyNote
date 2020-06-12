import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

"""
选中文本即复制
"""

class mylineedit(QLineEdit):
    clicked = pyqtSignal()

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()


class test(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('选中即复制')
        layout = QVBoxLayout()

        self.lnd = mylineedit()
        self.lnd.setPlaceholderText("选中及复制")
        self.lnd.clicked.connect(self.copyClicked)

        self.button = QPushButton('黏贴')
        self.button.clicked.connect(self.pasteBtnClicked)
        """或者直接使用内置槽函数
        self.button.pressed.connect(self.lnd.selectAll)
        self.button.released.connect(self.lnd.copy)
        """

        self.pasteBox = QLineEdit()
        """
        self.button.clicked.connect(self.pasteBox.paste)
        """
        layout.addWidget(self.lnd)
        layout.addWidget(self.button)
        layout.setSpacing(50)
        layout.addWidget(self.pasteBox)

        self.setLayout(layout)

    def copyClicked(self):
        self.lnd.selectAll()
        self.lnd.copy()

    def pasteBtnClicked(self):
        self.pasteBox.setText("")
        self.pasteBox.paste()


if __name__ == '__main__':
    app = QApplication([])
    window = test()
    window.show()
    sys.exit(app.exec())
