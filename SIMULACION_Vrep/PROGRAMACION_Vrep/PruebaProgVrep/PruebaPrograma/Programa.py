import vrep
import time
import math

# Vrep connection
vrep.simxFinish(-1) # Ending of previous communication open
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)


if clientID != -1:
    print("Connection succeed")
    returnCode2, handle2 = vrep.simxGetObjectHandle(clientID, 'div_join_1', vrep.simx_opmode_oneshot_wait)
    print(handle2)
    actualPos = vrep.simxGetJointPosition(clientID, handle2,vrep.simx_opmode_oneshot)
    print(actualPos)
    actualPos = vrep.simxSetJointTargetVelocity(clientID,handle2,0.5,vrep.simx_opmode_oneshot_wait)
    actualPos = vrep.simxGetJointPosition(clientID, handle2, vrep.simx_opmode_oneshot)
    print(actualPos)




else:
    print("Failed connection")