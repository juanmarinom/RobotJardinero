from Daisy import *
from Dandelion import *
from Tulip import *
from Sunflower import *
from Rose import *


def Flower(img, flower):



    Health = None
    LeafDens = None

    if (flower == 0):
        Health, LeafDens = DaisyStatus(img)

    elif (flower == 1):
        Health, LeafDens = DandelionStatus(img)

    elif (flower == 2):
        Health, LeafDens = RoseStatus(img)

    elif (flower == 3):
        Health, LeafDens = SunflowerStatus(img)

    elif (flower == 4):
        Health, LeafDens = TulipStatus(img)

    else:
        print("Could not read the image or number not expected.")

    #escribo health y LeafDens en la base de datos
    return