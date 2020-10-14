from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem
from ...views import CuentasUi
from .Operaciones import getGrupos, getTipos, getCuentas, getCuentasByType

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
        self.cmbCuenta.setEnabled(False)
    
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
            self.cmbCuenta.setEnabled(False)
            self.cmbCuenta.clear()
            return None
        result = getCuentasByType(nums)
        self.cmbCuenta.setEnabled(True)
        self.cmbCuenta.clear()
        for row in result:
            name = row.code + " " + row.descripcion
            self.cmbCuenta.addItem(name, row.id)
            print ("ID:", row.id, "descripcion: ",row.descripcion)
