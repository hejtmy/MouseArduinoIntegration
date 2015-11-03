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

##try communication with arduino, wait until specific code "XX37" is received, NEVYZKOUSENO
##try:
##    ard = serial.Serial("COM4", 9600)
##except Exception:
##    raise ValueError("Couldn't connect to Arduino")
##
####flush buffer
##while (ard.inWaiting>0):
##    ard.read() ##takhle?
##
####wait, until arduino sends again the "XX37" code
##while (True):
##    if (ard.inWaiting()>0):
##        arduinoText = ard.readline()
##        if (arduinoText == "XX37"):
##            print "communication with arduino OK"
####            Let arduino know to stop sending code XX37!
##            break
def fileExists():
    if (os.path.isfile(fileName)==True):
        raise ValueError("FIlE ALREADY EXISTS!!!")        

def writeHeader():
    dataFile = open("%s" % fileName, "w")
    dataFile.write("Mouse experiment\n")
    dataFile.write(time.strftime("%d/%m/%y\t%H:%M:%S\n"))
    dataFile.write("Repetitions to be made: %s\n" % str(repeat) )
    dataFile.write("\n")
    dataFile.write("Number\tStatus\tPicture\tTiming\n")
    dataFile.close()
    
def writeWrong():
    dataFile = open("%s" % fileName, "a")
    dataFile.write("%s\t" % str(counter))
    dataFile.write("False\t")
    
    if (picture == rightPicture):
        dataFile.write("True\t")
    else:
        dataFile.write("False\t")

    if ((now - start) > (initLag + 0.001) and (now - start) < (initLag + imgLag)):
        dataFile.write("True\t")
    else:
        dataFile.write("False\t")
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
    global start, now, counter
    start = time.clock() ##initialize timer
    processId = openImg(shape) ##open picture
    now = time.clock()
    while ((now-start)<initLag): ##wrong time
        now = time.clock()
##        if (ard.inWaiting()>0):
##            value = ard.readline()
##            if (value == "pushed"):
##                writeWrong();
##    print ("phase 1 ended, time from beginning is %.3fs" % (now - start))

    writeWrong() ##pokusne zapsat do souboru
    while ((now - start)< (initLag + imgLag)):
        now = time.clock()
##        if (ard.inWaiting()>0):
##            value = ard.readline()
##            if (value == "pushed" and picture == rightPicture):
##                writeRight();
##    if (picture == rightPicture):
##        print ("Right picture during phase 2 shown")
    while ((now - start)< (initLag + imgLag + finishLag)):
        now = time.clock()
##        if (ard.inWaiting()>0):
##            value = ard.readline()
##            if (value == "pushed"):
##                writeRight();
    kill(processId) ##close image
    counter = counter + 1; ##increment counter of repetitions

##begin experiment itself - call experiment function
fileExists() ##check for file existance
writeHeader() ##write file header
for i in range(repeat):
    shapeNumber = randint(1,3)
    experiment(shapeNumber)
print ("Experiment ran succesfully!")
