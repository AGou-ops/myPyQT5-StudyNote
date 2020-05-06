import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon


class myFirstMainWindow(QMainWindow):
    def __init__(self):
        super(myFirstMainWindow, self).__init__()

        self.setWindowTitle("my First Main Window!")
        self.resize(500, 300)
        self.statusBar = self.statusBar()
        self.statusBar.showMessage("该消息五秒后消失", 5000)
        self.center()

    def center(self):
        """ 居中实现方式一
        # 获取屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)
        """
        # 居中实现方式二
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./logo32_32.ico"))
    main = myFirstMainWindow()
    main.show()

    sys.exit(app.exec_())
