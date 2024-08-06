import os
import subprocess
import signal
import time

class testRun:
    def __init__(self):
        self.simProcess = None
        self.opencav_process = None
        self.fitness = 0

    def newSim(self):

        path = '~/Adi\ Summer\ 2024/AutoDRIVE-Simulator-AEB/AutoDRIVE\ Simulator.x86_64'
        #Local Path update for palmetto
        self.simProcess = subprocess.Popen(path, shell=True)

    def killSim(self):
        file = 'AutoDRIVE\ Simulator.x86_64'
        cmd = f"pgrep -f {file}"
        pid = os.popen(cmd).read().strip()

        if pid:
            os.system(f"kill {pid}")
            print(f"Executable {file} stopped.")
        else:
            print(f"No process found for {file}.")

    def simIsRunning():
        file = 'AutoDRIVE\ Simulator.x86_64'
        cmd = f"pgrep -f {file}"
        pid = os.popen(cmd).read().strip()

        if pid:
            return True
        else:
            return False
        
    def newOpenCAV(self, controls):
        path = 'opencav_aeb_genetic.py'
        

        controls = [str(item) for sublist in controls for item in sublist]

        command = ["python3", path] + controls

        self.opencav_process = subprocess.Popen(command, shell=False)

        stdout, stderr = self.opencav_process.communicate()
        
        self.fitness = stdout

    def killOpenCAV(self):
        file = 'opencav_aeb_genetic.py'
        cmd = f"pgrep -f {file}"
        pid = os.popen(cmd).read().strip()

        if pid:
            os.system(f"kill {pid}")
            print(f"Executable {file} stopped.")
        else:
            print(f"No process found for {file}.")
