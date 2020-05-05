from math import sqrt
from math import pi
import math
import numpy as np

def forward_kin(theta):
    # Definición de los parámetros
    a = 308.31
    b = 138.56
    l1 = 100
    l2 = 187
    alpha = [0,-120,-240]

    # Definición de las entradas
    # theta = [10,0,0]

    # Se calculan los puntos pi y zi
    p = [0,0,0]
    z = [0,0,0]
    c = [0,0,0]
    h = [0,0,0]

    index=0
    for alph,th in zip(alpha,theta):
        p[index] = np.array(
            [sqrt(3)/6*a*math.cos(math.radians(alph)),
             sqrt(3)/6*a*math.sin(math.radians(alph)),
             0])

        z[index] = p[index] + np.array(
            [l1*math.sin(math.radians(th))*math.cos(math.radians(alph)),
             l1*math.sin(math.radians(th))*math.sin(math.radians(alph)),
             l1*math.cos(math.radians(th))])

        # A c hay que sumarle las incognitas x', y' y z'
        c[index] = np.array(
            [sqrt(3)/6*b*math.cos(math.radians(alph)),
             sqrt(3)/6*b*math.sin(math.radians(alph)),
             0])

        # H serán los vectores auxiliares para la generación del sistema de ecuaciones
        h[index] = c[index] - z[index]

        print("El punto p_{} = {}".format(index+1, p[index]))
        print("El punto z_{} = {}".format(index+1, z[index]))
        print("El punto c_{} = {}".format(index+1, c[index]))

        index+=1

    # matrix_gauss = [[2*h[0][0]-2*h[1][0], 2*h[0][1]-2*h[1][1], 2*h[0][2]-2*h[1][2], h[0][0]**2+h[0][1]**2+h[0][2]**2-h[1][0]**2-h[1][1]**2-h[1][2]**2],
    #      [2*h[0][0]-2*h[2][0], 2*h[0][1]-2*h[2][1], 2*h[0][2]-2*h[2][2], h[0][0]**2+h[0][1]**2+h[0][2]**2-h[2][0]**2-h[2][1]**2-h[2][2]**2],
    #      [2*h[2][0]-2*h[1][0], 2*h[2][1]-2*h[1][1], 2*h[2][2]-2*h[1][2], h[2][0]**2+h[2][1]**2+h[2][2]**2-h[1][0]**2-h[1][1]**2-h[1][2]**2]]
    ecu = [[2*h[0][0]-2*h[1][0], 2*h[0][1]-2*h[1][1], 2*h[0][2]-2*h[1][2], h[0][0]**2+h[0][1]**2+h[0][2]**2-h[1][0]**2-h[1][1]**2-h[1][2]**2],
         [2*h[0][0]-2*h[2][0], 2*h[0][1]-2*h[2][1], 2*h[0][2]-2*h[2][2], h[0][0]**2+h[0][1]**2+h[0][2]**2-h[2][0]**2-h[2][1]**2-h[2][2]**2]]

    for ec in ecu:
        print(ec)

    # Se define como lambda z' y se obtienen las relaciones respecto a lambda de x' e y'
    # en un vector de (real, lambda)
    z = [0,1]
    y = [((-ecu[1][0]/ecu[0][0])*(-ecu[0][3])+ecu[1][3])*(1/((ecu[1][0]/ecu[0][0])*(-ecu[0][1])+ecu[1][1])),
         ((-ecu[1][0]/ecu[0][0])*(-ecu[0][2])+ecu[1][2])*(1/((ecu[1][0]/ecu[0][0])*(-ecu[0][1])+ecu[1][1]))]
    x = [(-ecu[0][1]*y[0]-ecu[0][3])/ecu[0][0],(-ecu[0][1]*y[1]-ecu[0][2])/ecu[0][0]]

    a_ecu = x[1]**2 + y[1]**2 + z[1]**2
    b_ecu = 2*x[0]*x[1] + 2*h[0][0]*x[1] + 2*y[0]*y[1] + 2*h[0][1]*y[1] + 2*z[0]*z[1] + 2*h[0][2]*x[1]
    c_ecu = h[0][0]**2 + x[0]**2 + 2*h[0][0]*x[0] + h[0][1]**2 + y[0]**2 + 2*h[0][1]*y[0] + h[0][2]**2 + z[0]**2 + 2*h[0][2]*z[0] - l2**2

    print("Parametros x,y,z")
    print(x)
    print(y)
    print(z)

    print("Parametros a,b,c de la ecuacion")
    print(a_ecu)
    print(b_ecu)
    print(c_ecu)

    sol_z1 = (-b_ecu+sqrt(b_ecu**2-4*a_ecu*c_ecu))/(2*a_ecu)
    sol_z2 = (-b_ecu-sqrt(b_ecu**2-4*a_ecu*c_ecu))/(2*a_ecu)

    sol_z = max(sol_z1,sol_z2)
    sol_x = x[0]+sol_z*x[1]
    sol_y = y[0]+sol_z*y[1]

    print("Las soluciones son")
    print(round(sol_x,4))
    print(round(sol_y,4))
    print(round(sol_z,4))

    return [sol_x,sol_y,sol_z]


def inverse_kin(pos):
    x,y,z = pos

    # Definicion de los parametros
    a = 60
    b = 30
    l1 = 20
    l2 = 40
    alpha = [0,-120,-240]

    d = (b-a)*sqrt(3)/6


    sol = list()

    index = 0
    for alph in alpha:
        p = 2*x*math.cos(math.radians(alph)) + 2*y*math.sin(math.radians(alph))
        print("p = {}".format(p))

        w = l1**2 + d**2 + x**2 + y**2 + z**2 + d*p
        u = -2*d*l1 - l1*p
        v = -2*z*l1

        print("w = {}".format(w))
        print("u = {}".format(u))
        print("v = {}".format(v))

        a_ecu = l2**2 + v - w
        b_ecu = -2*u
        c_ecu = l2**2 - v - w

        print("a_ecu = {}".format(a_ecu))
        print("b_ecu = {}".format(b_ecu))
        print("c_ecu = {}".format(c_ecu))

        sol_1 = (-b_ecu+sqrt(b_ecu**2-4*a_ecu*c_ecu))/(2*a_ecu)
        sol_2 = (-b_ecu-sqrt(b_ecu**2-4*a_ecu*c_ecu))/(2*a_ecu)

        sol_1_f = math.degrees(2*math.atan(sol_1))
        sol_2_f = math.degrees(2*math.atan(sol_2))
        sol_f = max(sol_1_f,sol_2_f)

        sol.append(sol_f)
        print()

    return sol

print("\n    INVERSE KINEMATICS     \n")
pos = inverse_kin([0,0,40])
print(pos)
# print("\n    FORWARD KINEMATICS     \n")
# forward_kin(pos)