import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.button1 = QPushButton('加载图片')
        self.button1.clicked.connect(self.loadImage)
        layout.addWidget(self.button1)

        self.imageLabel = QLabel()
        layout.addWidget(self.imageLabel)

        self.button2 = QPushButton('加载文本文件')
        self.button2.clicked.connect(self.loadText)
        layout.addWidget(self.button2)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)
        self.setWindowTitle('文件对话框演示 ')

    def loadImage(self):
        fname, _ = QFileDialog.getOpenFileName(self, '打开文件', '/home/agou-ops/Pictures', '图像文件(*.jpg *.png)')
        self.imageLabel.setPixmap(QPixmap(fname))

    def loadText(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home/agou-ops/Documents')
        # fname,_ = QFileDialog.getOpenFileName(self, 'Open file', '/home/agou-ops/Documents')
        print(fname[0])
        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.contents.setText(data)

        """
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            f = open(filenames[0], encoding='utf-8', mode='r')
            with f:
                data = f.read()
                self.contents.setText(data)
        """

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())
