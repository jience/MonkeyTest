from PyQt5 import QtWidgets
from widget.MainWidget import MainWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWidget()
    mainwindow.resize(500, 240)
    mainwindow.show()
    sys.exit(app.exec_())
