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



    #Posicion inicial

    Robot.setAngles(30,-10,-20)
    time.sleep(2)

    #Obtención posición base camara respecto centro robot(centro, parte superior)
    pos = Robot.getCameraPosition()
    print(pos)

else:
    print("Failed connection")