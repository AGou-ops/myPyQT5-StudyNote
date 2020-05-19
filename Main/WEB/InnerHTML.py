import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('内嵌HTML')  # 窗口标题
        self.setGeometry(5, 30, 1355, 730)  # 窗口的大小和位置设置
        self.browser = QWebEngineView()
        # 加载html代码(这里注意html代码是用三个单引号包围起来的)
        self.browser.setHtml('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>测试页面</title>
</head>
<body>
    <h1>Hello PyQt5</h1>
    <h2>Hello PyQt5</h2>
    <h3>Hello PyQt5</h3>
    <h4>Hello PyQt5</h4>
</body>
</html>''')
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exit(app.exec_())
