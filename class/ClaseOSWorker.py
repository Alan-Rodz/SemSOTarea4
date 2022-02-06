from PyQt5.QtCore import QThread, QObject, pyqtSignal


class OSWorker(QObject):
    finished = pyqtSignal()         # give worker class a finished signal
    progreso = pyqtSignal(int)

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        self.continuar_ejecucion = True  # provide a bool run condition for the class

    def procesar(self):
        i = 1
        while self.continuar_ejecucion:  # give the loop a stoppable condition
            self.progreso.emit(i)
            QThread.sleep(1)
            i = i + 1
        self.finished.emit()  # emit the finished signal when the loop is done

    def stop(self):
        self.continuar_ejecucion = False  # set the run condition to false on stop

    def restart(self):
        self.continuar_ejecucion = True

