#import modules
import subprocess as sp     ##for subprocessing - showing an image
import time                 ##for time.clock(), strftime and....
import psutil               ##for subprocessing, closing an image viewer
from random import randint  ##for choosing random image
from Experiment.helpers import isInt, kill             ## custom functions
from Experiment.arduino_class import Arduino
from Experiment.write_class import WriteClass,WriteClassSpecificExperiment
from Experiment.experiment_class import Experiment

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
                writer.writeWrong(1);
        time.sleep(0.05)                ##wait 50ms
        now = time.clock()              ##update current time variable
    ##PHASE 1 ENDED
    while ((now - start)< (initLag + imgLag)):  ##PHASE 2
        if (ard.inWaiting()>0):
            value = ard.readline()
            if (b'PUSHED' in value and picture == correctPicture):
                writer.writeOK(2);             ##if button was pushed, write it to file
            else:
                writer.writeWrong(2)
        time.sleep(0.05)                ##wait 50ms
        now = time.clock()              ##update current time variable
    ##PHASE 2 ENDED
    while ((now - start)< (initLag + imgLag + finishLag)): ##PHASE 3
        if (ard.inWaiting()>0):
            value = ard.readline()
            if (b'PUSHED' in value):   ##if button was pushed, write it to file
                writer.writeWrong(3);
        time.sleep(0.05)                ##wait 50ms
        now = time.clock()              ##update current time variable
    ##PHASE 3 ENDED

    kill(processId)                     ##close image = close the process
    counter = counter + 1;              ##increment counter of repetitions

###SETUP
arduino = Arduino();
#sets up arduino
while (True):
    try:
        arduino.connect();
    except ConnectionError as con_err:
        print(con_err);
        #maybe allow to reinstantite arduino or change te port values
        continue
    #this below might be redundant - need to check the pySerial doc what happens in Open stream,
    #if it returns true, then we can just break the code
    if arduino.is_connected():
        ##if "CX37\n" code is received we break the cycle and
        arduinoText = arduino.readline();
        if (b'CX37' in arduinoText):
            print ("Received code!")
            arduino.sendConnectionOK()          ##tell it to stop sending "CX37" identification code
            time.sleep(3)
            break

###Program logic
fileName = input("Name of the file: ")
##program exits if the file already exists, otherwise quit
writer = WriteClass(fileName);
while not writer.isOpen():
    writer.openFile();


experiment = Experiment()
##set up experiment parametres, initialize variables
experiment.setup()

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



writer.writeHeader()                   ##write file header

while (ard.inWaiting()>0):      ##flush previous pushed signals
    ard.read()

time.sleep(3)                   ##prepare for the experiment

for i in range(repeat):         ##call experiment function "repeat" times
    shapeNumber = randint(1,3)  ##random picture choice, passed to function
    experiment(shapeNumber)     ##call experiment main function

    ##ADD -> flush PUSHED signals received between images!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

arduino.sendReset();                     ##reset Arduino, start sending "CX37\n again"
print ("Experiment ran succesfully, Arduino reseted!")




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

