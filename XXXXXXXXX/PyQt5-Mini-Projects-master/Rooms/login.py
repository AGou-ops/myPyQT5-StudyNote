# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, DialogL):
        DialogL.setObjectName("Dialog")
        DialogL.resize(430, 317)
        self.label = QtWidgets.QLabel(DialogL)
        self.label.setGeometry(QtCore.QRect(30, 30, 47, 13))
        self.label.setObjectName("label")
        self.logEmail = QtWidgets.QLineEdit(DialogL)
        self.logEmail.setGeometry(QtCore.QRect(30, 60, 251, 31))
        self.logEmail.setObjectName("logEmail")
        self.logError = QtWidgets.QLabel(DialogL)
        self.logError.setGeometry(QtCore.QRect(40, 200, 211, 31))
        self.logError.setText("")
        self.logError.setObjectName("logError")
        self.label_2 = QtWidgets.QLabel(DialogL)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 47, 13))
        self.label_2.setObjectName("label_2")
        self.logPassword = QtWidgets.QLineEdit(DialogL)
        self.logPassword.setGeometry(QtCore.QRect(30, 140, 251, 31))
        self.logPassword.setObjectName("logPassword")
        self.logButton = QtWidgets.QPushButton(DialogL)
        self.logButton.setGeometry(QtCore.QRect(180, 270, 75, 23))
        self.logButton.setObjectName("logButton")
        self.logButton_2 = QtWidgets.QPushButton(DialogL)
        self.logButton_2.setGeometry(QtCore.QRect(300, 30, 111, 23))
        self.logButton_2.setObjectName("logButton_2")

        self.retranslateUi(DialogL)
        QtCore.QMetaObject.connectSlotsByName(DialogL)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Email: "))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.logButton.setText(_translate("Dialog", "Login"))
        self.logButton_2.setText(_translate("Dialog", "Register Here"))
