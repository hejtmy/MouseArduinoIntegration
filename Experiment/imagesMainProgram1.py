# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 21:32:16 2016

@author: Smoothie
"""
import time

from winsound import Beep

from arduinoClass import arduino
from experimentDataClass import experimentData
from fileHandlerClass import fileHandler
from windowClass import window

myArduino = arduino()
myArduino.connect()
myArduino.prepare()

data = experimentData()
data.setParametres()

data.checkValues()

experimentFile = fileHandler()
experimentFile.setFileName(data.fileName)

myWindow = window()

def singleRound(number):    
    index = data.imagesOrder[number]
    image = data.images[index]
    data.currentImage = image
    myWindow.setImage(image)
    
    clockStart = time.clock()
    
#    file structure: Time / Correct Time / Correct Image / Phase when pushed / Feeding
    Beep(500, 100)
#    first segment
    while( (time.clock() - clockStart) < data.times[0]):
        if (myArduino.isPushed() == True):
            timer = time.clock() - clockStart
            
            if (data.correctImage == data.currentImage):
                experimentFile.writeStatus(timer,"False","True", 1, "False")
            else:
                experimentFile.writeStatus(timer,"False","False", 1, "False")
        
            
    Beep(1000, 100)
#    second segment
    while( (time.clock() - clockStart) < (data.times[0] + data.times[1])):
        if (myArduino.isPushed() == True):
            timer = time.clock() - clockStart
                
            if (data.correctImage == data.currentImage):
                experimentFile.writeStatus(timer,"True","True", 2, "True")
                myArduino.feedMouse()
            else:
                experimentFile.writeStatus(timer,"True","False", 2, "False")

    
    Beep(2000, 100)            
#    third segment
    while( (time.clock() - clockStart) < (data.times[0] + data.times[1] + data.times[2])):
        if (myArduino.isPushed() == True):
            timer = time.clock() - clockStart
            
            if (data.correctImage == data.currentImage):
                experimentFile.writeStatus(timer,"False","True", 3, "False")
            else:
                experimentFile.writeStatus(timer,"False","False", 3, "False")
                
#    while( (time.clock() - clockStart) < data.totalTime):
#        if (myArduino.isPushed() == True):
#            if (data.times[0] < time.clock() - clockStart < (data.times[0] + data.times[1])):
#                correctTime = "True"
#            else:
#                correctTime = "False"
#            
#            if (data.correctImage == data.currentImage):
#                correctImage = "True"
#            else:
#                correctImage = "False"
#            
#            timer = time.clock() - clockStart
#            if (timer < data.times[0]):
#                phase = 1
#            elif (timer < (data.times[0] + data.times[1])):
#                phase = 2
#            else:
#                phase = 3
#            
#            if (correctTime == "True" and correctImage == "True"):
#                feeding = "True"
##                myArduino.feedMouse()
#            else:
#                feeding = "False"
#            
#            experimentFile.writeStatus(timer,correctTime, correctImage, phase, feeding)
    
def startExperiment():
    experimentFile.writeHeader()

    myArduino.flush()    
    
    myWindow.topmost()
    myWindow.maximize()    
    
    counter = 0
    while (counter < data.repetitions):
        singleRound(counter)
        counter += 1
    
    myArduino.reset()
    experimentFile.writeFooter()
    myWindow.closeWindow()
    
startExperiment()