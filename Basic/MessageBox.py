import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QVBoxLayout, QPushButton


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        layout = QVBoxLayout()

        self.btn1 = QPushButton('About Dialog')
        self.btn1.clicked.connect(self.showDialog)
        self.btn2 = QPushButton('Message Dialog')
        self.btn2.clicked.connect(self.showDialog)
        self.btn3 = QPushButton('Warnning Dialog')
        self.btn3.clicked.connect(self.showDialog)
        self.btn4 = QPushButton('Error Dialog')
        self.btn4.clicked.connect(self.showDialog)


        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
        self.setLayout(layout)
        self.show()

    def showDialog(self):
        text = self.sender().text()
        if text == 'About Dialog':
                QMessageBox.aboutQt(self, 'About')
        elif text == 'Message Dialog':
                reply = QMessageBox.information(self, 'Message Box', 'This is a Message Box',
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        elif text == 'Warnning Dialog':
                reply = QMessageBox.warning(self, 'Message Box', 'This is a Warnning Box',
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        elif text == 'Error Dialog':
                reply = QMessageBox.critical(self, 'Message Box', 'This is a Error Box',
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    # 重写closeEvent()事件处理程序
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
