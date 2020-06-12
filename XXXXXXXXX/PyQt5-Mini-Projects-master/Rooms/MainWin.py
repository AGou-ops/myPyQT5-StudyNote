import sys, pymongo
import datetime

from pymongo import MongoClient

from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from main import Ui_MainWindow
from register import Ui_Dialog
from login import Ui_Dialog

port = 27017

client = MongoClient('localhost', port)
db = client['test_database']


class Login(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.logButton.clicked.connect(self.login)
        #self.ui.logButton_2.clicked.connect(s)
        self.show()

    def login(self):
        username = self.ui.logEmail.text()
        self.ui.logEmail.setText('')
        self.ui.logEmail.setFocus()
        password = self.ui.logPassword.text()
        self.ui.logPassword.setText('')
        self.ui.logPassword.setFocus()

        Users = db.users
        count = Users.find({'username': username}, {'password': password}).count()

        if count == 0:
            self.ui.logError.setText('Wrong Username or Password')
        else:
            self.accept()


class Register(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.regButton.clicked.connect(self.register)

        self.show()

    def register(self):
        username = self.ui.regEmail.text()
        self.ui.regEmail.setText('')
        self.ui.regEmail.setFocus()
        password = self.ui.regPassword.text()
        self.ui.regPassword.setText('')
        self.ui.regPassword.setFocus()

        Users = db.users

        user = {'username': username,
                'password': password,
                "date": datetime.datetime.utcnow()}
        Users.insert_one(user)

        count = Users.find({'username': username}).count()

        if count != 0:
            self.ui.regError.setText('Username is already available')
        else:
            self.accept()

class Rooms(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


app = QApplication(sys.argv)
passdlg = Register()
if passdlg.exec() == QDialog.Accepted:
    w = Rooms()
    w.show()
sys.exit(app.exec())
