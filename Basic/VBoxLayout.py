'''

垂直盒布局（QBoxLayout）



'''

import sys, math
from PyQt5.QtWidgets import *


class VBoxLayout(QWidget):
    def __init__(self):
        super(VBoxLayout, self).__init__()
        self.setWindowTitle("垂直盒布局")

        layout = QVBoxLayout()
        btn1 = QPushButton('按钮1')

        btn2 = QPushButton('按钮2')
        btn3 = QPushButton('按钮3')
        # 设置控件伸缩量
        layout.addStretch(0)
        layout.addWidget(btn1)
        layout.addStretch(1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = VBoxLayout()
    main.show()
    sys.exit(app.exec_())
