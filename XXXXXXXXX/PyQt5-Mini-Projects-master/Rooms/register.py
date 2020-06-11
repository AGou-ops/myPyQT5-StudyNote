# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(411, 304)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 47, 13))
        self.label.setObjectName("label")
        self.regError = QtWidgets.QLabel(Dialog)
        self.regError.setGeometry(QtCore.QRect(40, 190, 211, 31))
        self.regError.setText("")
        self.regError.setObjectName("regError")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 47, 13))
        self.label_2.setObjectName("label_2")
        self.regEmail = QtWidgets.QLineEdit(Dialog)
        self.regEmail.setGeometry(QtCore.QRect(30, 50, 251, 31))
        self.regEmail.setObjectName("regEmail")
        self.regPassword = QtWidgets.QLineEdit(Dialog)
        self.regPassword.setGeometry(QtCore.QRect(30, 130, 251, 31))
        self.regPassword.setObjectName("regPassword")
        self.regButton = QtWidgets.QPushButton(Dialog)
        self.regButton.setGeometry(QtCore.QRect(134, 252, 81, 31))
        self.regButton.setObjectName("regButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Email: "))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.regButton.setText(_translate("Dialog", "Register"))
