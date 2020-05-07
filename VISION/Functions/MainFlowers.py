from Daisy import *
from Test import *
from Dandelion import *
from Tulip import *
from Sunflower import *
#get the image
img = cv.imread(cv.samples.findFile("Tulip3.jpg"))
if img is None:
    sys.exit("Could not read the image.")
#DaisyStatus(img)
#SunflowerStatus(img)
TulipStatus(img)
#DandelionStatus(img)

#Test(img)
