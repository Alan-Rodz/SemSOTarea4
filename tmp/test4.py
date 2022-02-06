import sys
import threading
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Added new
class Communicate(QObject):
    signal = pyqtSignal(str)

class Some(QWidget):
    e = threading.Event()

    def btnfunc(self):
        self.e.set()        

    def __init__(self):
        super().__init__()

        #communicate object
        self.comm = Communicate()
        self.comm.signal.connect(self.append_data)

        self.myButton = QPushButton('do next')
        self.logs = QTextEdit()

        self.mylay = QVBoxLayout()
        self.mylay.addWidget(self.myButton)
        self.mylay.addWidget(self.logs)

        self.setLayout(self.mylay)
        self.setGeometry(300, 300, 300, 550)
        self.setWindowTitle('mytest')
        self.show()
        t = threading.Thread(target=self.myfunc, args=( ))
        t.start()
        self.myButton.clicked.connect(self.btnfunc)

    def myfunc(self):
        for i in range(300):
            # time.sleep(0.4)
            #self.logs.append(str(i))
            self.comm.signal.emit(str(i))
            if i == 20:
                self.e.wait()

    def append_data(self, data):
        self.logs.append(data)

app = QApplication(sys.argv)
ex = Some()
sys.exit(app.exec_())
