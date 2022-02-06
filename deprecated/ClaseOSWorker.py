from PyQt5.QtCore import QThread, QObject, pyqtSignal


class OSWorker(QObject):
    finished = pyqtSignal()         
    progreso = pyqtSignal(int)

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        self.continuar_ejecucion = True  

    def procesar(self):
        i = 1
        while self.continuar_ejecucion:  
            self.progreso.emit(i)
            QThread.sleep(1)
            i = i + 1
        # self.finished.emit()  

    def pausar(self):
        self.continuar_ejecucion = False  # set the run condition to false on stop

    def continuar(self):
        self.continuar_ejecucion = True
