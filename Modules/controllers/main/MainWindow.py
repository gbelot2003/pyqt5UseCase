from PyQt5.QtWidgets import QMainWindow
from ...views import Ui_MainWindow
from ...models import Person, Car
from ...models.model import Session


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.txtNombre.setText("texto")
        self.pushButton.clicked.connect(self.changeText)

    def changeText(self):

        person = Person()
        car = Car()
        session = Session()
        person.name = self.txtNombre.text()
        session.add(person)
        session.commit()
        session.close()
        self.txtNombre.setText("")
