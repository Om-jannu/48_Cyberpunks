from PyQt5.QtCore import *
import subprocess
import schedule, time

class ScheduleWorker(QObject):
    target = ""
    result = ""
    option = 0

    def __init__(self, t, op):
        super().__init__()
        self.target = t
        self.option = op

    finished = pyqtSignal()
    progress = pyqtSignal(int)



    def run(self):
        if self.option == 0:
            # Regular scan
            def a():
                regScan = subprocess.run(['nmap', self.target],capture_output=True,text=True)
                self.result = regScan.stdout
                print(self.result)
            schedule.every(30).seconds.do(a)
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
            regScan = subprocess.run(['nmap','-p-','-sS','-sU','-T4', self.target],capture_output=True,text=True)
            self.result = regScan.stdout
            self.finished.emit()
        elif self.option == 4:
            # Intense TCP Scan
            regScan = subprocess.run(['nmap','-p-', self.target],capture_output=True,text=True)
            self.result = regScan.stdout
            self.finished.emit()
            
        while True:
            schedule.run_pending()
            time.sleep(1)