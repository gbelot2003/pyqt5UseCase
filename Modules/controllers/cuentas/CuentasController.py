from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem
from ...views import CuentasUi
from .Operaciones import getGrupos, getTipos

class CuentasController(QMainWindow, CuentasUi):
    def __init__(self, parent=None):    
        super().__init__(parent=parent)
        self.setupUi(self)
        
        self.setWindowTitle("Cuentas")
        self.loadCmTipos()
        self.loadCmGrupos()
    
    def loadCmTipos(self):
        tipos = getTipos()
        for i, tipo in enumerate(tipos):
            self.cmbTipo.addItem(tipo.name)
    
    def loadCmGrupos(self):
        grupos = getGrupos()
        for i, grupo in enumerate(grupos):
            self.cmbGrupo.addItem(grupo.name)