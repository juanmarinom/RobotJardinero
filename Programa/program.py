# Programa para ejecutar todos los subprogramas que controlan el robot

import subprocess
from subprocess import Popen, CREATE_NEW_CONSOLE
from multiprocessing import Process
import os

def serverControl():
    # process = subprocess.run("DELTA_V10.ttt", shell=True)
    # process = subprocess.run("python control.py", shell=True)
    os.system("python control.py")

def serverVision():
    # process = Popen("venv\\Scripts\\python vision.py", creationflags=CREATE_NEW_CONSOLE)
    os.system("venv\\Scripts\\python vision.py")

# def clientsUnity():
    # process = Popen("unity\\SQLite.exe")

if __name__ == '__main__':
    os.system("DELTA_V10.ttt")
    os.system("unity\\SQLite.exe")

    p = Process(target=serverControl, args=())
    q = Process(target=serverVision, args=())
    p.start()
    q.start()
    p.join()
    q.join()

# process = subprocess.run("DELTA_V8.ttt", shell=True)
# process = subprocess.run("python control.py", shell=True)
# process = subprocess.run("venv\\Scripts\\python vision.py", shell=True)
# input("Presione para finalizar...")
