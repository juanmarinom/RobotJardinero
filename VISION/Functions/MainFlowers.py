import random

from Daisy import *
from Dandelion import *
from Tulip import *
from Sunflower import *
from Rose import *

def Flower(flower):

    Health = None
    LeafDens = None
    path = './Flores_Aptas/'
    n = 5
    if (flower == 0):
        dir = 'Daisy/'
        num = random.randint(1,n)
        img = cv.imread(path + dir + 'Daisy' + str(num) + '.jpg')
        return DaisyStatus(img)

    elif (flower == 1):
        dir = 'Dandelion/'
        num = random.randint(1, n)
        img = cv.imread(path + dir + 'Dandelion' + str(num) + '.jpg')
        return DandelionStatus(img)

    elif (flower == 2):
        dir = 'Rose/'
        num = random.randint(1, n)
        img = cv.imread(path + dir + 'Rose' + str(num) + '.jpg')
        return RoseStatus(img)

    elif (flower == 3):
        dir = 'Sunflower/'
        num = random.randint(1, n)
        img = cv.imread(path + dir + 'Sunflower' + str(num) + '.jpg')
        return SunflowerStatus(img)

    elif (flower == 4):
        dir = 'Tulip/'
        num = random.randint(1, n)
        img = cv.imread(path + dir + 'Tulip' + str(num) + '.jpg')
        return TulipStatus(img)

    else:
        print("Could not read the image or number not expected.")
        return