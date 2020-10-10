#!/usr/bin/python

from PyQt5.QtWidgets import QApplication
from Modules.controllers import MainWindow
import sys
from Modules.models import Person


def Database():
    person = Person()
    person.SessionTest()


def window():
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show()
    sys.exit(app.exec_())


Database()
window()
