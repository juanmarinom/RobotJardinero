# Programa para ejecutar todos los subprogramas que controlan el robot

import subprocess
from subprocess import Popen, CREATE_NEW_CONSOLE
from multiprocessing import Process

def serverControl():
    process = subprocess.run("DELTA_V8.ttt", shell=True)
    process = subprocess.run("python control.py", shell=True)

def serverVision():
    process = Popen("venv\\Scripts\\python vision.py", creationflags=CREATE_NEW_CONSOLE)

def clientsUnity():
    process = Popen("unity\\SQLite.exe")

if __name__ == '__main__':
    p = Process(target=serverControl, args=())
    q = Process(target=serverVision, args=())
    r = Process(target=clientsUnity, args=())
    p.start()
    q.start()
    r.start()
    p.join()
    q.join()
    r.join()

# process = subprocess.run("DELTA_V8.ttt", shell=True)
# process = subprocess.run("python control.py", shell=True)
# process = subprocess.run("venv\\Scripts\\python vision.py", shell=True)
# input("Presione para finalizar...")
