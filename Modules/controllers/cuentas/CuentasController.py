from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem
from ...views import CuentasUi
from .Operaciones import getGrupos, getTipos

class CuentasController(QMainWindow, CuentasUi):
    def __init__(self, parent=None):    
        super().__init__(parent=parent)
        self.setupUi(self)
        
        self.setWindowTitle("Cuentas")
        getGrupos()
        getTipos()