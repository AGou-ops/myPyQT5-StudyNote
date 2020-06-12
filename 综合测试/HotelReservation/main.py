import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QApplication
from mainUi import *
import datetime

"""
实时检测控件变化
"""

class Hotel(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.roomTypes = ['Basic', 'Premium', 'Unique', 'Suite']
        self.ui.comboBox.addItems(self.roomTypes)
        self.date_message, self.roomTypes_message, self.days_message = datetime.datetime.now().strftime(
            '%Y-%m-%d'), "Basic", "1"
        # self.addContent()
        # self.ui.pushButton.clicked.connect(self.calculateRent)
        self.ui.calendarWidget.clicked[QtCore.QDate].connect(self.dateChanged)
        self.ui.comboBox.currentIndexChanged.connect(self.typeChanged)
        self.ui.spinBox.valueChanged.connect(self.dayChanged)
        self.show()

    # def addContent(self):
    #     for i in self.roomTypes:
    #         self.ui.comboBox.addItems(i)

    # def calculateRent(self):
    #     pass

    def dateChanged(self, data):
        print(data.toString("yyyy-MM-dd"))
        self.date_message = data.toString("yyyy-MM-dd")
        self.update()

    def typeChanged(self, str):
        print(self.ui.comboBox.itemText(str))
        type = self.ui.comboBox.itemText(str)
        self.roomTypes_message = type
        self.update()

    def dayChanged(self, day):
        print(day)
        self.days_message = day
        self.update()

    def paintEvent(self, event):
        # selectedDate = self.ui.calendarWidget.selectedDate()
        # dateString = str(selectedDate.toPyDate())
        dateString = self.date_message
        # days = self.ui.spinBox.value()
        days = self.days_message
        # chooseRoom = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        chooseRoom = self.roomTypes_message
        self.ui.user_choice.setText(
            f'you have selected {chooseRoom} , for reservation on {dateString} ,for {days} days.')
        roomRent = 0
        if chooseRoom == 'Basic':
            roomRent += 10000
        if chooseRoom == 'Premium':
            roomRent += 40000
        if chooseRoom == 'Unique':
            roomRent += 75000
        if chooseRoom == 'Suite':
            roomRent += 100000

        total = roomRent * days
        self.ui.total.setText(f'your bill is: {total} ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Hotel()
    w.show()
    sys.exit(app.exec())
