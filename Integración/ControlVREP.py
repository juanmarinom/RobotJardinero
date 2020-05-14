import vrep
import time
import math
import DeltaJardinero
import kinematics

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    dest = data.decode('ascii')
    PosX = dest[0:3]
    PosY = dest[4:7]
    PosZ =dest[8:11]
    PosF=[PosX,PosY,PosZ]
    print(PosX)
    print(PosY)
    print(PosZ)
# Vrep connection
vrep.simxFinish(-1) # Ending of previous communication open
clientID = vrep.simxStart('127.0.0.1', 3999, True, True, 5000, 5)
vrep.simxSynchronous(clientID, True)

PosF=[20,20,40]
i=0


    

if clientID != -1:
    print("Connection succeed")
    Robot = DeltaJardinero.Delta('div_join_1', 'div_join_2', 'div_join_3',1, -1, 1, 24, 24, 24, clientID)
#     # Set initial angles
    r, handle1 = vrep.simxGetObjectHandle(clientID, 'div_join_1', vrep.simx_opmode_oneshot_wait)
    # print(handle1)
    # r, handleCam = vrep.simxGetObjectHandle(clientID, 'BASECAMARA_respondable', vrep.simx_opmode_oneshot_wait)
    if i==0:
        vrep.simxSynchronous(clientID, True)
        Robot.setVelocity(0.5, 0.5, 0.5)
        i==1

#     #Posicion inicial
    Ang=kinematics.inverse_kin(PosF)
    print(Ang)
    Ang[0]=round(Ang[0],2)
    Ang[1]=round(Ang[1],2)
    Ang[2]=round(Ang[2],2)
    print(Ang[0])
    print(Ang[1])
    print(Ang[2])
    Robot.setAngles(Ang[0],Ang[1],Ang[2])
    time.sleep(2)
        # PosEF=vrep.simxGetObjectPosition(clientID,handleCam,-1,vrep.simx_opmode_streaming)
        # print(PosEF)