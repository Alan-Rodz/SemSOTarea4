import time
from PyQt5 import QtCore
# expect to see ticks & tocks
class Alarm(QtCore.QThread):
    signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Alarm, self).__init__(parent)
        self.signal.connect(self.eventp)
        self.start()

    def run(self):
        while True:
            print('tick')
            self.signal.emit()
            time.sleep(1)

    @QtCore.pyqtSlot()
    def eventp(self):
        print('Tock')

if __name__ == '__main__':
    import sys
    app = QtCore.QCoreApplication(sys.argv)
    alarm = Alarm()
    QtCore.QTimer.singleShot(6*1000, QtCore.QCoreApplication.quit)
    sys.exit(app.exec_())