"""
停靠控件
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DockWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Stacked Widget')
        self.setGeometry(200, 200, 600, 420)

        layout = QHBoxLayout()
        self.items = QDockWidget('Dockable', self)

        self.listWidget = QListWidget()
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')

        self.items.setWidget(self.listWidget)
        self.setCentralWidget(QPushButton('test Button'))
        self.items.setFloating(False)
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DockWidget()
    window.show()
    sys.exit(app.exec_())
