from PyQt5.QtWidgets import QWidget, QDialog, QLabel, QLineEdit, QPushButton, QGridLayout, QApplication
import sys


class LabelBuddy(QDialog):
    def __init__(self):
        super(LabelBuddy, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Label Buddy with lineTextEdit")

        nameLabel = QLabel('&Name：', self)
        nameLineEdit = QLineEdit(self)
        nameLabel.setBuddy(nameLineEdit)

        passwdLabel = QLabel('&Passwd：', self)
        passwdLineEdit = QLineEdit(self)
        passwdLabel.setBuddy(passwdLineEdit)

        btnOK = QPushButton('OK', self)
        btnCanel = QPushButton('Canel', self)

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)
        mainLayout.addWidget(passwdLabel, 1, 0)
        mainLayout.addWidget(passwdLineEdit, 1, 1, 1, 2)
        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCanel, 2, 2)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LabelBuddy()
    sys.exit(app.exec_())
