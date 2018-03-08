# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PythonProject\pythonQt\ui\devicebar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeviceBar(object):
    def setupUi(self, DeviceBar):
        DeviceBar.setObjectName("DeviceBar")
        DeviceBar.resize(490, 40)
        self.horizontalLayout = QtWidgets.QHBoxLayout(DeviceBar)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(DeviceBar)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.progressBar = QtWidgets.QProgressBar(DeviceBar)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(DeviceBar)
        QtCore.QMetaObject.connectSlotsByName(DeviceBar)

    def retranslateUi(self, DeviceBar):
        _translate = QtCore.QCoreApplication.translate
        DeviceBar.setWindowTitle(_translate("DeviceBar", "Form"))
        self.checkBox.setText(_translate("DeviceBar", "CheckBox"))

