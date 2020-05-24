# Programa para ejecutar todos los subprogramas que controlan el robot

import subprocess
from subprocess import Popen, CREATE_NEW_CONSOLE
from multiprocessing import Process
import os
import pathlib
import sys


def serverControl():
    process = subprocess.run("DELTA_V10.ttt", shell=True)
    process = subprocess.run("python control.py", shell=True)

def serverVision():
    process = subprocess.run("venv\\Scripts\\python vision.py", shell=True)

def programUnity():
    process = subprocess.run("unity\\SQLite.exe")


path = pathlib.Path().absolute()
print(path)

if __name__ == '__main__':
    p = Process(target=serverControl, args=())
    q = Process(target=serverVision, args=())
    r = Process(target=programUnity, args=())
    p.start()
    q.start()
    r.start()
    p.join()
    q.join()
    r.join()

    sys.exit()
