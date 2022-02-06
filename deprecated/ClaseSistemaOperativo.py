import os
import random
import keyboard
import time
from ClaseProceso import Proceso

# **************************************************************************************************************************
TAMAÑO_LOTE = 5
VELOCIDAD_PROCESAMIENTO = 1
TIEMPO_ESPERA_LOTES = 8
LIMPIAR_PANTALLA = 'clear'

# ====================================================================================================================
ESTADO_INICIAL = 'Inicial'
ESTADO_PROCESAR = 'Procesando'
ESTADO_PAUSA = 'Pausado'
ESTADO_TERMINAR = 'Terminado'

TECLA_PAUSA = 'p'
TECLA_CONTINUAR = 'c'
TECLA_TERMINAR = 'x'

# ====================================================================================================================
rangoSinCero = [i for i in range(-1000000, 1000000) if i not in [0]]
rangoConCero = [i for i in range(-1000000, 1000000)]

# ====================================================================================================================


class SistemaOperativo:
    listaLotesPendientes = []               
    loteActual = []                         

    cantidadProcesos = 0                    
    listaProcesos = []                      
    procesoActual = []                         

    procesosTerminados = []
    contadorGlobal = 0

    estado = ESTADO_INICIAL

    # ====================================================================================================================
    # Inicialización
    def __init__(self):
        self.lotesPendientes = []
        self.loteActual = []
        self.cantidadProcesos = 0
        self.listaProcesos = []
        self.procesosTerminados = []
        self.contadorGlobal = 0
        self.estado = ESTADO_INICIAL

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

            nuevoProceso = Proceso(
                idSecuencial, tmeAleatorio, operacionAleatoria, operando1Aleatorio, operando2Aleatorio)
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
    # Setters
    def setCantidadProcesos(self, cantidad):
        self.cantidadProcesos = cantidad

    # ====================================================================================================================
    # Getters

    # ====================================================================================================================
    # Utilidades
    def imprimirInformacionDiagnostica(self):
        os.system(LIMPIAR_PANTALLA)
        print('Estado: {}'.format(self.estado))
        print('Cantidad de Lotes Pendientes: {}'.format(len(self.listaLotesPendientes)))
        print('Lote Actual: {}'.format(self.loteActual))
        print('Proceso En Ejecución: {}'.format(self.procesoActual))
        print('Procesos Terminados: {}'.format(self.procesosTerminados))
        print('Contador Global: {}'.format(self.contadorGlobal))
