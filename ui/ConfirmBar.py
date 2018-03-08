# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PythonProject\pythonQt\ui\confirmbar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Confirm(object):
    def setupUi(self, Confirm):
        Confirm.setObjectName("Confirm")
        Confirm.resize(500, 43)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Confirm)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Confirm)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Confirm)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(Confirm)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.btn_scan = QtWidgets.QPushButton(Confirm)
        self.btn_scan.setObjectName("btn_scan")
        self.horizontalLayout.addWidget(self.btn_scan)
        self.btn_start = QtWidgets.QPushButton(Confirm)
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout.addWidget(self.btn_start)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Confirm)
        QtCore.QMetaObject.connectSlotsByName(Confirm)

    def retranslateUi(self, Confirm):
        _translate = QtCore.QCoreApplication.translate
        Confirm.setWindowTitle(_translate("Confirm", "Form"))
        self.btn_scan.setText(_translate("Confirm", "scan"))
        self.btn_start.setText(_translate("Confirm", "start"))

