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
        Dialog.resize(584, 511)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 30, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 51, 16))
        self.label_2.setObjectName("label_2")
        self.brisk = QtWidgets.QCheckBox(Dialog)
        self.brisk.setGeometry(QtCore.QRect(370, 110, 70, 17))
        self.brisk.setObjectName("brisk")
        self.appertizers = QtWidgets.QButtonGroup(Dialog)
        self.appertizers.setObjectName("appertizers")
        self.appertizers.addButton(self.brisk)
        self.stoup = QtWidgets.QCheckBox(Dialog)
        self.stoup.setGeometry(QtCore.QRect(370, 140, 70, 17))
        self.stoup.setObjectName("stoup")
        self.appertizers.addButton(self.stoup)
        self.rochin = QtWidgets.QCheckBox(Dialog)
        self.rochin.setGeometry(QtCore.QRect(370, 170, 70, 17))
        self.rochin.setObjectName("rochin")
        self.appertizers.addButton(self.rochin)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 240, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 350, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 450, 47, 13))
        self.label_5.setObjectName("label_5")
        self.chicken = QtWidgets.QCheckBox(Dialog)
        self.chicken.setGeometry(QtCore.QRect(370, 240, 211, 17))
        self.chicken.setObjectName("chicken")
        self.main = QtWidgets.QButtonGroup(Dialog)
        self.main.setObjectName("main")
        self.main.addButton(self.chicken)
        self.rice = QtWidgets.QCheckBox(Dialog)
        self.rice.setGeometry(QtCore.QRect(370, 270, 141, 17))
        self.rice.setObjectName("rice")
        self.main.addButton(self.rice)
        self.potato = QtWidgets.QCheckBox(Dialog)
        self.potato.setGeometry(QtCore.QRect(370, 300, 161, 17))
        self.potato.setObjectName("potato")
        self.main.addButton(self.potato)
        self.cake = QtWidgets.QCheckBox(Dialog)
        self.cake.setGeometry(QtCore.QRect(370, 350, 70, 17))
        self.cake.setObjectName("cake")
        self.Dessert = QtWidgets.QButtonGroup(Dialog)
        self.Dessert.setObjectName("Dessert")
        self.Dessert.addButton(self.cake)
        self.ice_cream = QtWidgets.QCheckBox(Dialog)
        self.ice_cream.setGeometry(QtCore.QRect(370, 380, 91, 17))
        self.ice_cream.setObjectName("ice_cream")
        self.Dessert.addButton(self.ice_cream)
        self.pie = QtWidgets.QCheckBox(Dialog)
        self.pie.setGeometry(QtCore.QRect(370, 410, 70, 17))
        self.pie.setObjectName("pie")
        self.Dessert.addButton(self.pie)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Menu</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Appertizer"))
        self.brisk.setText(_translate("Dialog", "$12 brisk"))
        self.stoup.setText(_translate("Dialog", "$10 stoup"))
        self.rochin.setText(_translate("Dialog", "$11 rochin"))
        self.label_3.setText(_translate("Dialog", "Main Course"))
        self.label_4.setText(_translate("Dialog", "Dessert"))
        self.label_5.setText(_translate("Dialog", "Bill: "))
        self.chicken.setText(_translate("Dialog", "$32 Chicken soup with plantain freckles"))
        self.rice.setText(_translate("Dialog", "$26 Fried rice and Brisket"))
        self.potato.setText(_translate("Dialog", "$20 Potatoe soup and steak"))
        self.cake.setText(_translate("Dialog", "$5 Cake"))
        self.ice_cream.setText(_translate("Dialog", "$6 Ice Cream"))
        self.pie.setText(_translate("Dialog", "$5 Pie"))
