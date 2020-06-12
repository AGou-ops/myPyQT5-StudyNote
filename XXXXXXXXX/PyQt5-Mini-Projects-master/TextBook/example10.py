import sys
from PyQt5.QtWidgets import QDialog, QApplication
from exam10 import *


class Sname:
    name = ''
    gender = ''

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def print(self):
        return self.name

    def gen(self):
        return self.gender


class Marks(Sname):
    history = 0
    geography = 0

    def __init__(self, name, gender, history, geography):
        self.history = history
        self.geography = geography
        Sname.__init__(self, name, gender)

    def hisMarks(self):
        return self.history

    def geoMarks(self):
        return self.geography


class Total(Marks):
    totalMarks = 0
    percentage = 0

    def __init__(self, name, gender, history, geography, totalMarks, percentage):
        self.totalMarks = totalMarks
        self.percentage = percentage
        Marks.__init__(self, name, gender, history, geography)
        self.totalMarks = history + geography
        self.percentage = (history + geography) / 200 * 100

    def getTotal(self):
        return self.totalMarks

    def getPercentage(self):
        return self.percentage


class SomeName(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.someName)
        self.show()

    def someName(self):
        nameObj = Total(self.ui.lineEdit.text(),
        self.ui.lineEdit_2.text(),
        int(self.ui.lineEdit_3.text()),
        int(self.ui.lineEdit_4.text()))
        self.ui.total.setText(str(f'Total: {Total.getTotal()}')),
        self.ui.percent.setText(str(f'Percentage: {Total.getPercentage()}'))
        self.ui.listWidget.addItem(f'Candidate Name: {nameObj.print()}, Candidate Gender: {nameObj.gen()}\n'
                                   f'History Score: {Total.hisMarks()}, Geography: {Total.geoMarks()}\n'
                                   f'Total Marks: {Total.getTotal()}, Marks Percentage: {Total.getPercentage()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SomeName()
    w.show()
    sys.exit(app.exec())
