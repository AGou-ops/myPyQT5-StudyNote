import sys, sqlite3

from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QTableWidget
from databaseEx.createTabCol.main import *


class Database(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.add.clicked.connect(self.addItems)
        self.ui.display.clicked.connect(self.displayData)
        self.show()

    def addItems(self):
        id = int(self.ui.id.text())
        self.ui.id.setText('')
        self.ui.id.setFocus()
        name = self.ui.name.text()
        self.ui.name.setText('')
        self.ui.name.setFocus()
        age = int(self.ui.age.text())
        self.ui.age.setText('')
        self.ui.age.setFocus()
        address = self.ui.address.text()
        self.ui.address.setText('')
        self.ui.address.setFocus()
        marks = int(self.ui.marks.text())
        self.ui.marks.setText('')
        self.ui.marks.setFocus()

        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        c.execute('INSERT INTO SCHOOL VALUES (?,?,?,?,?)', (id, name, age, address, marks))
        c.close()
        conn.commit()
        conn.close()

    def displayData(self):
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        query = c.execute('SELECT * FROM SCHOOL')
        self.ui.tableWidget.setRowCount(0)
        for row_num, row_data in enumerate(query):
            self.ui.tableWidget.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))

        # rows = c.fetchall()
        # rowCount = 0
        # for tuple in rows:
        #     columnCount = 0
        # for columns in tuple:
        #     oneColumn = QTableWidgetItem(columns)
        #     self.ui.tableWidget.setItem(rowCount, columnCount, oneColumn)
        #     columnCount += 1
        #     rowCount += 1
        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Database()
    w.show()
    sys.exit(app.exec())
