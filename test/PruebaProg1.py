import vrep
import time
import math
import DeltaJardinero
import sys

sys.path.insert(1, '../../../control')
from kinematics import *
from movement import *

def write(file, robot):
    pos_teo = forward_kin(robot.getAngles())
    campos = robot.getCameraPosition()
    pos_real = [campos[1]*1000,-campos[0]*1000,-campos[2]*1000]

    file.write("{},{},{},{},{},{}\n".format(pos_teo[0],pos_teo[1],pos_teo[2],
        pos_real[0],pos_real[1],pos_real[2]))


# Vrep connection
vrep.simxFinish(-1) # Ending of previous communication open
clientID = vrep.simxStart('127.0.0.1', 3999, True, True, 5000, 5)
vrep.simxSynchronous(clientID, True)

if clientID != -1:
    print("Connection succeed")

    Robot = DeltaJardinero.Delta('div_join_2', 'div_join_3', 'div_join_1',-1, 1, 1, 24, 24, 24, clientID)
    # Set initial angles
    #r, handle1 = vrep.simxGetObjectHandle(clientID, 'div_join_1', vrep.simx_opmode_oneshot_wait)
    #print(handle1)
    #vrep.simxSynchronous(clientID, True)
    velnom = 0.7
    Robot.setVelocity(velnom, velnom, velnom)

    #Posicion inicial

    Robot.setAngles(90,90,90)
    time.sleep(2)
    robpos = forward_kin([90,90,90])
    print("La posicion del efector final es: {}".format(robpos))

    f = open("data.csv","a")

    # while True:
    move(Robot, [80,80,200])
    time.sleep(0.5)
    write(f,Robot)
    move(Robot, [-80,80,200])
    time.sleep(0.5)
    write(f,Robot)
    move(Robot, [-80,-80,200])
    time.sleep(0.5)
    write(f,Robot)
    move(Robot, [80,-80,200])
    time.sleep(0.5)
    write(f,Robot)
    move(Robot, [0,0,130])
    time.sleep(0.5)
    write(f,Robot)
    move(Robot, [40,40,200])
    time.sleep(0.5)
    write(f,Robot)
    move(Robot, [-40,40,200])
    time.sleep(0.5)
    write(f,Robot)
    move(Robot, [-40,-40,200])
    time.sleep(0.5)
    write(f,Robot)
    move(Robot, [40,-40,200])
    time.sleep(0.5)
    write(f,Robot)
    move(Robot, [50,-20,180])
    time.sleep(0.5)
    write(f,Robot)
    move(Robot, [10,-90,200])
    time.sleep(0.5)
    write(f,Robot)
    move(Robot, [0,-40,200])
    time.sleep(0.5)
    write(f,Robot)
    move(Robot, [40,0,250])
    time.sleep(0.5)
    write(f,Robot)
    move(Robot, [10,10,230])
    time.sleep(0.5)
    write(f,Robot)
    move(Robot, [-100,-100,200])
    time.sleep(0.5)
    write(f,Robot)

    f.close()

    #vrep.simxSynchronousTrigger(clientID)

    #Obtención posición base camara respecto centro robot(centro, parte superior)


else:
    print("Failed connection")
