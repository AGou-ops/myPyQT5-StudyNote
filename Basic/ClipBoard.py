import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ClipBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Clip Board')
        self.copyBtn = QPushButton('copy text')
        self.pasteBtn = QPushButton('paste text')

        self.copyHTMLBtn = QPushButton('copy HTML')
        self.pasteHTMLBtn = QPushButton('paste HTML')

        self.copyImgBtn = QPushButton('copy image')
        self.pasteImgBtn = QPushButton('paste image')

        self.textLabel = QLabel('Defalut Text')
        self.imgLabel = QLabel()
        self.imgLabel.setPixmap(QPixmap('/home/agou-ops/PycharmProjects/myPyQT5-StudyNote/imgs/logo32_32.ico'))

        layout = QGridLayout()
        layout.addWidget(self.copyBtn, 0, 0)
        layout.addWidget(self.pasteBtn, 1, 0)
        layout.addWidget(self.copyHTMLBtn, 0, 2)
        layout.addWidget(self.pasteHTMLBtn, 1, 2)
        layout.addWidget(self.copyImgBtn, 0, 1)
        layout.addWidget(self.pasteImgBtn, 1, 1)

        layout.addWidget(self.textLabel, 2, 0, 1, 2)
        layout.addWidget(self.imgLabel, 2, 2)

        self.setLayout(layout)

        self.copyBtn.clicked.connect(self.copyText)
        self.pasteBtn.clicked.connect(self.pasteText)
        self.copyHTMLBtn.clicked.connect(self.copyHtml)
        self.pasteHTMLBtn.clicked.connect(self.pasteHtml)
        self.copyImgBtn.clicked.connect(self.copyImage)
        self.pasteImgBtn.clicked.connect(self.pasteImage)

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText('hello world')

    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())

    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap('/home/agou-ops/PycharmProjects/myPyQT5-StudyNote/imgs/test.jpg'))

    def pasteImage(self):
        clipboard = QApplication.clipboard()
        self.imgLabel.setPixmap(clipboard.pixmap())

    def copyHtml(self):
        mimeData = QMimeData()
        mimeData.setHtml('<b>Bold and <font color=red>Red</font></b>')
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ClipBoard()
    main.show()
    sys.exit(app.exec_())