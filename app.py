#!/usr/bin/python

from PyQt5.QtWidgets import QApplication
from Modules.controllers import MainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show()
    sys.exit(app.exec_())


window()
