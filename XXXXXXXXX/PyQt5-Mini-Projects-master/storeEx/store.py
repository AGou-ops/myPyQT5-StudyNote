import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox
from storeEx.main import *


class Store(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.nikes.stateChanged.connect(self.storeOptions)
        self.ui.adidas.stateChanged.connect(self.storeOptions)
        self.ui.puma.stateChanged.connect(self.storeOptions)
        self.ui.fenty.stateChanged.connect(self.storeOptions)
        self.ui.mastercard.toggled.connect(self.cardOptions)
        self.ui.visacard.toggled.connect(self.cardOptions)
        self.ui.netexpress.toggled.connect(self.cardOptions)
        self.ui.addtocart.clicked.connect(self.onClickTab)
        #self.ui.next.clicked.connect(self.onClickTab2)
        self.ui.pushButton_3.clicked.connect(self.checkOut)
        self.show()

    def storeOptions(self):
        bill = 0
        if self.ui.nikes.isChecked() == True:
            bill = bill + 100
        if self.ui.adidas.isChecked() == True:
            bill = bill + 89
        if self.ui.puma.isChecked() == True:
            bill = bill + 96
        if self.ui.fenty.isChecked() == True:
            bill = bill + 97

        self.ui.bill.setText(str(f'Bill: {bill}'))

    def cardOptions(self):
        cardType = ''
        if self.ui.mastercard.isChecked():
            cardType = 'MasterCard'
        if self.ui.visacard.isChecked():
            cardType = 'VisaCard'
        if self.ui.netexpress.isChecked():
            cardType = 'NetExpress'
        self.ui.card.setText(f'Card: {cardType}')

    def checkOut(self):
        home = self.ui.home.text()
        alternate = self.ui.alternate.text()
        mobile = int(self.ui.mobile.text())
        email = self.ui.email.text()
        choice = QMessageBox.question(self, 'Checkout', 'Are you Ready to Check Out',
                                      QMessageBox.Yes | QMessageBox.No)

        if choice == QMessageBox.Yes:
            print(f'{home}\n {alternate}\n {mobile}\n {email}')

    def onClickTab(self):
        QtWidgets.QTabWidget.currentIndex(self.paymentMethod)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Store()
    w.show()
    sys.exit(app.exec())
