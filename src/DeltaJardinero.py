import sys
sys.path.insert(1, '../')

import math
import vrep
import Joints as motor

class Delta:

    clientID = 0
    # Funcion que coge el valor de los handle de los motores para cada pata
    def __init__(self, name0, name1, name2, sentido1, sentido2, sentido3, cero1, cero2, cero3, clientID):
        self.clientID = clientID

        self.m0 = motor.Join(name0, clientID, sentido1, cero1)
        self.m1 = motor.Join(name1, clientID, sentido2, cero2)
        self.m2 = motor.Join(name2, clientID, sentido3, cero3)

        self.vectorAngles = []

        self.vectorAngles.append(self.m0.position)
        self.vectorAngles.append(self.m1.position)
        self.vectorAngles.append(self.m2.position)



        self.vectorPosition = []



        vrep.simxSynchronousTrigger(clientID)







    def getJointPosition(self):
        self.m0.getJointPosition()
        self.m1.getJointPosition()
        self.m2.getJointPosition()



    # This function sets the position of the Delta motors

    def setAngles(self, a0, a1, a2):
        self.vectorAngles = [a0, a1, a2]

        self.m0.setJointPosition(self.vectorAngles[0])
        self.m1.setJointPosition(self.vectorAngles[1])
        self.m2.setJointPosition(self.vectorAngles[2])





    def getAngles(self):

        self.m0.getJointPosition()
        self.m1.getJointPosition()
        self.m2.getJointPosition()


        self.vectorAngles = [self.m0.position, self.m1.position, self.m2.position]

        return self.vectorAngles

    def setVelocity(self, v0, v1, v2):
        if v0 != -1:
            self.m0.setJointVelocity(v0) #self.m0.setJointVelocity(v0, 21)
        if v1 != -1:
            self.m1.setJointVelocity(v1)
        if v2 != -1:
            self.m2.setJointVelocity(v2)

    def getCameraPosition(self):

        r, BaseCamara = vrep.simxGetObjectHandle(self.clientID, 'BASECAMARA_respondable', vrep.simx_opmode_oneshot_wait)
        r, BaseRobot = vrep.simxGetObjectHandle(self.clientID, 'Cuboid2', vrep.simx_opmode_oneshot_wait)

        r,position = vrep.simxGetObjectPosition(self.clientID, BaseCamara, BaseRobot, vrep.simx_opmode_oneshot_wait)
        return position
