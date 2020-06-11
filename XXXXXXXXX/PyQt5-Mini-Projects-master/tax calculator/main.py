# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.tax_rate = QtWidgets.QSpinBox(Form)
        self.tax_rate.setGeometry(QtCore.QRect(150, 110, 42, 22))
        self.tax_rate.setProperty("value", 5)
        self.tax_rate.setObjectName("tax_rate")
        self.Button = QtWidgets.QPushButton(Form)
        self.Button.setGeometry(QtCore.QRect(140, 160, 75, 23))
        self.Button.setObjectName("Button")
        self.tax_results = QtWidgets.QTextEdit(Form)
        self.tax_results.setGeometry(QtCore.QRect(130, 190, 104, 71))
        self.tax_results.setObjectName("tax_results")
        self.price_input = QtWidgets.QPlainTextEdit(Form)
        self.price_input.setGeometry(QtCore.QRect(130, 20, 104, 71))
        self.price_input.setObjectName("price_input")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Button.setText(_translate("Form", "PushButton"))

