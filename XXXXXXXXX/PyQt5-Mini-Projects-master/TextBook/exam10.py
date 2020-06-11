# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Example10.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(573, 516)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 460, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(210, 50, 161, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.namePrompt = QtWidgets.QLabel(Dialog)
        self.namePrompt.setGeometry(QtCore.QRect(20, 50, 91, 16))
        self.namePrompt.setObjectName("namePrompt")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 110, 71, 16))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 100, 161, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(290, 310, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 170, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 71, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 160, 61, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 210, 61, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.total = QtWidgets.QLabel(Dialog)
        self.total.setGeometry(QtCore.QRect(30, 310, 71, 16))
        self.total.setObjectName("total")
        self.percent = QtWidgets.QLabel(Dialog)
        self.percent.setGeometry(QtCore.QRect(30, 340, 71, 16))
        self.percent.setObjectName("percent")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Submit"))
        self.namePrompt.setText(_translate("Dialog", "Enter a name"))
        self.label.setText(_translate("Dialog", "Enter Gender"))
        self.label_2.setText(_translate("Dialog", "History"))
        self.label_3.setText(_translate("Dialog", "Geography"))
        self.total.setText(_translate("Dialog", "Total"))
        self.percent.setText(_translate("Dialog", "Percentage"))

