import vrep
import time
import math
import DeltaJardinero
# Vrep connection
vrep.simxFinish(-1) # Ending of previous communication open
clientID = vrep.simxStart('127.0.0.1', 3999, True, True, 5000, 5)
vrep.simxSynchronous(clientID, True)

if clientID != -1:
    print("Connection succeed")
    Robot = DeltaJardinero.Delta('div_join_1', 'div_join_2', 'div_join_3',1, -1, 1, 24, 24, 24, clientID)
    # Set initial angles
    #r, handle1 = vrep.simxGetObjectHandle(clientID, 'div_join_1', vrep.simx_opmode_oneshot_wait)
    #print(handle1)
    #vrep.simxSynchronous(clientID, True)
    #Robot.setVelocity(0.5, 0.5, 0.5)

    #Posicion inicial

    Robot.setAngles(40,10,10)
    time.sleep(2)
    #vrep.simxSynchronousTrigger(clientID)



    #ret = vrep.simxSetObjectFloatParameter(clientID, handle1, vrep.sim_jointfloatparam_upper_limit, velocity, vrep.simx_opmode_oneshot)
    #time.sleep(0.5)
    #vrep.simxSetJointTargetPosition(clientID, handle1, angle * math.pi / 180, vrep.simx_opmode_oneshot)
    #time.sleep(1)

    #vrep.simxSynchronousTrigger(clientID)
    #time.sleep(1)
    #print(POS)
    #time.sleep(1)

else:
    print("Failed connection")