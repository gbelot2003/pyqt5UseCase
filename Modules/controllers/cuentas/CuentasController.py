from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5 import QtCore, QtWidgets
from ...views import CuentasUi
from .Operaciones import getGrupos, getTipos, getCuentas, getCuentasByGroup, record, getCuentasById, getCuentasByGroupAndType, getCount


class CuentasController(QMainWindow, CuentasUi):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.txtCuenta.installEventFilter(self)
        self.initialState()
        self.loadTextView()

    def initialState(self):
        self.setWindowTitle("Cuentas")
        self.loadCmTipos()
        self.loadCmGrupos()
        self.lblCodigo.setText("")
        self.btnCancelar.clicked.connect(self.CloseWindow)
        self.btnIngresar.clicked.connect(self.saveData)
        self.cmbGrupo.currentTextChanged.connect(self.loadCuentasPadre)
        self.cmbTipo.currentTextChanged.connect(self.loadCuentasPadre)
        self.cmbCuenta.setEnabled(False)

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.FocusOut and
                source is self.txtCuenta):
            tipo_id = str(self.cmbTipo.currentData())
            parent_id = self.cmbCuenta.currentData()
            cuenta = str(self.txtCuenta.text())
            self.getCode(tipo_id, parent_id, cuenta)
        return super(CuentasController, self).eventFilter(source, event)

    def CloseWindow(self):
        self.close()

    def loadCmTipos(self):
        tipos = getTipos()
        for i, tipo in enumerate(tipos):
            self.cmbTipo.addItem(tipo.name, tipo.code)

    def loadCmGrupos(self):
        grupos = getGrupos()
        for i, grupo in enumerate(grupos):
            self.cmbGrupo.addItem(grupo.name, grupo.id)

    def loadCuentasPadre(self):
        nums = self.cmbGrupo.currentData() - 1
        tipo = self.cmbTipo.currentData()
        if nums == 0:
            self.cmbCuenta.setEnabled(False)
            self.cmbCuenta.clear()
            return None
        result = getCuentasByGroupAndType(nums, tipo)
        self.cmbCuenta.setEnabled(True)
        self.cmbCuenta.clear()
        for row in result:
            name = row.code + " " + row.descripcion
            self.cmbCuenta.addItem(name, row.id)

    def loadTextView(self):
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setRowCount(getCount())
        cuentas = getCuentas()
        for i, cuenta in enumerate(cuentas):
            self.tableWidget.setItem(
                i, 0, QTableWidgetItem(cuenta.code))
            self.tableWidget.setItem(
                i, 1, QTableWidgetItem(cuenta.descripcion))
            self.tableWidget.setItem(
                i, 2, QTableWidgetItem(str(cuenta.grupo_id)))

    def clearFields(self):
        self.txtDescripcion.setText("")
        self.txtCuenta.setText("")
        self.lblCodigo.setText("")

    def saveData(self):
        tipo_id = self.cmbTipo.currentData()
        grupo_id = self.cmbGrupo.currentData()
        cuenta = self.txtCuenta.text()
        parent_id = self.cmbCuenta.currentData()
        codigo = self.lblCodigo.text()
        descripcion = str(self.txtDescripcion.text())
        record(tipo_id, grupo_id, cuenta, parent_id, codigo, descripcion)
        self.loadTextView()
        self.clearFields()

    def getCode(self, tipo, parent, cuenta):
        if (self.cmbGrupo.currentData() != 1):
            codi = getCuentasById(parent)
            dCuenta = codi.code + "-" + str(cuenta)
            self.lblCodigo.setText(dCuenta)

        else:
            dCuenta = str(tipo) + str(cuenta)
            self.lblCodigo.setText(dCuenta)
