import os
import subprocess
import signal
import time

class testRun:
    def __init__(self):
        self.simProcess = None
        self.opencav_process = None
        self.fitness = 0

    @staticmethod
    def newSim(self):

        path = '~/Adi\ Summer\ 2024/AutoDRIVE-Simulator-AEB/AutoDRIVE\ Simulator.x86_64'
        #Local Path update for palmetto
        self.simProcess = subprocess.Popen(path, shell=True)

    @staticmethod
    def killSim(self):
        if self.sim_process:
            try:
                os.kill(self.simProcess.pid, signal.SIGTERM)
                self.simProcess = None
            except OSError:
                print("Process Not Found")

    @staticmethod
    def simIsRunning():
        file = 'AutoDRIVE\ Simulator.x86_64'
        cmd = f"pgrep -f {file}"
        pid = os.popen(cmd).read().strip()

        if pid:
            return True
        else:
            return False
        
    @staticmethod
    def newOpenCAV(self, controls):
        path = 'opencav_aeb_genetic.py'
        

        controls = [str(item) for sublist in controls for item in sublist]

        command = ["python3", path] + controls

        self.opencav_process = subprocess.Popen(command, shell=False)

        stdout, stderr = self.opencav_process.communicate()
        
        self.fitness = stdout

    @staticmethod
    def killOpenCAV(self):
        if self.opencav_process:
            try:
                os.kill(self.opencav_process.pid, signal.SIGTERM)
                self.opencav_process = None
            except OSError:
                print("Process Not Found")
