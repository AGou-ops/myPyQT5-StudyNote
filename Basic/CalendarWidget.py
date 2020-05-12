import sys
from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
                             QLabel, QApplication)
from PyQt5.QtCore import QDate


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1988,1,1))
        self.cal.setMaximumDate(QDate(2088,1,1))
        self.cal.setGridVisible(True)
        self.cal.move(20, 20)
        # 如果我们从部件选择一个日期,点击[QDate]发出信号。我们将这个信号连接到用户定义的showDate()方法。
        self.cal.clicked[QDate].connect(self.showDate)
        # self.cal.clicked.connect(self.showDate)


        self.lbl = QLabel(self)
        date = self.cal.selectedDate()
        self.lbl.setText(date.toString("yyyy-MM-dd dddd"))
        self.lbl.move(260, 260)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString("yyyy-MM-dd dddd"))
        # self.lbl.setText((self.cal.selectedDate().toString("yyyy-MM-dd dddd")))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())