# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 21:32:16 2016

@author: Smoothie
"""
import time

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
    while( (time.clock() - clockStart) < data.totalTime):
        if (myArduino.isPushed() == True):
            if (data.times[0] < time.clock() - clockStart < (data.times[0] + data.times[1])):
                correctTime = "True"
            else:
                correctTime = "False"
            
            if (data.correctImage == data.currentImage):
                correctImage = "True"
            else:
                correctImage = "False"
            
            timer = time.clock() - clockStart
            if (timer < data.times[0]):
                phase = 1
            elif (timer < (data.times[0] + data.times[1])):
                phase = 2
            else:
                phase = 3
            
            if (correctTime == "True" and correctImage == "True"):
                feeding = "True"
                myArduino.feedMouse()
            else:
                feeding = "False"
            
            experimentFile.writeStatus(timer,correctTime, correctImage, phase, feeding)
#            break
    
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