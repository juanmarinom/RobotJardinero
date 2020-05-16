import sys

sys.path.insert(1,'./src')

import socket
import time
import math
import vrep
import DeltaJardinero
from kinematics import *
from movement import *

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

clientID = -1
while clientID==-1:
    # Vrep connection
    vrep.simxFinish(-1) # Ending of previous communication open
    clientID = vrep.simxStart('127.0.0.1', 3999, True, True, 5000, 5)
    vrep.simxSynchronous(clientID, True)


print("Connection succeed")

Robot = DeltaJardinero.Delta('div_join_2', 'div_join_3', 'div_join_1',-1, 1, 1, 24, 24, 24, clientID)
vel = 0.7
Robot.setVelocity(vel, vel, vel)

# Posicion inicial
Robot.setAngles(90,90,90)
time.sleep(1)

# Se establece un bucle principal en el que se escucha el socket para moverse
# una vez recibida la posicion
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) # Creación del socket

while True:
    data = s.recv(1024)#Recibimiento de la información
    if len(data)>1:
        print('Posicion de destino: ')
        # print(data)
        dest = data.decode('ascii')
        XFin=dest[0:3]
        YFin=dest[4:7]
        ZFin=dest[8:11]
        XFin=int(XFin)
        YFin=int(YFin)
        ZFin=int(ZFin)
        print(XFin,YFin,ZFin)
        Ref = [XFin, YFin, ZFin]

        # Se mueve el robot a la posicion recibida
        move_robot(Robot, Ref)
        time.sleep(0.01)

s.close()
