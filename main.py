import sys
sys.path.insert(1, './class/')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QWidget, QLabel, QPushButton
import random
import time

from ClaseOSWorker import OSWorker
from ClaseSistemaOperativo import SistemaOperativo

# *********************************************************************************************
sistemaOperativo = SistemaOperativo()

# Palettes - UI - Labels - Buttons - TextEdits - Functions
class Ui_MainWindow(object):
    # stop_signal = pyqtSignal()  # make a stop signal to communicate with the worker in another thread

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
        self.label_ContadorGeneral.setGeometry(QtCore.QRect(30, 510, 121, 21))
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
        # Thread:
        # self.thread = QThread()
        # self.worker = OSWorker()
        # self.stop_signal.connect(self.worker.stop)              # connect stop signal to worker stop method
        # self.worker.moveToThread(self.thread)

        # self.worker.finished.connect(self.thread.quit)          # connect the workers finished signal to stop thread
        # self.worker.finished.connect(self.worker.deleteLater)   # connect the workers finished signal to clean up worker
        # self.thread.finished.connect(self.thread.deleteLater)   # connect threads finished signal to clean up thread

        # self.thread.started.connect(self.worker.do_work)
        # self.thread.finished.connect(self.worker.stop)

        # # Start Button action:
        # self.pbComenzar.clicked.connect(self.thread.start)
        # self.pbContinuar.clicked.connect(self.thread.start)

        # # Stop Button action:
        # self.pbPausar.clicked.connect(self.stop_thread)

        # ---------------------------------------------------------------------------------------------
        # Setup
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # =============================================================================================
    # Functions
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
            self.label_Estado.setText('Estado: {}'.format(sistemaOperativo.estado))
            
            sistemaOperativo.setCantidadProcesos(int(cantidadProcesos))
            sistemaOperativo.generarProcesosAleatoriamente()
            sistemaOperativo.particionarProcesosEnLotes()
            sistemaOperativo.imprimirInformacionDiagnostica()

            self.label_LotesPendientes.setText( 'Número de Lotes Pendientes: {}'.format(str(len(sistemaOperativo.listaLotesPendientes))))

    def procesar(self):
        # Step 1: Create a QThread object
        self.thread = QThread()
        # Step 2: Create a worker object
        self.worker = OSWorker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.do_work)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportarProgreso)
        
        # Step 6: Start the thread
        self.thread.start()

        # Final resets
        # self.longRunningBtn.setEnabled(False)
        # self.thread.finished.connect(lambda: self.longRunningBtn.setEnabled(True))
        # self.thread.finished.connect(lambda: self.stepLabel.setText("Long-Running Step: 0"))

    def reportarProgreso(self, n):
        self.textEdit_LoteActual.setText(f"{n}")


    def handleComenzar(self):
        self.pbComenzar.setEnabled(False)
        self.pbInterrumpir.setEnabled(True)
        self.pbError.setEnabled(True)
        self.pbPausar.setEnabled(True)
        self.pbContinuar.setEnabled(False)
        self.pbTerminar.setEnabled(True)
        self.procesar()


    def handleInterrumpir(self):
        pass

    def handleError(self):
        pass

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
        # sys.exit()

    # When stop_btn is clicked this runs. Terminates the worker and the thread.
    def stop_thread(self):
        self.stop_signal.emit()  # emit the finished signal on stop


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
