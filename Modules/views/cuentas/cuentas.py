# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cuentas.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 740)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 771, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.Formulario = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.Formulario.setObjectName("Formulario")
        self.btnIngresar = QtWidgets.QPushButton(self.Formulario)
        self.btnIngresar.setGeometry(QtCore.QRect(20, 140, 75, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.btnIngresar.setPalette(palette)
        self.btnIngresar.setCheckable(False)
        self.btnIngresar.setFlat(False)
        self.btnIngresar.setObjectName("btnIngresar")
        self.btnCancelar = QtWidgets.QPushButton(self.Formulario)
        self.btnCancelar.setGeometry(QtCore.QRect(100, 140, 75, 31))
        self.btnCancelar.setObjectName("btnCancelar")
        self.txtCuenta = QtWidgets.QLineEdit(self.Formulario)
        self.txtCuenta.setGeometry(QtCore.QRect(492, 91, 133, 31))
        self.txtCuenta.setObjectName("txtCuenta")
        self.label = QtWidgets.QLabel(self.Formulario)
        self.label.setGeometry(QtCore.QRect(490, 70, 61, 16))
        self.label.setObjectName("label")
        self.txtDescripcion = QtWidgets.QLineEdit(self.Formulario)
        self.txtDescripcion.setGeometry(QtCore.QRect(12, 91, 471, 31))
        self.txtDescripcion.setObjectName("txtDescripcion")
        self.label_2 = QtWidgets.QLabel(self.Formulario)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 61, 16))
        self.label_2.setObjectName("label_2")
        self.cmbGrupo = QtWidgets.QComboBox(self.Formulario)
        self.cmbGrupo.setGeometry(QtCore.QRect(11, 36, 141, 22))
        self.cmbGrupo.setObjectName("cmbGrupo")
        self.label_3 = QtWidgets.QLabel(self.Formulario)
        self.label_3.setGeometry(QtCore.QRect(16, 16, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Formulario)
        self.label_4.setGeometry(QtCore.QRect(162, 16, 61, 16))
        self.label_4.setObjectName("label_4")
        self.cmbTipo = QtWidgets.QComboBox(self.Formulario)
        self.cmbTipo.setGeometry(QtCore.QRect(160, 36, 191, 22))
        self.cmbTipo.setObjectName("cmbTipo")
        self.label_5 = QtWidgets.QLabel(self.Formulario)
        self.label_5.setGeometry(QtCore.QRect(360, 16, 81, 16))
        self.label_5.setObjectName("label_5")
        self.cmbCuenta = QtWidgets.QComboBox(self.Formulario)
        self.cmbCuenta.setGeometry(QtCore.QRect(359, 35, 141, 22))
        self.cmbCuenta.setObjectName("cmbCuenta")
        self.lblCodigo = QtWidgets.QLabel(self.Formulario)
        self.lblCodigo.setGeometry(QtCore.QRect(570, 13, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lblCodigo.setFont(font)
        self.lblCodigo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblCodigo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblCodigo.setObjectName("lblCodigo")
        self.gridLayout.addWidget(self.Formulario, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(13, 200, 761, 491))
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setKerning(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cmbGrupo, self.cmbTipo)
        MainWindow.setTabOrder(self.cmbTipo, self.cmbCuenta)
        MainWindow.setTabOrder(self.cmbCuenta, self.txtDescripcion)
        MainWindow.setTabOrder(self.txtDescripcion, self.txtCuenta)
        MainWindow.setTabOrder(self.txtCuenta, self.btnIngresar)
        MainWindow.setTabOrder(self.btnIngresar, self.btnCancelar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Formulario.setTitle(_translate("MainWindow", "Formulario"))
        self.btnIngresar.setText(_translate("MainWindow", "Guardar"))
        self.btnCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.label.setText(_translate("MainWindow", "No Cuenta"))
        self.label_2.setText(_translate("MainWindow", "Descripcion"))
        self.label_3.setText(_translate("MainWindow", "Grupo"))
        self.label_4.setText(_translate("MainWindow", "Tipo"))
        self.label_5.setText(_translate("MainWindow", "Cuenta Padre"))
        self.lblCodigo.setText(_translate("MainWindow", "TextLabel"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Codigo"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Descripcion"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tipo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
