from PyQt5.QtWidgets import (QWidget, QApplication, QProgressBar, QMainWindow, QHBoxLayout, QPushButton)
from PyQt5.QtCore import (Qt, QObject, pyqtSignal, pyqtSlot, QRunnable, QThreadPool)
import time

class SistemaOperativoSignals(QObject):
    progreso = pyqtSignal(int)

class RunnerSistemaOperativo(QRunnable):    

    # Enviadas desde aquí hacia la GUI
    señales = SistemaOperativoSignals()                        

    def __init__(self):
        super().__init__()
        self.esta_pausado = False
        self.esta_terminado = False
            
    @pyqtSlot()
    def run(self):
        for n in range(100):
            self.señales.progreso.emit(n + 1)
            time.sleep(1)
            
            while self.esta_pausado:
                time.sleep(0)
                
            if self.esta_terminado:
                break
                
    def pausar(self):
        self.esta_pausado = True
        
    def reanudar(self):
        self.esta_pausado = False
        
    def terminar(self):
        self.esta_terminado = True