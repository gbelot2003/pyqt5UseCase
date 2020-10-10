from PyQt5.QtWidgets import QMainWindow
from ...views import Ui_MainWindow
from .Operations import create


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.txtNombre.setText("texto")
        self.pushButton.clicked.connect(self.changeText)

    def changeText(self):
        create(self.txtNombre.text())
        self.txtNombre.setText("")
