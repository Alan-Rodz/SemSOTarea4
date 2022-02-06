import sys
sys.path.insert(1, './class/')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QWidget, QLabel, QPushButton

from ClaseSistemaOperativo import SistemaOperativo

# *********************************************************************************************
sistemaOperativo = SistemaOperativo()

# Palettes - UI - Labels - Buttons - TextEdits - Functions
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # *********************************************************************************************
        # Palettes
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)

        # *********************************************************************************************
        # UI
        MainWindow.setObjectName("MainWiMainWindow")
        MainWindow.resize(1022, 785)
        MainWindow.setWindowTitle("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # =============================================================================================
        # Labels

        self.label_BG = QtWidgets.QLabel(self.centralwidget)
        self.label_BG.setGeometry(QtCore.QRect(0, 0, 1091, 851))
        self.label_BG.setStyleSheet("background-image: url(./imgs/fondoPrincipal.png);")
        self.label_BG.setText("")
        self.label_BG.setObjectName("label_BG")

        self.label_Logo = QtWidgets.QLabel(self.centralwidget)
        self.label_Logo.setGeometry(QtCore.QRect(640, 130, 321, 191))
        self.label_Logo.setStyleSheet("image: url(./imgs/cog.png);")
        self.label_Logo.setText("")
        self.label_Logo.setObjectName("label_Logo")

        self.label_NombrePrograma = QtWidgets.QLabel(self.centralwidget)
        self.label_NombrePrograma.setGeometry(QtCore.QRect(600, 340, 391, 41))
        self.label_NombrePrograma.setText("Simulador de Sistema Operativo")
        self.label_NombrePrograma.setPalette(palette)
        self.label_NombrePrograma.setAlignment(QtCore.Qt.AlignCenter)
        self.label_NombrePrograma.setObjectName("label_NombrePrograma")        

        self.label_loteActual = QtWidgets.QLabel(self.centralwidget)
        self.label_loteActual.setGeometry(QtCore.QRect(30, 70, 81, 21))
        self.label_loteActual.setText("Lote Actual:")
        self.label_loteActual.setPalette(palette)
        self.label_loteActual.setAlignment(QtCore.Qt.AlignCenter)
        self.label_loteActual.setObjectName("label_loteActual")

        self.label_LotesPendientes = QtWidgets.QLabel(self.centralwidget)
        self.label_LotesPendientes.setGeometry(QtCore.QRect(240, 70, 211, 21))
        self.label_LotesPendientes.setPalette(palette)
        self.label_LotesPendientes.setAlignment(QtCore.Qt.AlignCenter)
        self.label_LotesPendientes.setObjectName("label_LotesPendientes")
        self.label_LotesPendientes.setText("Número de Lotes Pendientes: ")
        
        self.label_ProcesoEjecucion = QtWidgets.QLabel(self.centralwidget)
        self.label_ProcesoEjecucion.setGeometry(QtCore.QRect(30, 190, 141, 21))
        self.label_ProcesoEjecucion.setPalette(palette)
        self.label_ProcesoEjecucion.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ProcesoEjecucion.setObjectName("label_ProcesoEjecucion")
        self.label_ProcesoEjecucion.setText("Proceso en ejecución:")

        self.label_ContadorGeneral = QtWidgets.QLabel(self.centralwidget)
        self.label_ContadorGeneral.setGeometry(QtCore.QRect(30, 510, 121, 21))
        self.label_ContadorGeneral.setPalette(palette)
        self.label_ContadorGeneral.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ContadorGeneral.setObjectName("label_ContadorGeneral")
        self.label_ContadorGeneral.setText("Contador General: ")
        
        self.label_ProcesosTerminados = QtWidgets.QLabel(self.centralwidget)
        self.label_ProcesosTerminados.setGeometry(QtCore.QRect(30, 310, 141, 21))
        self.label_ProcesosTerminados.setPalette(palette)
        self.label_ProcesosTerminados.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ProcesosTerminados.setObjectName("label_ProcesosTerminados")
        self.label_ProcesosTerminados.setText("Procesos Terminados:")

        self.label_Mensajes = QtWidgets.QLabel(self.centralwidget)
        self.label_Mensajes.setGeometry(QtCore.QRect(60, 610, 391, 41))
        self.label_Mensajes.setPalette(palette)
        self.label_Mensajes.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Mensajes.setObjectName("label_Mensajes")
        self.label_Mensajes.setText("Aquí se mostrarán mensajes")

        # =============================================================================================
        # Buttons
        self.pbTerminar = QtWidgets.QPushButton(self.centralwidget)
        self.pbTerminar.setEnabled(False)
        self.pbTerminar.setGeometry(QtCore.QRect(600, 700, 391, 41))
        self.pbTerminar.setObjectName("pbTerminar")
        self.pbTerminar.setText("Terminar Programa")
        
        self.pbContinuar = QtWidgets.QPushButton(self.centralwidget)
        self.pbContinuar.setEnabled(False)
        self.pbContinuar.setGeometry(QtCore.QRect(600, 640, 391, 41))
        self.pbContinuar.setObjectName("pbContinuar")# *******************************************************************************************

        self.pbContinuar.setText("Continuar Ejecución del Programa")


        self.pbInterrumpir = QtWidgets.QPushButton(self.centralwidget)
        self.pbInterrumpir.setEnabled(False)
        self.pbInterrumpir.setGeometry(QtCore.QRect(600, 460, 391, 41))
        self.pbInterrumpir.setObjectName("pbInterrumpir")
        self.pbInterrumpir.setText("Interrumpir Proceso Actual")

        self.pbPausar = QtWidgets.QPushButton(self.centralwidget)
        self.pbPausar.setEnabled(False)
        self.pbPausar.setGeometry(QtCore.QRect(600, 580, 391, 41))
        self.pbPausar.setObjectName("pbPausar")
        self.pbPausar.setText("Poner Programa en Pausa")


        self.pbError = QtWidgets.QPushButton(self.centralwidget)
        self.pbError.setEnabled(False)
        self.pbError.setGeometry(QtCore.QRect(600, 520, 391, 41))
        self.pbError.setObjectName("pbError")
        self.pbError.setText("Marcar Error en Proceso")

        self.pushButton_Comenzar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Comenzar.setGeometry(QtCore.QRect(890, 410, 101, 31))
        self.pushButton_Comenzar.setObjectName("pushButton_Comenzar")
        self.pushButton_Comenzar.setText("Comenzar")
        self.pushButton_Comenzar.clicked.connect(self.obtenerCantidadDeProcesos)

        # =============================================================================================
        # TextEdits
        self.textEdit_ProcesoEjecucion = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_ProcesoEjecucion.setEnabled(False)
        self.textEdit_ProcesoEjecucion.setGeometry(QtCore.QRect(30, 220, 421, 61))
        self.textEdit_ProcesoEjecucion.setObjectName("textEdit_ProcesoEjecucion")

        self.textEdit_CantidadProcesos = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_CantidadProcesos.setGeometry(QtCore.QRect(600, 410, 281, 31))
        self.textEdit_CantidadProcesos.setUndoRedoEnabled(False)
        self.textEdit_CantidadProcesos.setObjectName("textEdit_CantidadProcesos")
        self.textEdit_CantidadProcesos.setPlaceholderText("Ingresa la cantidad de procesos...")

        self.textEdit_LoteActual = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_LoteActual.setEnabled(False)
        self.textEdit_LoteActual.setGeometry(QtCore.QRect(30, 100, 421, 61))
        self.textEdit_LoteActual.setObjectName("textEdit_LoteActual")

        self.textEdit_ProcesosTerminados = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_ProcesosTerminados.setEnabled(False)
        self.textEdit_ProcesosTerminados.setGeometry(QtCore.QRect(30, 340, 421, 151))
        self.textEdit_ProcesosTerminados.setObjectName("textEdit_ProcesosTerminados")

        # ---------------------------------------------------------------------------------------------
        # Setup
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # =============================================================================================
    # Functions
    def obtenerCantidadDeProcesos(self):
        cantidadProcesos = self.textEdit_CantidadProcesos.toPlainText()
        if (not cantidadProcesos.isnumeric()):
            self.label_Mensajes.setText("Ingresa un número válido")
        elif (int(cantidadProcesos) < 0):
            self.label_Mensajes.setText("Ingresa un número válido")
        else:
            self.label_Mensajes.setText("El número de procesos ingresado es válido")
            sistemaOperativo.setCantidadProcesos(int(cantidadProcesos))
            sistemaOperativo.generarProcesosAleatoriamente()
            sistemaOperativo.imprimirInformacionDiagnostica()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(1025, 775)
    window.show()
    sys.exit(app.exec_())
