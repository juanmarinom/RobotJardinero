# Programa para ejecutar todos los subprogramas que controlan el robot

# import os
#
# # os.system("python C:\\Users\\Alvaro\\Desktop\\Master\\LAB\\RobotJardinero\\Programa\\control.py")
# os.system("DELTA_V8.ttt")
# os.system("python control.py")

import subprocess

process = subprocess.run("DELTA_V8.ttt", shell=True)
process = subprocess.run("python control.py")
input("Presione para finalizar...")
