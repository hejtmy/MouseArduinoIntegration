#import modules
import subprocess as sp     ##for subprocessing - showing an image
import serial               ##for communication with arduino
import time                 ##for time.clock(), strftime and....
import psutil               ##for subprocessing, closing an image viewer
from random import randint  ##for choosing random image
import os.path              ##for checking if file exists
from Experiment.helpers import isInt             ## custom functions
from Experiment.arduino import connect


##check if file to be created already exists
def fileExists():
    if (os.path.isfile(fileName)==True):
        raise ValueError("FIlE ALREADY EXISTS!!!")

##write file header in specific format
##1st line - "Mouse experiment"
##2nd line - Date and time of creation
##3rd line - Repetitions to be made
##4th line - Free line for further notes
##5th line - Format of data sequence writing
def writeHeader():
    dataFile = open("%s" % fileName, "w")
    dataFile.write("Mouse experiment\n")
    dataFile.write(time.strftime("%d/%m/%y\t%H:%M:%S\n"))
    dataFile.write("Repetitions to be made: %s\n" % str(repeat) )
    dataFile.write("\n")
    dataFile.write("Number\tStatus\tPicture\tTiming\tPhase\tElapsed\n")
    dataFile.close()

##write to file, when button is pushed UNCORRECTLY
##phase argument - during which phase button was pushed (1/2/3)
##elapsed time = timing = time since showing the picture
def writeWrong(phase):
    elapsedTime = now - start               ##time elapsed from showing picture

    dataFile = open("%s" % fileName, "a")   ##open a file
    dataFile.write("%s\t" % str(counter))   ##write number of push
    dataFile.write("False\t")               ##write Status - False

    if (picture == correctPicture):           ##if the right picture was shown
        dataFile.write("True\t")            ##write Picture - True
    else:
        dataFile.write("False\t")           ##write Picture - False

    ###alternative - if (phase == 2):
    if (elapsedTime > (initLag) and elapsedTime < (initLag + imgLag)):
        dataFile.write("True\t")            ##write Timing - True
    else:
        dataFile.write("False\t")           ##write Timing - False
    dataFile.write("%d\t" % phase)          ##write Phase
    dataFile.write("%.2f\t" % elapsedTime)  ##write Elapsed time
    dataFile.write("\n")
    dataFile.close()

##write to file, when button is pushed CORRECTLY
##phase argument - during which phase button was pushed (1/2/3)
##elapsed time = timing = time since showing the picture
def writeOK(phase):
    elapsedTime = now - start;              ##time elapsed from showing picture
    dataFile = open("%s" % fileName, "a")   ##open a file
    dataFile.write("%s\t" % str(counter))   ##write number of push
    dataFile.write("True\t")                ##write Status - True
    dataFile.write("True\t")                ##write Picture - True
    dataFile.write("True\t")                ##write Timing - True
    dataFile.write("%d\t" % phase)          ##write Phase
    dataFile.write("%.2f" % elapsedTime)    ##write Elapsed time
    dataFile.write("\n")
    dataFile.close()

##function for opening an image
##function returns ID of the image process (MS Paint)
def openImg(number):
    global picture          ##global variable, indicating which image was opened
    ##global proc             ##global class proc, asi neni nutne "global"
    if (number == 1):
        proc = sp.Popen("mspaint circle.jpg", shell=True)
        picture = "circle"
    if (number == 2):
        proc = sp.Popen("mspaint square.jpg", shell=True)
        picture = "square"
    if (number == 3):
        proc = sp.Popen("mspaint triangle.jpg", shell=True)
        picture = "triangle"
    return (proc.pid)       ##Proceess ID to be closed with kill() function

def kill(proc_pid):         ##function for killing process of showing picture
    process = psutil.Process(proc_pid)
    for proc in process.get_children(recursive=True):
        proc.kill()
    process.kill()          ##kill the process of showing an image

