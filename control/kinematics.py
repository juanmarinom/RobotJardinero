from math import sqrt
from math import pi
import math
import numpy as np

def forward_kin(theta):
    # Definición de los parámetros
    a = 60
    b = 30
    l1 = 20
    l2 = 40
    alpha = [0,-120,-240]

    # Definición de las entradas
    # theta = [10,0,0]

    # Se calculan los puntos pi y zi
    q = [0,0,0]
    r = [0,0,0]
    s = [0,0,0]
    t = [0,0,0]

    d = (b-a)*sqrt(3)/6

    index=0
    for alph,th in zip(alpha,theta):
        q[index] = 2*math.cos(math.radians(alph))*(d-l1*math.sin(math.radians(th)))
        r[index] = 2*math.sin(math.radians(alph))*(d-l1*math.sin(math.radians(th)))
        s[index] = 2*math.cos(math.radians(th))*l1
        t[index] = -2*math.sin(math.radians(th))*d*l1

        # print("El punto q_{} = {}".format(index+1, q[index]))
        # print("El punto r_{} = {}".format(index+1, r[index]))
        # print("El punto s_{} = {}".format(index+1, s[index]))
        # print("El punto t_{} = {}".format(index+1, t[index]))

        index+=1

    ecu = [[q[0]-q[1],r[0]-r[1],s[0]-s[1],t[0]-t[1]],[q[0]-q[2],r[0]-r[2],s[0]-s[2],t[0]-t[2]]]

    print(q)
    print(r)
    print(s)
    print(t)

    for ec in ecu:
        print(ec)

    # Se define como lambda z' y se obtienen las relaciones respecto a lambda de x' e y'
    # en un vector de (real, lambda)
    z = [0,1]
    x = [(-(t[0]-t[2])-((r[0]-r[2])*(-(t[0]-t[1])))/(r[0]-r[1]))/((q[0]-q[2])-((r[0]-r[2])*(q[0]-q[1])/(r[0]-r[1]))),
         (-(s[0]-s[2])-((r[0]-r[2])*(-(s[0]-s[1])))/(r[0]-r[1]))/((q[0]-q[2])-((r[0]-r[2])*(q[0]-q[1])/(r[0]-r[1])))]
    y = [(-(t[0]-t[1])-x[0]*(q[0]-q[1]))/(r[0]-r[1]),(-(s[0]-s[1])-x[1]*(q[0]-q[1]))/(r[0]-r[1])]

    a_ecu = x[1]**2 + y[1]**2 + z[1]**2
    b_ecu = 2*x[0]*x[1] + 2*y[0]*y[1] + 2*z[0]*z[1] + q[0]*x[1] + r[0]*y[1] + s[0]*z[1]
    c_ecu = l1**2 + d**2 + x[0]**2 + y[0]**2 + z[0]**2 - l2**2 + q[0]*x[0] + r[0]*y[0] + s[0]*z[0] + t[0]

    print("Parametros x,y,z")
    print(x)
    print(y)
    print(z)

    print("Parametros a,b,c de la ecuacion")
    print(a_ecu)
    print(b_ecu)
    print(c_ecu)

    sol_z1 = (-b_ecu+sqrt(b_ecu**2-4*a_ecu*c_ecu))/(-2*a_ecu)
    sol_z2 = (-b_ecu-sqrt(b_ecu**2-4*a_ecu*c_ecu))/(-2*a_ecu)

    print(sol_z1)
    print(sol_z2)

    sol_z = max(sol_z1,sol_z2)
    sol_x = x[0]-sol_z*x[1]
    sol_y = y[0]-sol_z*y[1]

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
pos = inverse_kin([6.977,-3.66,32.487])
print(pos)
print("\n    FORWARD KINEMATICS     \n")
# forward_kin([90,90,90])
forward_kin(pos)
