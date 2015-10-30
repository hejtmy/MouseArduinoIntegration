##set up program parametres

#import everything
import subprocess as sp
import serial
from time import sleep
##set up

imgLag = raw_input("Enter lag between images (seconds): ")
initLag = raw_input("Enter lag to start after showing image (seconds): ")
finishLag = raw_input("Enter lag to start after showing image (seconds): ")

##check value of variables
def isInt(value):
    try:
        int(value)
    except Exception:
        return -1
    return 0

if (isInt(imgLag)==0 and int(imgLag) > 0):
    imgLag = int(imgLag)
    print "imdLag set!"
else:
    print "Couldn't make imgLag an Int, or less than 0"

if (isInt(initLag)==0 and int(initLag) > 0):
    initLag = int(initLag)
    print "initLag set!"
else:
    print "Couldn't make imgLag an Int, or less than 0"

sleep(2)
##blah blah
##try communication with arduino, wait until specific code "XX37" is received
try:
    ard = serial.Serial("COM4", 9600)
except Exception:
    raise ValueError("Couldn't connect to Arduino")

while (True):
    if (ard.inWaiting()>0):
        arduinoText = ard.readline()
        if arduinoText = 
    
