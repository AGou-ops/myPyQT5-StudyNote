# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(508, 441)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 10, 441, 391))
        self.tabWidget.setObjectName("tabWidget")
        self.productListing = QtWidgets.QWidget()
        self.productListing.setObjectName("productListing")
        self.nikes = QtWidgets.QCheckBox(self.productListing)
        self.nikes.setGeometry(QtCore.QRect(40, 40, 70, 17))
        self.nikes.setObjectName("nikes")
        self.adidas = QtWidgets.QCheckBox(self.productListing)
        self.adidas.setGeometry(QtCore.QRect(40, 80, 81, 17))
        self.adidas.setObjectName("adidas")
        self.puma = QtWidgets.QCheckBox(self.productListing)
        self.puma.setGeometry(QtCore.QRect(40, 130, 70, 17))
        self.puma.setObjectName("puma")
        self.fenty = QtWidgets.QCheckBox(self.productListing)
        self.fenty.setGeometry(QtCore.QRect(40, 180, 70, 17))
        self.fenty.setObjectName("fenty")
        self.addtocart = QtWidgets.QPushButton(self.productListing)
        self.addtocart.setGeometry(QtCore.QRect(40, 250, 75, 23))
        self.addtocart.setObjectName("addtocart")
        self.bill = QtWidgets.QLabel(self.productListing)
        self.bill.setGeometry(QtCore.QRect(250, 250, 47, 13))
        self.bill.setObjectName("bill")
        self.tabWidget.addTab(self.productListing, "")
        self.paymentMethod = QtWidgets.QWidget()
        self.paymentMethod.setObjectName("paymentMethod")
        self.mastercard = QtWidgets.QRadioButton(self.paymentMethod)
        self.mastercard.setGeometry(QtCore.QRect(30, 50, 82, 17))
        self.mastercard.setObjectName("mastercard")
        self.visacard = QtWidgets.QRadioButton(self.paymentMethod)
        self.visacard.setGeometry(QtCore.QRect(30, 100, 82, 17))
        self.visacard.setObjectName("visacard")
        self.netexpress = QtWidgets.QRadioButton(self.paymentMethod)
        self.netexpress.setGeometry(QtCore.QRect(30, 150, 82, 17))
        self.netexpress.setObjectName("netexpress")
        self.next = QtWidgets.QPushButton(self.paymentMethod)
        self.next.setGeometry(QtCore.QRect(280, 250, 75, 23))
        self.next.setObjectName("next")
        self.card = QtWidgets.QLabel(self.paymentMethod)
        self.card.setGeometry(QtCore.QRect(40, 250, 47, 13))
        self.card.setObjectName("card")
        self.tabWidget.addTab(self.paymentMethod, "")
        self.deliveryAddress = QtWidgets.QWidget()
        self.deliveryAddress.setObjectName("deliveryAddress")
        self.label = QtWidgets.QLabel(self.deliveryAddress)
        self.label.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.deliveryAddress)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 270, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.home = QtWidgets.QLineEdit(self.deliveryAddress)
        self.home.setGeometry(QtCore.QRect(120, 40, 251, 31))
        self.home.setObjectName("home")
        self.label_2 = QtWidgets.QLabel(self.deliveryAddress)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.deliveryAddress)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.deliveryAddress)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 91, 16))
        self.label_4.setObjectName("label_4")
        self.alternate = QtWidgets.QLineEdit(self.deliveryAddress)
        self.alternate.setGeometry(QtCore.QRect(120, 100, 251, 31))
        self.alternate.setObjectName("alternate")
        self.mobile = QtWidgets.QLineEdit(self.deliveryAddress)
        self.mobile.setGeometry(QtCore.QRect(120, 150, 251, 31))
        self.mobile.setObjectName("mobile")
        self.email = QtWidgets.QLineEdit(self.deliveryAddress)
        self.email.setGeometry(QtCore.QRect(120, 200, 251, 31))
        self.email.setObjectName("email")
        self.tabWidget.addTab(self.deliveryAddress, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 508, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nikes.setText(_translate("MainWindow", "Nikes $100"))
        self.adidas.setText(_translate("MainWindow", "Adidas $89"))
        self.puma.setText(_translate("MainWindow", "Puma $97"))
        self.fenty.setText(_translate("MainWindow", "Fenty $96"))
        self.addtocart.setText(_translate("MainWindow", "Add to Cart"))
        self.bill.setText(_translate("MainWindow", "Bill:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.productListing), _translate("MainWindow", "Product Listing"))
        self.mastercard.setText(_translate("MainWindow", "MasterCard"))
        self.visacard.setText(_translate("MainWindow", "VisaCard"))
        self.netexpress.setText(_translate("MainWindow", "NetExpress"))
        self.next.setText(_translate("MainWindow", "Next"))
        self.card.setText(_translate("MainWindow", "Card: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.paymentMethod), _translate("MainWindow", "Payment Method"))
        self.label.setText(_translate("MainWindow", "Home Address"))
        self.pushButton_3.setText(_translate("MainWindow", "Check Out"))
        self.label_2.setText(_translate("MainWindow", "Alternate Address"))
        self.label_3.setText(_translate("MainWindow", "Phone Num"))
        self.label_4.setText(_translate("MainWindow", "Email"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.deliveryAddress), _translate("MainWindow", "Delivery Address"))
