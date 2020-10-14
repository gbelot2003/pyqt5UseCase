from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem
from ...views import CuentasUi
from .Operaciones import getGrupos, getTipos, getCuentas

class CuentasController(QMainWindow, CuentasUi):
    def __init__(self, parent=None):    
        super().__init__(parent=parent)
        self.setupUi(self)
        self.initialState()
           
    
    def initialState(self):
        self.setWindowTitle("Cuentas")
        self.loadCmTipos()
        self.loadCmGrupos()
        self.lblCodigo.setText("")
        self.btnCancelar.clicked.connect(self.CloseWindow)
        self.btnIngresar.clicked.connect(self.getValues)    
        self.cmbGrupo.currentTextChanged.connect(self.loadCuentasPadre)
    
    def CloseWindow(self):
        self.close()
        
    def getValues(self):
        print(self.cmbGrupo.currentText())
        print(self.cmbGrupo.currentData())
    
    def loadCmTipos(self):
        tipos = getTipos()
        cuentas = getCuentas()
        for i, tipo in enumerate(tipos):
            self.cmbTipo.addItem(tipo.name, tipo.code)
    
    def loadCmGrupos(self):
        grupos = getGrupos()
        for i, grupo in enumerate(grupos):
            self.cmbGrupo.addItem(grupo.name, grupo.id)
    
    def loadCuentasPadre(self):
        nums = self.cmbGrupo.currentData() - 1
        if nums == 0:
            return None
        print(nums)
