
from PyQt5 import QtWidgets
from ui.DeviceBar import Ui_DeviceBar

class DeviceBarWidget(QtWidgets.QWidget):
    def __init__(self):
        super(DeviceBarWidget,self).__init__()
        self.layout = Ui_DeviceBar()
        self.layout.setupUi(self)

    def setTitle(self,title):
        self.layout.checkBox.setText(title)

    def setProgressMax(self,max):
        self.layout.progressBar.setMaximum(max)

    def setProgress(self,value):
        self.layout.progressBar.setValue(value)

    def setChecked(self,checked):
        self.layout.checkBox.setChecked(checked)
