# -*- coding: utf-8 -*- 
'''
    【简介】
    PyQT5中关闭应用例子
 
  
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

time = 10


class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showlabel)
        self.timer.singleShot(10000, app.quit)
        self.showlabel()
        self.label.show()

    def showlabel(self):
        self.timer.start(1000)
        global time
        self.label.setText("<font color=red size=128><b>Hello PyQT，窗口会在 %d 秒后消失！</b></font>" % time)
        time -= 1
        print(time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = Test()
    # 设置10s后自动退出
    sys.exit(app.exec_())
