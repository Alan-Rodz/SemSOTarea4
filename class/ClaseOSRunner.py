from PyQt5.QtWidgets import (QWidget, QApplication, QProgressBar, QMainWindow, QHBoxLayout, QPushButton)
from PyQt5.QtCore import (Qt, QObject, pyqtSignal, pyqtSlot, QRunnable, QThreadPool)
import time
import os 
import random 
from ClaseProceso import Proceso

# **************************************************************************************************************************
TAMAÑO_LOTE = 5
VELOCIDAD_PROCESAMIENTO = 1
TIEMPO_ESPERA_LOTES = 8
LIMPIAR_PANTALLA = 'clear'

ESTADO_SO_INICIAL = 'Inicial'
ESTADO_SO_PROCESAR = 'Procesando'
ESTADO_SO_PAUSA = 'Pausado'
ESTADO_SO_INTERRUMPIR = 'Interrumpir'
ESTADO_SO_ERROR = 'Error'
ESTADO_SO_TERMINAR = 'Terminado'

ESTADO_PROCESO_PENDIENTE = 'Pendiente'
ESTADO_PROCESO_EJECUCION = 'Ejecucion'
ESTADO_PROCESO_TERMINADO = 'Terminado'

rangoSinCero = [i for i in range(-1000000, 1000000) if i not in [0]]
rangoConCero = [i for i in range(-1000000, 1000000)]

# --------------------------------------------------------------------------------------------------------------------------
class SistemaOperativoSignals(QObject):
    # Regresamos una lista con todo el estado del programa en un momento particular
    # [0] = listaLotesPendientes
    # [1] = loteActual
    # [2] = cantidadProcesos
    # [3] = listaProcesos
    # [4] = procesoActual
    # [5] = procesosTerminados
    # [6] = contadorGlobal
    # [7] = estadoSO
 
    progreso = pyqtSignal(list)                 

# --------------------------------------------------------------------------------------------------------------------------
class RunnerSistemaOperativo(QRunnable):    

    # Enviadas desde aquí hacia la GUI
    señales = SistemaOperativoSignals()    
                    
    # ====================================================================================================================
    # Inicialización
    def __init__(self):
        super().__init__()
        self.listaLotesPendientes = []
        self.loteActual = []

        self.cantidadProcesos = 0
        self.listaProcesos = []
        self.procesoActual = []

        self.procesosTerminados = []
        self.contadorGlobal = 0 
        self.estado = ESTADO_SO_INICIAL
        self.estadoGeneral = []


    def generarProcesosAleatoriamente(self):
        for i in range(self.cantidadProcesos):
            idSecuencial = i
            tmeAleatorio = random.randint(6, 16)
            operacionAleatoria = random.choice(['+', '-', '/', '%'])

            if (operacionAleatoria == '/' or operacionAleatoria == '%'):
                operando1Aleatorio = random.choice(rangoSinCero)
                operando2Aleatorio = random.choice(rangoSinCero)
            else:
                operando1Aleatorio = random.choice(rangoConCero)
                operando2Aleatorio = random.choice(rangoConCero)

            estadoDefinido = 'pendiente'
            tiempoTotalAleatorio = tmeAleatorio
            tiempoRestanteDefinido = 0

            numeroLoteDefinido = 0
            errorDefinido = False

            nuevoProceso = Proceso(idSecuencial, tmeAleatorio, operacionAleatoria, operando1Aleatorio, operando2Aleatorio)
            self.listaProcesos.append(nuevoProceso)

    def particionarProcesosEnLotes(self):
        lotes = [self.listaProcesos[x:x+TAMAÑO_LOTE]
                 for x in range(0, len(self.listaProcesos), TAMAÑO_LOTE)]
        # Acomodamos el lote de cada proceso
        for indiceLote in range(len(lotes)):
            for indiceProceso in range(len(lotes[indiceLote])):
                lotes[indiceLote][indiceProceso].numlote = indiceLote
        self.listaProcesos = []
        self.listaLotesPendientes = lotes

    # ====================================================================================================================
    # Ejecución
    @pyqtSlot()
    def run(self):
        for n in range(100):
            self.estadoGeneral = [self.listaLotesPendientes, self.loteActual, self.cantidadProcesos, self.listaProcesos, 
                self.procesoActual, self.procesosTerminados, self.contadorGlobal, self.estado]
            self.señales.progreso.emit(self.estadoGeneral)
          
            print(self.cantidadProcesos)
            time.sleep(1)
            
            while self.estado == ESTADO_SO_PAUSA:
                time.sleep(0)
                
            if self.estado == ESTADO_SO_TERMINAR:
                break

    # ====================================================================================================================
    # Control de Estados
    def pausar(self):
        self.estado = ESTADO_SO_PAUSA
        
    def reanudar(self):
        self.estado = ESTADO_SO_PROCESAR
        
    def terminar(self):
        self.estado = ESTADO_SO_TERMINAR

    # ====================================================================================================================
    # Utilidad
    def imprimirInformacionDiagnostica(self):
        os.system(LIMPIAR_PANTALLA)
        print('Estado: {}'.format(self.estado))
        print('Cantidad de Lotes Pendientes: {}'.format(len(self.listaLotesPendientes)))
        print('Lote Actual: {}'.format(self.loteActual))
        print('Proceso En Ejecución: {}'.format(self.procesoActual))
        print('Procesos Terminados: {}'.format(self.procesosTerminados))
        print('Contador Global: {}'.format(self.contadorGlobal))

