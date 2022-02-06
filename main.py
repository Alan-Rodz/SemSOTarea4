import sys
sys.path.insert(1, './class/')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QObject, pyqtSignal, QThreadPool
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QWidget, QLabel, QPushButton
import random
import time

from ClaseOSRunner import RunnerSistemaOperativo

# *********************************************************************************************

# Palettes - UI - Labels - Buttons - TextEdits - Functions
class Ui_MainWindow(object):

    # =============================================================================================
    # Signals Setup
    pausar = pyqtSignal() 
    reanudar = pyqtSignal()
    terminar = pyqtSignal()   
    interrumpirProceso = pyqtSignal()
    marcarErrorProceso = pyqtSignal()

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
        MainWindow.setObjectName('MainWiMainWindow')
        MainWindow.resize(1022, 785)
        MainWindow.setWindowTitle('MainWindow')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')

        # =============================================================================================
        # Labels
        self.label_BG = QtWidgets.QLabel(self.centralwidget)
        self.label_BG.setGeometry(QtCore.QRect(0, 0, 1091, 851))
        self.label_BG.setStyleSheet('background-image: url(./imgs/fondoPrincipal.png);')
        self.label_BG.setText('')
        self.label_BG.setObjectName('label_BG')

        self.label_Logo = QtWidgets.QLabel(self.centralwidget)
        self.label_Logo.setGeometry(QtCore.QRect(630, 20, 321, 191))
        self.label_Logo.setStyleSheet('image: url(./imgs/cog.png);')
        self.label_Logo.setText('')
        self.label_Logo.setObjectName('label_Logo')

        self.label_NombrePrograma = QtWidgets.QLabel(self.centralwidget)
        self.label_NombrePrograma.setGeometry(QtCore.QRect(600, 240, 391, 41))
        self.label_NombrePrograma.setPalette(palette)
        self.label_NombrePrograma.setAlignment(QtCore.Qt.AlignCenter)
        self.label_NombrePrograma.setObjectName('label_NombrePrograma')
        self.label_NombrePrograma.setText('Simulador de Sistema Operativo')

        self.label_loteActual = QtWidgets.QLabel(self.centralwidget)
        self.label_loteActual.setGeometry(QtCore.QRect(30, 70, 81, 21))
        self.label_loteActual.setText('Lote Actual:')
        self.label_loteActual.setPalette(palette)
        self.label_loteActual.setAlignment(QtCore.Qt.AlignCenter)
        self.label_loteActual.setObjectName('label_loteActual')

        self.label_LotesPendientes = QtWidgets.QLabel(self.centralwidget)
        self.label_LotesPendientes.setGeometry(QtCore.QRect(240, 70, 211, 21))
        self.label_LotesPendientes.setPalette(palette)
        self.label_LotesPendientes.setAlignment(QtCore.Qt.AlignCenter)
        self.label_LotesPendientes.setObjectName('label_LotesPendientes')
        self.label_LotesPendientes.setText('Número de Lotes Pendientes: ')
        
        self.label_ProcesoEjecucion = QtWidgets.QLabel(self.centralwidget)
        self.label_ProcesoEjecucion.setGeometry(QtCore.QRect(30, 190, 141, 21))
        self.label_ProcesoEjecucion.setPalette(palette)
        self.label_ProcesoEjecucion.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ProcesoEjecucion.setObjectName('label_ProcesoEjecucion')
        self.label_ProcesoEjecucion.setText('Proceso en ejecución:')

        self.label_ContadorGeneral = QtWidgets.QLabel(self.centralwidget)
        self.label_ContadorGeneral.setGeometry(QtCore.QRect(30, 510, 141, 21))
        self.label_ContadorGeneral.setPalette(palette)
        self.label_ContadorGeneral.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ContadorGeneral.setObjectName('label_ContadorGeneral')
        self.label_ContadorGeneral.setText('Contador General: ')
        
        self.label_ProcesosTerminados = QtWidgets.QLabel(self.centralwidget)
        self.label_ProcesosTerminados.setGeometry(QtCore.QRect(30, 310, 141, 21))
        self.label_ProcesosTerminados.setPalette(palette)
        self.label_ProcesosTerminados.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ProcesosTerminados.setObjectName('label_ProcesosTerminados')
        self.label_ProcesosTerminados.setText('Procesos Terminados:')

        self.label_Mensajes = QtWidgets.QLabel(self.centralwidget)
        self.label_Mensajes.setGeometry(QtCore.QRect(60, 610, 391, 41))
        self.label_Mensajes.setPalette(palette)
        self.label_Mensajes.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Mensajes.setObjectName('label_Mensajes')
        self.label_Mensajes.setText('Aquí se mostrarán mensajes')

        self.label_Estado = QtWidgets.QLabel(self.centralwidget)
        self.label_Estado.setGeometry(QtCore.QRect(30, 30, 331, 31))
        self.label_Estado.setPalette(palette)
        self.label_Estado.setObjectName('label_Estado')
        self.label_Estado.setText('Estado: Inicial')

        # =============================================================================================
        # Buttons
        self.pbTerminar = QtWidgets.QPushButton(self.centralwidget)
        self.pbTerminar.setEnabled(False)
        self.pbTerminar.setGeometry(QtCore.QRect(600, 700, 391, 41))
        self.pbTerminar.setObjectName('pbTerminar')
        self.pbTerminar.setText('Terminar Programa')
        self.pbTerminar.clicked.connect(self.handleTerminar)
        
        self.pbContinuar = QtWidgets.QPushButton(self.centralwidget)
        self.pbContinuar.setEnabled(False)
        self.pbContinuar.setGeometry(QtCore.QRect(600, 640, 391, 41))
        self.pbContinuar.setObjectName('pbContinuar')
        self.pbContinuar.setText('Continuar Ejecución del Programa')
        self.pbContinuar.clicked.connect(self.handleContinuar)

        self.pbInterrumpir = QtWidgets.QPushButton(self.centralwidget)
        self.pbInterrumpir.setEnabled(False)
        self.pbInterrumpir.setGeometry(QtCore.QRect(600, 460, 391, 41))
        self.pbInterrumpir.setObjectName('pbInterrumpir')
        self.pbInterrumpir.setText('Interrumpir Proceso Actual')
        self.pbInterrumpir.clicked.connect(self.handleInterrumpir)

        self.pbPausar = QtWidgets.QPushButton(self.centralwidget)
        self.pbPausar.setEnabled(False)
        self.pbPausar.setGeometry(QtCore.QRect(600, 580, 391, 41))
        self.pbPausar.setObjectName('pbPausar')
        self.pbPausar.setText('Poner Programa en Pausa')
        self.pbPausar.clicked.connect(self.handlePausar)

        self.pbError = QtWidgets.QPushButton(self.centralwidget)
        self.pbError.setEnabled(False)
        self.pbError.setGeometry(QtCore.QRect(600, 520, 391, 41))
        self.pbError.setObjectName('pbError')
        self.pbError.setText('Marcar Error en Proceso')
        self.pbError.clicked.connect(self.handleError)

        self.pbEvaluar = QtWidgets.QPushButton(self.centralwidget)
        self.pbEvaluar.setGeometry(QtCore.QRect(890, 310, 101, 31))
        self.pbEvaluar.setObjectName('pbEvaluar')
        self.pbEvaluar.setText('Evaluar')
        self.pbEvaluar.clicked.connect(self.obtenerCantidadDeProcesos)

        self.pbComenzar = QtWidgets.QPushButton(self.centralwidget)
        self.pbComenzar.setEnabled(False)
        self.pbComenzar.setGeometry(QtCore.QRect(600, 360, 391, 41))
        self.pbComenzar.setObjectName('pbComenzar')
        self.pbComenzar.setText('Comenzar')
        self.pbComenzar.clicked.connect(self.handleComenzar)


        # =============================================================================================
        # TextEdits
        self.textEdit_ProcesoEjecucion = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_ProcesoEjecucion.setEnabled(True)
        self.textEdit_ProcesoEjecucion.setGeometry(QtCore.QRect(30, 220, 421, 61))
        self.textEdit_ProcesoEjecucion.setObjectName('textEdit_ProcesoEjecucion')

        self.textEdit_CantidadProcesos = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_CantidadProcesos.setGeometry(QtCore.QRect(600, 310, 281, 31))
        self.textEdit_CantidadProcesos.setUndoRedoEnabled(False)
        self.textEdit_CantidadProcesos.setObjectName('textEdit_CantidadProcesos')
        self.textEdit_CantidadProcesos.setPlaceholderText('Ingresa la cantidad de procesos...')

        self.textEdit_LoteActual = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_LoteActual.setEnabled(True)
        self.textEdit_LoteActual.setGeometry(QtCore.QRect(30, 100, 421, 61))
        self.textEdit_LoteActual.setObjectName('textEdit_LoteActual')

        self.textEdit_ProcesosTerminados = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_ProcesosTerminados.setEnabled(True)
        self.textEdit_ProcesosTerminados.setGeometry(QtCore.QRect(30, 340, 421, 151))
        self.textEdit_ProcesosTerminados.setObjectName('textEdit_ProcesosTerminados')

        # =============================================================================================
        # Thread
        self.threadpool = QThreadPool()
        self.runnerSistemaOperativo = RunnerSistemaOperativo()
        self.runnerSistemaOperativo.señales.progreso.connect(self.actualizarProgreso)                       # Conectar la señal del runner a actualizar progreso aquí

        # ... Signals: UI - Runner ....................................................................
        self.pbInterrumpir.pressed.connect(self.runnerSistemaOperativo.interrumpir)
        self.pbError.pressed.connect(self.runnerSistemaOperativo.error)
        self.pbPausar.pressed.connect(self.runnerSistemaOperativo.pausar)
        self.pbContinuar.pressed.connect(self.runnerSistemaOperativo.reanudar)
        self.pbTerminar.pressed.connect(self.runnerSistemaOperativo.terminar)

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # =================================================================================================
    # Funciones - Setup
    def obtenerCantidadDeProcesos(self):
        cantidadProcesos = self.textEdit_CantidadProcesos.toPlainText()
        if (not cantidadProcesos.isnumeric()):
            self.label_Mensajes.setText('Ingresa un número válido')
        elif (int(cantidadProcesos) < 0):
            self.label_Mensajes.setText('Ingresa un número válido')
        else:
            self.label_Mensajes.setText('El número de procesos ingresado es válido')
            self.textEdit_CantidadProcesos.setEnabled(False)
            self.pbComenzar.setEnabled(True)
            self.pbEvaluar.setEnabled(False)
            self.label_Estado.setText('Estado: {}'.format(self.runnerSistemaOperativo.estado))
            self.label_LotesPendientes.setText( 'Número de Lotes Pendientes: {}'.format(str(len(self.runnerSistemaOperativo.listaLotesPendientes))))

    # ---------------------------------------------------------------------------------------------
    # Funciones - Thread
    def comenzarProcesamiento(self, cantidadProcesos):
        self.runnerSistemaOperativo.cantidadProcesos = int(cantidadProcesos)
        self.runnerSistemaOperativo.generarProcesosAleatoriamente()
        self.runnerSistemaOperativo.particionarProcesosEnLotes()
        self.threadpool.start(self.runnerSistemaOperativo)          
                                                           
    def actualizarProgreso(self, estadoGeneral):
        # [0] = listaLotesPendientes, [1] = loteActual, [2] = cantidadProcesos, [3] = listaProcesos
        # [4] = procesoActual, [5] = procesosTerminados, [6] = contadorGlobal, [7] = estadoSO
        self.label_LotesPendientes.setText(f'Número de Lotes Pendientes: {len(estadoGeneral[0])}')
        self.textEdit_LoteActual.setText(f'{estadoGeneral[1]}')
        # estadoGeneral[2]
        # estadoGeneral[3]
        self.textEdit_ProcesoEjecucion.setText(f'{estadoGeneral[4]}')
        self.textEdit_ProcesosTerminados.setText(f'{estadoGeneral[5]}')
        self.label_ContadorGeneral.setText(f'Contador General: {estadoGeneral[6]}')
        self.label_Estado.setText(f'Estado: {estadoGeneral[7]}')
        self.label_Mensajes.setText('Programa en Ejecución')
    

    # ---------------------------------------------------------------------------------------------
    # Funciones - Handlers
    def handleComenzar(self):
        self.pbComenzar.setEnabled(False)
        self.pbInterrumpir.setEnabled(True)
        self.pbError.setEnabled(True)
        self.pbPausar.setEnabled(True)
        self.pbContinuar.setEnabled(False)
        self.pbTerminar.setEnabled(True)

        cantidadProcesos = self.textEdit_CantidadProcesos.toPlainText()
        self.comenzarProcesamiento(cantidadProcesos)

    def handleInterrumpir(self):
        self.label_Mensajes.setText('Proceso Interrumpido')

    def handleError(self):
        self.label_Mensajes.setText('Proceso Abortado')

    def handlePausar(self):
        self.pbInterrumpir.setEnabled(False)
        self.pbError.setEnabled(False)
        self.pbPausar.setEnabled(False)
        self.pbContinuar.setEnabled(True)
        self.pbTerminar.setEnabled(True)

    def handleContinuar(self):
        self.pbInterrumpir.setEnabled(True)
        self.pbError.setEnabled(True)
        self.pbPausar.setEnabled(True)
        self.pbContinuar.setEnabled(False)
        self.pbTerminar.setEnabled(True)
    
    def handleTerminar(self):
        self.pbInterrumpir.setEnabled(False)
        self.pbError.setEnabled(False)
        self.pbPausar.setEnabled(False)
        self.pbContinuar.setEnabled(False)
        self.pbTerminar.setEnabled(False)


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
