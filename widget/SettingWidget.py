import os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from application.applocation import get_app_packagename
from ui.SettingBar import Ui_Setting


class SettingWidget(QtWidgets.QWidget):
    def __init__(self):
        super(SettingWidget,self).__init__()
        self.layout = Ui_Setting()
        self.layout.setupUi(self)

        self.layout.edit_times.setValidator(QIntValidator(0, 10000*10000))
        self.layout.edit_div.setValidator(QIntValidator(0, 10000*10000))
        self.layout.edit_times.setText("500")
        self.layout.edit_div.setText("300")

        self.layout.btn_app.clicked.connect(self.chooseapp)


    def chooseapp(self):
        filename,selectedFilter = QFileDialog.getOpenFileName(self,("Choose App"),None)
        if filename==None or  filename=="":
            return
        self.layout.textEdit_apppath.setText(filename)
        try:
            packagename = get_app_packagename(filename)
            if packagename == None:
                self.apk_error_dialog()
            else:
                self.layout.textEdit_packagename.setText(packagename)
        except Exception as e:
            self.apk_error_dialog()
        finally:
            print("")

    def apk_error_dialog(self):
        self.layout.textEdit_apppath.setText("")
        QMessageBox.information(self,("Warning"),("""Apk cannot be resolved"""),
                     QMessageBox.StandardButtons(QMessageBox.Yes))

    def get_settings(self):
        self.testTimes = self.layout.edit_times.text()
        self.testDiv = self.layout.edit_div.text()
        self.testPackage = self.layout.textEdit_packagename.text()
        self.testApplicationPath = self.layout.textEdit_apppath.text()
        self.installApp = self.layout.checkBox_install.isChecked()
        self.uninstallApp = self.layout.checkBox_uninstall.isChecked()

        if self.testTimes==None or self.testTimes=="":
            self.testTimes=500

        if self.testDiv==None or self.testDiv=="":
            self.testDiv=300

        if not os.path.exists('./log'):
            os.makedirs('./log')

        self.cmdcell = ""
        self.cmdcell = self.cmdcell + "  --throttle " + self.testDiv + " -v -v -v " + self.testTimes + " --ignore-crashes --ignore-timeouts"

    def disable_view(self):
        self.layout.edit_times.setEnabled(False)
        self.layout.edit_div.setEnabled(False)
        self.layout.textEdit_packagename.setEnabled(False)
        self.layout.btn_app.setEnabled(False)
        self.layout.checkBox_install.setEnabled(False)
        self.layout.checkBox_uninstall.setEnabled(False)

    def enable_view(self):
        self.layout.edit_times.setEnabled(True)
        self.layout.edit_div.setEnabled(True)
        self.layout.textEdit_packagename.setEnabled(True)
        self.layout.btn_app.setEnabled(True)
        self.layout.checkBox_install.setEnabled(True)
        self.layout.checkBox_uninstall.setEnabled(True)

