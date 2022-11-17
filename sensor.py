import random
import math

lnumb = 0

def GetSensorValue():
    global lnumb
    returnVal = math.sin(lnumb)
    lnumb += math.pi / 60
    returnVal += random.random()/20
    returnVal = returnVal*3 + 25
    return returnVal