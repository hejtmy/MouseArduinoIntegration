import serial, os, string, random, time

import arduinoClass, inputDataClass, fileHandlerClass, experimentClass


MyArduino = Arduino()
MyArduino.connect()
MyArduino.prepareForExperiment()
#ready for an experiment
#MyArduino.resetArduino()

dataFile = fileHandler("givenFileName")
dataFile.createFile()
dataFile.writeHeader()
dataFile.write(time.clock(),"False","True")
dataFile.closeFile()

data = inputData()
data.getTimes()
data.getReps()
data.getFileName()

events order:
1 - Establish connection with arduino
2 - Get data from user - file name, reps, times
3 - Create file for writing data / error if it exists, write the file header
4 - Check with user if the right pictures are to be shown
5 - Prepare for experiment -  flush signals, set correct Image etc
5.5 - PRINT ALL SET DATA TO USER, AND CHECK VALIDITY
6 - Initiate black / blank tkinter window
7 - Start experiment function
    For every picture shown:
        change current image
        start timer for that picture
        for each phase:
            check constantly for signal from arduino
            if signal is received:
                write it to file
            check constantly the timer
8 - after experiment is finished
        change the img to blank / close it
        reset arduino