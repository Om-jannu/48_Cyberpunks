from PyQt5.QtCore import *
import subprocess
from multipledispatch import dispatch

class Worker(QObject):
    target = ""
    result = ""
    option = 0
    port1 = 0
    port2 = 0

    @dispatch(str, int)
    def __init__(self, t, op):
        super().__init__()
        self.target = t
        self.option = op

    @dispatch(str, int, int, int)
    def __init__(self, t, p1, p2, op):
        super().__init__()
        self.target = t
        self.port1 = p1
        self.port2 = p2
        self.option = op

    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        if self.option == 0:
            # Regular scan
            regScan = subprocess.run(['nmap', self.target],capture_output=True,text=True)
            self.result = regScan.stdout
            self.finished.emit()
        elif self.option == 1:
            # Ping scan
            regScan = subprocess.run(['nmap','-sn', self.target],capture_output=True,text=True)
            self.result = regScan.stdout
            self.finished.emit()
        elif self.option == 2:
            # Intense Scan
            regScan = subprocess.run(['nmap','-T4','-A','-v', self.target],capture_output=True,text=True)
            self.result = regScan.stdout
            self.finished.emit()
        elif self.option == 3:
            # Intense UDP Scan
            regScan = subprocess.run(['nmap','-p',str(self.port1)+'-'+str(self.port2),'-sS','-sU','-T4', self.target],capture_output=True,text=True)
            self.result = regScan.stdout
            self.finished.emit()
        elif self.option == 4:
            # Intense TCP Scan
            regScan = subprocess.run(['nmap','-p',str(self.port1)+'-'+str(self.port2), self.target],capture_output=True,text=True)
            self.result = regScan.stdout
            self.finished.emit()
            