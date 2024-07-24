import os
import subprocess
import signal
import time

class testRun:
    @staticmethod
    def newSim():

        path = '~/Adi\ Summer\ 2024/AutoDRIVE-Simulator-AEB/AutoDRIVE\ Simulator.x86_64'
        #Local Path update for palmetto
        process = subprocess.Popen(path, shell=True)

    @staticmethod
    def killSim():
        file = 'AutoDRIVE\ Simulator.x86_64'
        cmd = f"pgrep -f {file}"
        pid = os.popen(cmd).read().strip()

        if pid:
            os.system(f"kill {pid}")
            print(f"Executable {file} stopped.")
        else:
            print(f"No process found for {file}.")

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
    def newOpenCAV(controls):
        path = 'opencav_aeb_genetic.py'
        

        controls = [str(item) for sublist in controls for item in sublist]

        command = ["python3", path] + controls

        process = subprocess.Popen(command, shell=False)

    @staticmethod
    def killOpenCAV():
        file = 'opencav_aeb_genetic.py'
        cmd = f"pgrep -f {file}"
        pid = os.popen(cmd).read().strip()

        if pid:
            os.system(f"kill {pid}")
            print(f"Executable {file} stopped.")
        else:
            print(f"No process found for {file}.")


        