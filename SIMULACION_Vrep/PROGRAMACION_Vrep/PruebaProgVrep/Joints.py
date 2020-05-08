import math
import vrep
import time

class Join:

    # Attributes
    handle = 0
    position = 0
    velocity = 0
    clientID = 0
    Sentido = 1 #1: Antihorario -1: horario
    Cero = 0

    def __init__(self, name,client,sentido,cero):
        self.setJointHandle(name)
        self.setClientID(client)
        self.Cero = cero
        self.Sentido = sentido

    def setClientID(self, clientID):
        self.clientID = clientID

    def setJointHandle(self, name):
        r, self.handle = vrep.simxGetObjectHandle(self.clientID, name, vrep.simx_opmode_oneshot_wait)

    def setJointPosition(self, pos):

        self.position = self.Sentido * (pos - self.Cero)
        vrep.simxSetJointTargetPosition(self.clientID, self.handle, self.position * math.pi / 180, vrep.simx_opmode_oneshot)



    def getJointPosition (self):
        ret, position = vrep.simxGetJointPosition(self.clientID, self.handle, vrep.simx_opmode_streaming)
        self.position = math.degrees(position)

    def setJointVelocity(self, vel):
        self.velocity = vel
        ret = vrep.simxSetObjectFloatParameter(self.clientID, self.handle, vrep.sim_jointfloatparam_upper_limit, self.velocity,
                                               vrep.simx_opmode_oneshot)
        #ret = vrep.simxSetJointTargetVelocity(self.clientID, self.handle, self.velocity, vrep.simx_opmode_oneshot_wait)


        # Tenia puesto simx_opmode_streaming en el script de la prueba, en internet recomienda oneshot
