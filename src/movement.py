from math import sqrt
from math import pi
import math
import time
import sys
from kinematics import *

def calc_vel(rob, ref):
    curpos = rob.getAngles()
    err = list()
    for re,cur in zip(ref,curpos):
        err.append(abs(re-cur))

    norm = max(err)
    if norm != 0:
        err[0]=err[0]/norm
        err[1]=err[1]/norm
        err[2]=err[2]/norm
    else:
        err = [0,0,0]

    return err

def move_robot(rob, ref, velnom=0.7, type="linear", numpoints=50):
    # Movimiento lineal del robot de una posicion a otra
    if type == "linear":
        inter = list()

        curpos = forward_kin(rob.getAngles())

        aux = [0,0,0]
        for i in range(0,numpoints+1):
            aux[0] = curpos[0] + (ref[0]-curpos[0])*i/numpoints
            aux[1] = curpos[1] + (ref[1]-curpos[1])*i/numpoints
            aux[2] = curpos[2] + (ref[2]-curpos[2])*i/numpoints

            inter.append([aux[0],aux[1],aux[2]])

        for ints in inter:
            # print("## Pos 1")
            angles = inverse_kin(ints)
            # print("Angulos del robot = {}".format(angles))
            vel = calc_vel(rob, angles)
            rob.setVelocity(velnom*vel[0], velnom*vel[1], velnom*vel[2])
            rob.setAngles(angles[0],angles[1],angles[2])
            # Se tiene que quitar el sleep para que se ejecute correctamente
            # para ello se comprueba como si fuera un debouncer que no se ha
            # realizado movimiento (posicion_prev = curpos)
            # time.sleep(1)
            curpos = forward_kin(rob.getAngles())
            prev_pos = 0
            while (prev_pos != curpos):
                prev_pos = curpos
                curpos = forward_kin(rob.getAngles())
                time.sleep(0.01)

        return 1

    # Movimiento no lineal del robot de una posicion a otra
    else:
        pass
