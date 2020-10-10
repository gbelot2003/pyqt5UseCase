from PyQt5.QtWidgets import QApplication
from Modules.controllers.MainWindow import MainWindow as Main
import sys


def window():
    app = QApplication(sys.argv)
    win = Main()

    win.show()
    sys.exit(app.exec_())


window()
