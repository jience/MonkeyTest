from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout
from widget.DeviceBarWidget import DeviceBarWidget


class DeviceBarListWidget(QtWidgets.QWidget):
    def __init__(self):
        super(DeviceBarListWidget, self).__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.devicebarlist = []
        self.devicelist = []

        self.deviceBar0 = DeviceBarWidget()
        self.devicebarlist.append(self.deviceBar0)
        self.deviceBar1 = DeviceBarWidget()
        self.devicebarlist.append(self.deviceBar1)
        self.deviceBar2 = DeviceBarWidget()
        self.devicebarlist.append(self.deviceBar2)
        self.deviceBar3 = DeviceBarWidget()
        self.devicebarlist.append(self.deviceBar3)
        self.deviceBar4 = DeviceBarWidget()
        self.devicebarlist.append(self.deviceBar4)
        self.deviceBar5 = DeviceBarWidget()
        self.devicebarlist.append(self.deviceBar5)
        self.deviceBar6 = DeviceBarWidget()
        self.devicebarlist.append(self.deviceBar6)
        self.deviceBar7 = DeviceBarWidget()
        self.devicebarlist.append(self.deviceBar7)

        for i, val in enumerate(self.devicebarlist):
            self.layout.addWidget(val)
            val.setHidden(True)

    def updateList(self, list):
        self.devicelist = list
        devicelen = len(list)

        for i in range(0, devicelen):
            self.devicebarlist[i].setProgress(0)
            self.devicebarlist[i].setChecked(False)

            self.devicebarlist[i].setHidden(False)
            title = list[i].serialno
            if len(title) < 24:
                for j in range(0, 24-len(title)):
                    title = title + " "
            else:
                title = title[0:24]
            self.devicebarlist[i].setTitle(title)

        for i in range(devicelen, len(self.devicebarlist)):
           self.devicebarlist[i].setHidden(True)

    def get_device_setting(self):
        valuelist = []
        for i, val in enumerate(self.devicebarlist):
            value = []
            value.append(val.layout.checkBox.isChecked())
            value.append(self.devicelist[i].serialno)
            value.append(self.devicelist[i].devicename)
            valuelist.append(value)
        return valuelist

    def disable_view(self):
        for i, val in enumerate(self.devicebarlist):
            val.layout.checkBox.setEnabled(False)

    def enable_view(self):
        for i, val in enumerate(self.devicebarlist):
            val.layout.checkBox.setEnabled(True)
