import vrep
import time
import math
import DeltaJardinero
import sys

sys.path.insert(1, '../../../control')
from kinematics import *

def calc_vel(ref):
    curpos = Robot.getAngles()
    err = list()
    for re,cur in zip(ref,curpos):
        err.append(abs(re-cur))

    norm = max(err)
    err[0]=err[0]/norm
    # if err[0]<0.05:
    #     err[0]=0.05
    err[1]=err[1]/norm
    # if err[1]<0.05:
    #     err[1]=0.05
    err[2]=err[2]/norm
    # if err[2]<0.05:
    #     err[2]=0.05

    return err

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
    time.sleep(5)
    robpos = forward_kin([90,90,90])
    print("La posicion del efector final es: {}".format(robpos))


    while True:
        print("## Pos 1")
        angles = inverse_kin([-40,-40,150])
        print(angles)
        vel = calc_vel(angles)
        print(vel)
        Robot.setVelocity(velnom*vel[0], velnom*vel[1], velnom*vel[2])
        Robot.setAngles(angles[0],angles[1],angles[2])
        time.sleep(1)
        print(Robot.getAngles())

        print("## Pos 2")
        angles = inverse_kin([40,-40,150])
        print(angles)
        vel = calc_vel(angles)
        print(vel)
        Robot.setVelocity(velnom*vel[0], velnom*vel[1], velnom*vel[2])
        Robot.setAngles(angles[0],angles[1],angles[2])
        time.sleep(1)
        print(Robot.getAngles())

        print("## Pos 3")
        angles = inverse_kin([40,40,150])
        print(angles)
        vel = calc_vel(angles)
        print(vel)
        Robot.setVelocity(velnom*vel[0], velnom*vel[1], velnom*vel[2])
        Robot.setAngles(angles[0],angles[1],angles[2])
        time.sleep(1)
        print(Robot.getAngles())

        print("## Pos 4")
        angles = inverse_kin([-40,40,150])
        print(angles)
        vel = calc_vel(angles)
        print(vel)
        Robot.setVelocity(velnom*vel[0], velnom*vel[1], velnom*vel[2])
        Robot.setAngles(angles[0],angles[1],angles[2])
        time.sleep(1)
        print(Robot.getAngles())
    #vrep.simxSynchronousTrigger(clientID)


    #Posicion inicial

    Robot.setAngles(30,-10,-20)
    time.sleep(2)

    #Obtención posición base camara respecto centro robot(centro, parte superior)
    pos = Robot.getCameraPosition()
    print(pos)

else:
    print("Failed connection")
