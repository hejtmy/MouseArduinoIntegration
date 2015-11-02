#import modules
import subprocess as sp ##import for subprocessing, show an image
import serial ##for communication with arduino
import time ##for time.clock() feature
import psutil ##import for subprocessing, closing an image viewer

##set up experiment variables and parametres
initLag = raw_input("Enter lag to start after showing image (seconds): ")
imgLag = raw_input("Enter lag between images (seconds): ")
finishLag = raw_input("Enter lag to start after showing image (seconds): ")
picture = "square" ##variable - which image was shown
rightPicture = "circle" ##variable - which image is right
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

##try communication with arduino, wait until specific code "XX37" is received
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
##            break

##begin the experiment
##proces skenuje jestli arduino poslalo zaznam o zmacknuti
##potrebuju stopky, musim zaznamenat vsechny stisky s presnosti na 100ms
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
    if (number ==2):
        proc = sp.Popen("mspaint square.jpg", shell=True)
        picture = "square"
    return (proc.pid) ##return number of proceess ID

##pokazde spustit funkci pro kazdy obrazek
def experiment(shape):
    start = time.clock() ##initialize timer
    processId = openImg(shape) ##open picture
    now = time.clock()
    while ((now-start)<initLag): ##wrong time
        now = time.clock()
##        if (ard.inWaiting()>0):
##            value = ard.readline()
##            if (value == "pushed"):
##                writeWrong();
    print ("phase 1 ended, time from beginning is %.3fs" % (now - start))
    while ((now - start)< (initLag + imgLag)):
        now = time.clock()
##        if (ard.inWaiting()>0):
##            value = ard.readline()
##            if (value == "pushed" and picture == desired shape):
##                writeRight();
    kill(processId)

