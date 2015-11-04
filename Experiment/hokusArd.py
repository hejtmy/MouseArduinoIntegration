import serial
from time import sleep

try:
    ard = serial.Serial("com4", 9600)
    print "connected"
except Exception:
    raise ValueError("bullshit")

def sendStop():
    ard.write("STOP")
    sleep(5)
    ard.write("REPEAT")

while (1==1):
    if (ard.inWaiting()>0):
        x = ard.readline()
        print x
        if (x == "CX37\n"):
            print "TRUE"
            sendStop()
