"""
import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget


class exitApplication(QMainWindow):
    def __init__(self):
        super(exitApplication, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle("Exit Application")

        self.button1 = QPushButton('退出')
        self.button1.clicked.connect(self.clicked)
        # 创建水平布局，在水平布局中添加一个小部件，该小部件就是上面所定义的退出按钮
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        # 创建窗体，并设置主窗体的布局为上面定义好的水平布局
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        # 创建主窗体，将上面的窗体添加进来
        self.setCentralWidget(mainFrame)

    def clicked(self):
        sender = self.sender()
        print(sender.text() + ' 按钮被按下')
        app = QApplication.instance()
        # 退出应用程序
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = exitApplication()
    main.show()
    sys.exit(app.exec_())
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
