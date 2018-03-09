import threading
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout
from adb.adbdevice import adbdevice
from presenter.MonkeyTest import MonkeyTest
from widget.ConfirmBarWidget import ConfirmBarWidget
from widget.DeviceBarListWidget import DeviceBarListWidget
from widget.SettingWidget import SettingWidget


class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__()
        self.setWindowTitle("MonkeyTest")
        self.reflushview()
        self.monkeythreadlistflag = []

    def reflushview(self):
        self.slayout = QGridLayout()

        self.settingWidget = SettingWidget()
        self.confirmWidget = ConfirmBarWidget()
        self.deviceBarListWidget = DeviceBarListWidget()

        self.slayout.addWidget(self.settingWidget)
        self.slayout.addWidget(self.confirmWidget)
        self.slayout.addWidget(self.deviceBarListWidget)
        self.setLayout(self.slayout)

        self.confirmWidget.layout.btn_scan.clicked.connect(self.scan_device)
        self.confirmWidget.layout.btn_start.clicked.connect(self.start_test)

    def scan_device(self):
        self.devicebar = []
        androiddevice = adbdevice()
        androiddevice.get_devices()
        list = androiddevice.devicelist

        self.deviceBarListWidget.updateList(list)

    def start_test(self):
        self.disable_view()
        monkeytestlist = []
        self.settingWidget.get_settings()
        print("cmdcell：", self.settingWidget.cmdcell)
        print("testTimes：", self.settingWidget.testTimes)
        print("testApplicationPath：", self.settingWidget.testApplicationPath)
        print("installApp：", self.settingWidget.installApp)
        print("uninstallApp：", self.settingWidget.uninstallApp)

        for i, val in enumerate(self.deviceBarListWidget.devicebarlist):
            if val.layout.checkBox.isChecked():
                print("serialno", self.deviceBarListWidget.devicelist[i].serialno)
                print("devicename", self.deviceBarListWidget.devicelist[i].devicename)

                devicebar = self.deviceBarListWidget.devicebarlist[i]
                monkeytest = MonkeyTest(self, devicebar,
                                        self.deviceBarListWidget.devicelist[i].devicename,
                                        self.deviceBarListWidget.devicelist[i].serialno,
                                        self.settingWidget.testTimes,
                                        self.settingWidget.testApplicationPath,
                                        self.settingWidget.testPackage,
                                        self.settingWidget.installApp,
                                        self.settingWidget.uninstallApp)
                monkeytestlist.append(monkeytest)

        self.monkeythreadlistflag = []
        for i, monkeytest in enumerate(monkeytestlist):
            monkeyt =threading.Thread(target=monkeytest.startMonkeyTest,
                    args = (self, i, self.settingWidget.cmdcell, self.settingWidget.testPackage))
            monkeyt.setDaemon(True)
            monkeyt.start()
            self.monkeythreadlistflag.append(True)

    def enable_view(self):
        self.settingWidget.enable_view()
        self.deviceBarListWidget.enable_view()
        self.confirmWidget.enable_view()

    def disable_view(self):
        self.settingWidget.disable_view()
        self.deviceBarListWidget.disable_view()
        self.confirmWidget.disable_view()

    def onResult(self, id):
        self.monkeythreadlistflag[id] = False
        for value in self.monkeythreadlistflag:
            if value:
                return
        self.enable_view()
