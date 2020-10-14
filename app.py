#!/usr/bin/python

from PyQt5.QtWidgets import QApplication
from Modules.controllers import MainWindow
from Modules.controllers import CuentasController
import sys


def window():
    app = QApplication(sys.argv)
    win = CuentasController()

    win.show()
    sys.exit(app.exec_())


window()