##for each image to be shown, call this main experiment function
##only argument is randomly generated number, specifying pictre to be opened
def experiment(shape):
    global counter, start, now          ##global variables (now, start -> timing)
    start = time.clock()                ##initialize timing
    processId = openImg(shape)          ##open picture, assign processID value
    now = time.clock()                  ##now = updated timing variable for comparing times
    while ((now-start)<initLag):        ##PHASE 1
        if (ard.inWaiting()>0):
            value = ard.readline()
            if (b'PUSHED' in value):   ##if button was pushed, write it to file
                writeWrong(1);
        time.sleep(0.05)                ##wait 50ms
        now = time.clock()              ##update current time variable
    ##PHASE 1 ENDED
    while ((now - start)< (initLag + imgLag)):  ##PHASE 2
        if (ard.inWaiting()>0):
            value = ard.readline()
            if (b'PUSHED' in value and picture == correctPicture):
                writeOK(2);             ##if button was pushed, write it to file
            else:
                writeWrong(2)
        time.sleep(0.05)                ##wait 50ms
        now = time.clock()              ##update current time variable
    ##PHASE 2 ENDED
    while ((now - start)< (initLag + imgLag + finishLag)): ##PHASE 3
        if (ard.inWaiting()>0):
            value = ard.readline()
            if (b'PUSHED' in value):   ##if button was pushed, write it to file
                writeWrong(3);
        time.sleep(0.05)                ##wait 50ms
        now = time.clock()              ##update current time variable
    ##PHASE 3 ENDED

    kill(processId)                     ##close image = close the process
    counter = counter + 1;              ##increment counter of repetitions


##START THE EXPERIMENT ITSELF - CONNECT TO ARDUINO AND START CALLING FUNCTIONS

connect()                       ##connect to arduino

while (True):                   ##check for code "CX37\n", wait until it is received
    if (ard.inWaiting()>0):
        arduinoText = ard.readline()
        if (b'CX37' in arduinoText): ##if "CX37\n" code is received
            print ("Received code!")
            sendStop()          ##tell it to stop sending "CX37" identification code
            time.sleep(3)       ##sleep for 3 sec
            break               ##break when received "CX37\n"

fileName = input("Name of the file: ")
fileExists()                    ##program exits if the file already exists, otherwise quit

##set up experiment parametres, initialize variables
initLag = input("Duration of PHASE 1 (seconds): ")
imgLag = input("Duration of PHASE 2 (seconds): ")
finishLag = input("Duration of PHASE 3 (seconds): ")
repeat = input("Enter number of repetitions: ")

picture = "square"              ##initialize to random value
correctPicture = "circle"       ##variable - which image is correct
counter = 1                     ##counting repetition number

##check values of phase durations, if wrong value -> quit the program
##check value of imgLag
if (isInt(imgLag)==0 and int(imgLag) > 0):
    imgLag = int(imgLag)
    print ("imgLag set!")
else:
    raise ValueError("Couldn't make imgLag an Int, or less than 0")

##check value of imgLag
if (isInt(initLag)==0 and int(initLag) > 0):
    initLag = int(initLag)
    print ("initLag set!")
else:
    raise ValueError("Couldn't make initLag an Int, or less than 0")

##check value of finishLag
if (isInt(finishLag)==0 and int(finishLag) > 0):
    finishLag = int(finishLag)
    print ("finishLag set!")
else:
    raise ValueError("Couldn't make finishLag an Int, or less than 0")

##check value of repeat
if (isInt(repeat)==0 and int(repeat) > 0):
    repeat = int(repeat)
    print ("Repeat set!")
else:
    raise ValueError("Couldn't make repeat an Int, or less than 0")



writeHeader()                   ##write file header

while (ard.inWaiting()>0):      ##flush previous pushed signals
    ard.read()

time.sleep(3)                   ##prepare for the experiment

for i in range(repeat):         ##call experiment function "repeat" times
    shapeNumber = randint(1,3)  ##random picture choice, passed to function
    experiment(shapeNumber)     ##call experiment main function

    ##ADD -> flush PUSHED signals received between images!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

sendReset()                     ##reset Arduino, start sending "CX37\n again"
print ("Experiment ran succesfully, Arduino reseted!")
