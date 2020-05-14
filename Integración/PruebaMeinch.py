import socket
import movement
import vrep
import time
import math
import DeltaJardinero
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))#Creación del socket
    data = s.recv(1024)#Recibimiento de la información
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
    
vrep.simxFinish(-1) # Ending of previous communication open
clientID = vrep.simxStart('127.0.0.1', 3999, True, True, 5000, 5)
vrep.simxSynchronous(clientID, True)

if clientID != -1:
    print("Connection succeed")

    Robot = DeltaJardinero.Delta('div_join_2', 'div_join_3', 'div_join_1',-1, 1, 1, 24, 24, 24, clientID)
    r, handle1 = vrep.simxGetObjectHandle(clientID, 'div_join_1', vrep.simx_opmode_oneshot_wait)
    # print(handle1)
    vrep.simxSynchronous(clientID, True)
    velnom = 0.7
    Robot.setVelocity(velnom, velnom, velnom)
    Robot.setAngles(90,90,90)
    movement.move(Robot, Ref)