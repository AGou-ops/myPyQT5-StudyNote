# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(587, 475)
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(260, 50, 296, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(260, 260, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(260, 300, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 20, 191, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 270, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 310, 61, 16))
        self.label_4.setObjectName("label_4")
        self.user_choice = QtWidgets.QLabel(Dialog)
        self.user_choice.setGeometry(QtCore.QRect(30, 360, 471, 41))
        self.user_choice.setText("")
        self.user_choice.setObjectName("user_choice")
        self.total = QtWidgets.QLabel(Dialog)
        self.total.setGeometry(QtCore.QRect(20, 430, 221, 31))
        self.total.setText("")
        self.total.setObjectName("total")
        # self.pushButton = QtWidgets.QPushButton(Dialog)
        # self.pushButton.setGeometry(QtCore.QRect(470, 300, 81, 23))
        # self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Hotel Reservation</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>Select date</p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p>Room Type</p><p><br/></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>No of Days</p><p><br/></p></body></html>"))
        # self.pushButton.setText(_translate("Dialog", "calculate rent"))
