# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 101, 16))
        self.label.setObjectName("label")
        self.add = QtWidgets.QPushButton(Dialog)
        self.add.setGeometry(QtCore.QRect(50, 160, 51, 23))
        self.add.setObjectName("add")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 81, 20))
        self.label_2.setObjectName("label_2")
        self.results = QtWidgets.QLabel(Dialog)
        self.results.setGeometry(QtCore.QRect(40, 230, 301, 31))
        self.results.setText("")
        self.results.setObjectName("results")
        self.subtract = QtWidgets.QPushButton(Dialog)
        self.subtract.setGeometry(QtCore.QRect(140, 160, 51, 23))
        self.subtract.setObjectName("subtract")
        self.multiply = QtWidgets.QPushButton(Dialog)
        self.multiply.setGeometry(QtCore.QRect(230, 160, 51, 23))
        self.multiply.setObjectName("multiply")
        self.divide = QtWidgets.QPushButton(Dialog)
        self.divide.setGeometry(QtCore.QRect(320, 160, 51, 23))
        self.divide.setObjectName("divide")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 90, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "First Num"))
        self.add.setText(_translate("Dialog", "+"))
        self.label_2.setText(_translate("Dialog", "Second Num"))
        self.subtract.setText(_translate("Dialog", "-"))
        self.multiply.setText(_translate("Dialog", "x"))
        self.divide.setText(_translate("Dialog", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

