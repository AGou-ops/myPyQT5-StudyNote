import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFormLayout, QLineEdit, QApplication, QWidget


class EditLineEchoMode(QWidget):
    def __init__(self):
        super(EditLineEchoMode, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Edit Line four different Echo Mode')

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwdLineEdit = QLineEdit()
        passwdEchoOnEdit = QLineEdit()

        mainLayout = QFormLayout(self)
        # 添加一行
        mainLayout.addRow('Normal', normalLineEdit)
        mainLayout.addRow('NoEcho', noEchoLineEdit)
        mainLayout.addRow('Passwd', passwdLineEdit)
        mainLayout.addRow('PasswdEchoOnEdit', passwdEchoOnEdit)

        normalLineEdit.setPlaceholderText('Normal')
        noEchoLineEdit.setPlaceholderText('NoEcho')
        passwdLineEdit.setPlaceholderText('Passwd')
        passwdEchoOnEdit.setPlaceholderText('PasswdEchoOnEdit')

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwdLineEdit.setEchoMode(QLineEdit.Password)
        passwdEchoOnEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(mainLayout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = EditLineEchoMode()
    sys.exit(app.exec_())
