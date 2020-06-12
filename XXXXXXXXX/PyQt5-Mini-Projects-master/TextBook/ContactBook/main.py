import sqlite3,sys

from PyQt5.QtWidgets import QDialog,QApplication,QInputDialog, QTableWidgetItem
from mainUi import *

class Contacts(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.add.clicked.connect(self.addContacts)
        self.ui.add_2.clicked.connect(self.displayContacts)
        # self.ui.edit.clicked.connect(self.editContacts)
        self.ui.delete_2.clicked.connect(self.deleteContacts)
        self.ui.clear.clicked.connect(self.clearContacts)
        self.show()

    def addContacts(self):
        id = int(self.ui.lineEdit_3.text())
        self.ui.lineEdit_3.setText('')
        self.ui.lineEdit_3.setFocus()

        name = self.ui.lineEdit.text()
        self.ui.lineEdit.setText('')
        self.ui.lineEdit.setFocus()

        phone = int(self.ui.lineEdit_2.text())
        self.ui.lineEdit_2.setText('')
        self.ui.lineEdit_2.setFocus()



        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute('INSERT INTO CONTACTS VALUES (?,?,?)', (id,name, phone))

        conn.commit()
        conn.close()

    def displayContacts(self):
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        query = c.execute('select * from CONTACTS')
        conn.commit()
        self.ui.tableWidget.setRowCount(0)
        for row_num, row_data in enumerate(query):
            self.ui.tableWidget.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))
            row_num +=1
        conn.close()

    # def editContacts(self):
    #     contact = self.ui.listWidget.currentRow()
    #     newtext, ok=QInputDialog.getText(self, 'Enter new Contact', 'enter new Contact')
    #     if ok and (len(newtext)) != 0:
    #         self.ui.listWidget.takeItems()
    #         self.ui.listWidget.insertItems()
    #
    #     conn = sqlite3.connect('contacts.db')
    #     c = conn.cursor()
    #     c.execute('UPDATE CONTACTS SET name = contact WHERE id = id')

    def deleteContacts(self):
        id = self.ui.tableWidget.takeItem(self.ui.tableWidget.currentRow())

        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute('DELETE from CONTACTS WHERE id = id')

        conn.commit()
        conn.close()


    def clearContacts(self):
        self.ui.tableWidget.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Contacts()
    w.show()
    sys.exit(app.exec())