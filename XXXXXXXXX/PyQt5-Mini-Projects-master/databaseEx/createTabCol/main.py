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
        Dialog.resize(822, 367)
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(160, 80, 201, 31))
        self.name.setObjectName("name")
        self.age = QtWidgets.QLineEdit(Dialog)
        self.age.setGeometry(QtCore.QRect(160, 150, 201, 31))
        self.age.setObjectName("age")
        self.add = QtWidgets.QPushButton(Dialog)
        self.add.setGeometry(QtCore.QRect(10, 330, 75, 23))
        self.add.setObjectName("add")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(26, 90, 111, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 111, 21))
        self.label_2.setObjectName("label_2")
        self.address = QtWidgets.QLineEdit(Dialog)
        self.address.setGeometry(QtCore.QRect(160, 210, 201, 31))
        self.address.setObjectName("address")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 111, 21))
        self.label_3.setObjectName("label_3")
        self.marks = QtWidgets.QLineEdit(Dialog)
        self.marks.setGeometry(QtCore.QRect(160, 260, 201, 31))
        self.marks.setObjectName("marks")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 270, 111, 21))
        self.label_4.setObjectName("label_4")
        self.id = QtWidgets.QLineEdit(Dialog)
        self.id.setGeometry(QtCore.QRect(160, 30, 31, 31))
        self.id.setObjectName("id")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 40, 111, 21))
        self.label_5.setObjectName("label_5")
        self.update = QtWidgets.QPushButton(Dialog)
        self.update.setGeometry(QtCore.QRect(100, 330, 75, 23))
        self.update.setObjectName("update")
        self.delete_2 = QtWidgets.QPushButton(Dialog)
        self.delete_2.setGeometry(QtCore.QRect(190, 330, 75, 23))
        self.delete_2.setObjectName("delete_2")
        self.display = QtWidgets.QPushButton(Dialog)
        self.display.setGeometry(QtCore.QRect(280, 330, 75, 23))
        self.display.setObjectName("display")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(440, 10, 361, 341))
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.add.setText(_translate("Dialog", "Add"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Age"))
        self.label_3.setText(_translate("Dialog", "Address"))
        self.label_4.setText(_translate("Dialog", "Marks"))
        self.label_5.setText(_translate("Dialog", "ID"))
        self.update.setText(_translate("Dialog", "Update"))
        self.delete_2.setText(_translate("Dialog", "Delete"))
        self.display.setText(_translate("Dialog", "Display"))
