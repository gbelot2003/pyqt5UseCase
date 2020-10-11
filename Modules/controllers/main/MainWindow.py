from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem
from ...views import Ui_MainWindow
from .Operations import create, Count, GetAll


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.loadTable()
        self.txtNombre.setText("texto")
        self.pushButton.clicked.connect(self.changeText)

    def changeText(self):
        create(self.txtNombre.text())
        self.txtNombre.setText("")
        self.loadTable()

    def openCars(self):
        print('cars')

    def loadTable(self):
        self.tableWidget.setRowCount(Count())
        persons = GetAll()

        for i, person in enumerate(persons):
            self.tableWidget.setItem(
                i, 0, QTableWidgetItem(person.name))

        #self.tableWidget.move(0, 0)
