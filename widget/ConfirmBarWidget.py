from PyQt5 import QtWidgets
from ui.ConfirmBar import Ui_Confirm


class ConfirmBarWidget(QtWidgets.QWidget):
    def __init__(self):
        super(ConfirmBarWidget, self).__init__()
        self.layout = Ui_Confirm()
        self.layout.setupUi(self)

    def disable_view(self):
        self.layout.btn_scan.setEnabled(False)
        self.layout.btn_start.setEnabled(False)

    def enable_view(self):
        self.layout.btn_scan.setEnabled(True)
        self.layout.btn_start.setEnabled(True)
