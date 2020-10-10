from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from ...views import Ui_MainWindow
from ...models import Person
from ...models.model import Base, engine
from sqlalchemy.orm import sessionmaker


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.txtNombre.setText("texto")
        self.pushButton.clicked.connect(self.changeText)

    def changeText(self):
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        person = Person()
        person.name = self.txtNombre.text()
        session.add(person)
        session.commit()
        session.close()
        self.txtNombre.setText("")
