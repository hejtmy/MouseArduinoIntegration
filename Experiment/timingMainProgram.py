# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:04:39 2016

@author: Smoothie
"""

import time, msvcrt

from winsound import Beep

from arduinoClass import arduino
from experimentDataClass import experimentData
from fileHandlerClass import fileHandler
from windowClass import window

totalPush = 0
pushedOK = 0
experimentStartTime = None
roundStartTime = None

def phase1():
    phaseStartTime = time.clock()
    myWindow.blankWhite()
    myWindow.blinkBlack()

    phase = 1
    while (time.clock() - phaseStartTime <= data.times[0]):
         if (myArduino.isPushed() == True):
            roundTime = time.clock() - roundStartTime
            experimentTime = time.clock() - experimentStartTime
            experimentFile.writeStatusTiming(experimentTime, roundTime, phase, "False")
            global totalPush
            totalPush += 1
            if data.resetAfterPush == True:
                return "END"
            elif data.jumpToEnd == True:
                return "JUMP"
    return 0
    
def phase2():
    phaseStartTime = time.clock()
    Beep(2000, 50)
    
    phase = 2
    while (time.clock() - phaseStartTime <= data.times[1]):
         if (myArduino.isPushed() == True):             
            roundTime = time.clock() - roundStartTime
            experimentTime = time.clock() - experimentStartTime
            experimentFile.writeStatusTiming(experimentTime, roundTime, phase, "True")
            
            global totalPush
            totalPush += 1
            global pushedOK
            pushedOK += 1
            
            if data.resetAfterPush == True:
                return "END"
            elif data.jumpToEnd == True:
                return "JUMP"
    return 0
                
            
def phase3():
    phaseStartTime = time.clock()
    Beep(4000, 50)
    phase = 3
    
    while (time.clock() - phaseStartTime <= data.times[2]):
         if (myArduino.isPushed() == True):
            roundTime = time.clock() - roundStartTime
            experimentTime = time.clock() - experimentStartTime
            experimentFile.writeStatusTiming(experimentTime, roundTime, phase, "False")
            global totalPush
            totalPush += 1
            if data.resetAfterPush == True:
                return "END"
            elif data.jumpToEnd == True:
                return "JUMP"
    return 0
    
        
def singleRound():    
    global roundStartTime
    roundStartTime = time.clock()
    
    p1 = phase1()
    if p1 == "END":
        return
    elif p1 == "JUMP":
        phase3()
        return
        
    p2 = phase2()
    if p2 == "END":
        return
    elif p2 == "JUMP":
        phase3()
        return
    
#    edit, not to react, when moved to phase3
    p3 = phase3()
    if p3 == "END":
        return
    elif p3 == "JUMP":
        phase3()
        
    

def startExperiment():
    experimentFile.writeHeader()

    myArduino.flush()    
    
    myWindow.topmost()
    myWindow.maximize()    
    myWindow.blankWhite()
    
    global experimentStartTime
    experimentStartTime = time.clock()
    
    counter = 0
    while (counter < data.repetitions):
        global roundStartTime
        roundStartTime = time.clock()
        
        singleRound()
        counter += 1
    
    myArduino.reset()
    experimentFile.writeFooter()
    myWindow.closeWindow()
    print("Total push: %d" %totalPush)
    print("Pushed right: %d" %pushedOK)
    msvcrt.getch()

#Beep(1000, 100)
 
myArduino = arduino()
try:
    myArduino.connect()
except Exception as ex:
    print(ex)
    
myArduino.prepare()

#Beep(1500, 100)

data = experimentData()
data.setP("mode3.txt")
data.check()

#Beep(2000, 100)

experimentFile = fileHandler()
experimentFile.setFileName(data.fileName)

myWindow = window()
startExperiment()