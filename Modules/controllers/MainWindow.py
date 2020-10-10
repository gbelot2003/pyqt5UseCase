from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from ..views.test import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.txtNombre.setText("texto")
        self.pushButton.clicked.connect(self.changeText)

    def changeText(self):
        self.txtNombre.setText("cambio")
