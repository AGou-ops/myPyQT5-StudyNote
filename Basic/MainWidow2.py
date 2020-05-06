from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class ui_MainWindow(object):
    def __init__(self):
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

    def setupUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        MainWindow.setWindowTitle("my First Main Window")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.showMessage("该消息五秒后消失", 5000)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("../imgs/logo32_32.ico"))
    MainWindow = QtWidgets.QMainWindow()
    ui = ui_MainWindow()
    ui.setupUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
