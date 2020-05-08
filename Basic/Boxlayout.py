import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        """
        addStretch()函数用于在控件按钮间增加伸缩量，
        伸缩量的比例为1:1:1:6，意思就是将控件以外的空白地方按设定的比例等分为9份
        
        并按照设定的顺序放入buttonLayout布局器中。
        这个就表示在这两个按键的左边放置一个Stretch，由于没有其他的Stretch，所以它占了空白的全部。
        所以这两个按键始终会被挤到hbox的最右边！
        """
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())