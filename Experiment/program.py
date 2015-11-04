#import modules
import subprocess as sp ##import for subprocessing, show an image
import serial ##for communication with arduino
import time ##for time.clock(), strftime and....
import psutil ##import for subprocessing, closing an image viewer
from random import randint
import os.path
##set up experiment variables and parametres
initLag = raw_input("Enter lag to start after showing image (seconds): ")
imgLag = raw_input("Enter lag between images (seconds): ")
finishLag = raw_input("Enter lag to start after showing image (seconds): ")
picture = "square" ##variable - which image was shown
rightPicture = "circle" ##variable - which image is right
repeat = raw_input("Enter number of repetitions: ")
fileName = raw_input("Name of the file: ")##check for alreadz existing file
counter = 1
##write functions for checking correct inputs from user - delays
##check value of variables
def isInt(value):
    try:
        int(value)
    except Exception:
        return -1
    return 0
##imglag
if (isInt(imgLag)==0 and int(imgLag) > 0):
    imgLag = int(imgLag)
    print "imgLag set!"
else:
##  print "Couldn't make imgLag an Int, or less than 0"
    raise ValueError("imgLag is bullshit")
##nitLag
if (isInt(initLag)==0 and int(initLag) > 0):
    initLag = int(initLag)
    print "initLag set!"
else:
    print "Couldn't make imgLag an Int, or less than 0"
##finishlag
if (isInt(finishLag)==0 and int(finishLag) > 0):
    finishLag = int(finishLag)
    print "initLag set!"
else:
    print "Couldn't make imgLag an Int, or less than 0"
##repeat
if (isInt(repeat)==0 and int(repeat) > 0):
    repeat = int(repeat)
    print "Repeat set!"
else:
    print "Couldn't make repeat an Int, or less than 0"


def fileExists():
    if (os.path.isfile(fileName)==True):
        raise ValueError("FIlE ALREADY EXISTS!!!")
    
def connect():
    ##try communication with arduino, wait until specific code "CX37" is received, NEVYZKOUSENO
    global ard
    try:
        ard = serial.Serial("COM4", 9600)
    except Exception:
        raise ValueError("Couldn't connect to Arduino")

    ##wait, until arduino sends again the "XX37" code
def sendStop():
    ard.write("STOP")

def sendReset():
    ard.write("REPEAT")

def writeHeader():
    dataFile = open("%s" % fileName, "w")
    dataFile.write("Mouse experiment\n")
    dataFile.write(time.strftime("%d/%m/%y\t%H:%M:%S\n"))
    dataFile.write("Repetitions to be made: %s\n" % str(repeat) )
    dataFile.write("\n")
    dataFile.write("Number\tStatus\tPicture\tTiming\tPhase\n")
    dataFile.close()
    
def writeWrong(phase):
    dataFile = open("%s" % fileName, "a")
    dataFile.write("%s\t" % str(counter))
    dataFile.write("False\t")
    
    if (picture == rightPicture):
        dataFile.write("True\t")
    else:
        dataFile.write("False\t")

    if ((now - start) > (initLag) and (now - start) < (initLag + imgLag)):
        dataFile.write("True\t")
    else:
        dataFile.write("False\t")
    dataFile.write("%d" %phase)
    dataFile.write("\n")
    dataFile.close()

def writeOK(phase):
    dataFile = open("%s" % fileName, "a")
    dataFile.write("%s\t" % str(counter))
    dataFile.write("True\t") ##status
    dataFile.write("True\t") ##img
    dataFile.write("True\t") ##timing
    dataFile.write("%d" % phase) ##timing
    dataFile.write("\n")
    dataFile.close()
    
def kill(proc_pid): ##function for killing process of showing picture
    process = psutil.Process(proc_pid)
    for proc in process.get_children(recursive=True):
        proc.kill()
    process.kill()

def openImg(number): ##open image function, returns image viewer process ID
    global picture ##global variable, indicating which image was opened
    global proc
    if (number == 1):
        proc = sp.Popen("mspaint circle.jpg", shell=True)
        picture = "circle"
    if (number == 2):
        proc = sp.Popen("mspaint square.jpg", shell=True)
        picture = "square"
    if (number == 3):
        proc = sp.Popen("mspaint triangle.jpg", shell=True)
        picture = "triangle"
    return (proc.pid) ##return number of proceess ID

##pokazde spustit funkci pro kazdy obrazek
def experiment(shape):
    print "Img shown!"
    global counter, start, now
    start = time.clock() ##initialize timer
    processId = openImg(shape) ##open picture
    now = time.clock()
    while ((now-start)<initLag): ##wrong time
        now = time.clock()
        if (ard.inWaiting()>0):
            value = ard.readline()
            if (value == "PUSHED\n"):
                writeWrong(1);
        time.sleep(0.05)
    print "Phase 1 ended"
    while ((now - start)< (initLag + imgLag)):
        if (ard.inWaiting()>0):
            value = ard.readline()
            if (value == "PUSHED\n" and picture == rightPicture):
                writeOK(2);
            else:
                writeWrong(2)
        now = time.clock()
        time.sleep(0.05)
    print "Phase 2 ended"
    while ((now - start)< (initLag + imgLag + finishLag)):
        if (ard.inWaiting()>0):
            value = ard.readline()
            if (value == "PUSHED\n"):
                writeWrong(3);
        now = time.clock()
        time.sleep(0.05)
    print "Phase 3 ended"
    
    kill(processId) ##close image
    counter = counter + 1; ##increment counter of repetitions

##begin experiment itself - onnect to arduino and call experiment function

connect() ##connect to arduino
sendStop()

while (True):  ##check for code CX37\n
    if (ard.inWaiting()>0):
        arduinoText = ard.readline()
        if (arduinoText == "CX37\n"):
            print "communication with arduino OK"
            sendStop()
            time.sleep(3)
            break ##break when received "CX37\n"

fileExists() ##check for file existance
writeHeader() ##write file header

##flush previous pushed signals
while (ard.inWaiting()>0):
    ard.read()
    
for i in range(repeat): ##experiment itself
    shapeNumber = randint(1,3) ##random picture choice
    experiment(shapeNumber)

sendReset()
print ("Reset arduino!")
