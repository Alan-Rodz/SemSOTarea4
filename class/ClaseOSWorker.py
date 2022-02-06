from PyQt5.QtCore import QThread, QObject, pyqtSignal


class OSWorker(QObject):
    finished = pyqtSignal()         # give worker class a finished signal
    progress = pyqtSignal(int)

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        self.continue_run = True  # provide a bool run condition for the class

    def do_work(self):
        i = 1
        while self.continue_run:  # give the loop a stoppable condition
            self.progress.emit(i)
            QThread.sleep(1)
            i = i + 1
        self.finished.emit()  # emit the finished signal when the loop is done

    def stop(self):
        self.continue_run = False  # set the run condition to false on stop

    def restart(self):
        self.continue_run = True
