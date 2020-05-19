"""
singleShot 用于单次执行某个任务
timer 多次执行某个任务
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel('<font color=red size=140><b>Hello World，窗口在3秒后自动关闭!</b></font>')
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    label.show()
    QTimer.singleShot(3000, app.quit)

    sys.exit(app.exec_())
