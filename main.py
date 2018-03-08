from PyQt5 import QtWidgets
import sys
from widget.MainWidget import MainWidget


def mainwindows():
    app = QtWidgets.QApplication(sys.argv)
    mainshow = MainWidget()
    mainshow.setFixedWidth(500)
    # mainshow.resize(500,240)
    mainshow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    mainwindows()
