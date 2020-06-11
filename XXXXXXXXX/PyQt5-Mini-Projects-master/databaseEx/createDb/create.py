import sys, sqlite3

from sqlite3 import Error
from PyQt5.QtWidgets import QDialog,QApplication
from databaseEx.createDb.main import *

class Database(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.createDatabase)
        self.show()

    def createDatabase(self):
        try:
            conn = sqlite3.connect(self.ui.lineEdit.text()+'.db')
            self.ui.label.setText('connection is created')
        except Error as e:
            self.ui.label.setText('some error occured')
        finally:
            conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Database()
    w.show()
    sys.exit(app.exec())
