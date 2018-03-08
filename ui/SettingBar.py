# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PythonProject\pythonQt\ui\settingbar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(550, 176)
        self.gridLayout = QtWidgets.QGridLayout(Setting)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Setting)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.edit_div = QtWidgets.QLineEdit(Setting)
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.edit_div.setFont(font)
        self.edit_div.setObjectName("edit_div")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_div)
        self.label_2 = QtWidgets.QLabel(Setting)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.edit_times = QtWidgets.QLineEdit(Setting)
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.edit_times.setFont(font)
        self.edit_times.setObjectName("edit_times")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.edit_times)
        self.text = QtWidgets.QLabel(Setting)
        self.text.setObjectName("text")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.text)
        self.btn_app = QtWidgets.QPushButton(Setting)
        self.btn_app.setEnabled(True)
        self.btn_app.setObjectName("btn_app")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.btn_app)
        self.textEdit_packagename = QtWidgets.QLineEdit(Setting)
        self.textEdit_packagename.setObjectName("textEdit_packagename")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textEdit_packagename)
        self.textEdit_apppath = QtWidgets.QLineEdit(Setting)
        self.textEdit_apppath.setEnabled(False)
        self.textEdit_apppath.setObjectName("textEdit_apppath")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.textEdit_apppath)
        self.checkBox_install = QtWidgets.QCheckBox(Setting)
        self.checkBox_install.setObjectName("checkBox_install")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.checkBox_install)
        self.checkBox_uninstall = QtWidgets.QCheckBox(Setting)
        self.checkBox_uninstall.setObjectName("checkBox_uninstall")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.checkBox_uninstall)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "Form"))
        self.label.setText(_translate("Setting", " Test Gap(ms):"))
        self.label_2.setText(_translate("Setting", " Test Times:    "))
        self.text.setText(_translate("Setting", " Package Name:"))
        self.btn_app.setText(_translate("Setting", "Choose App:"))
        self.checkBox_install.setText(_translate("Setting", "install app"))
        self.checkBox_uninstall.setText(_translate("Setting", "uninstall app"))

