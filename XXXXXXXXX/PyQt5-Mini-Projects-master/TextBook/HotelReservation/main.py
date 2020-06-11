import sys
from PyQt5.QtWidgets import QDialog, QApplication
from TextBook.HotelReservation.mainUi import *

class Hotel(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.roomTypes = ['Basic','Premium','Unique','Suite']
        self.addContent()
        self.ui.pushButton.clicked.connect(self.calculateRent)
        self.show()

    def addContent(self):
        for i in self.roomTypes:
            self.ui.comboBox.addItem(i)

    def calculateRent(self):
        selectedDate = self.ui.calendarWidget.selectedDate()
        dateString = str(selectedDate.toPyDate())
        days = self.ui.spinBox.value()
        chooseRoom = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        self.ui.user_choice.setText(f'you have selected {chooseRoom} , for reservation on {dateString} ,for {days} days.')
        roomRent = 0
        if chooseRoom == 'Basic':
            roomRent += 10000
        if chooseRoom == 'Premium':
            roomRent += 40000
        if chooseRoom == 'Unique':
            roomRent += 75000
        if chooseRoom == 'Suite':
            roomRent += 100000

        total= roomRent * days
        self.ui.total.setText(f'your bill is: {total} ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Hotel()
    w.show()
    sys.exit(app.exec())