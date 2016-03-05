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

pressesTotal = 0
pressesCorrect = 0

experimentStartTime = None
roundStartTime = None

def phase1():
#    Beep(1000, 200)
    phaseStartTime = time.clock()
    myWindow.blankBlack()
    if data.beep == True:
        Beep(1000, data.beepLength)
        
    myWindow.blinkWhite()
    phase = 1
    while (time.clock() - phaseStartTime <= data.times[0]):
        if (myArduino.isPushed() == True):
            roundTime = time.clock() - roundStartTime
            experimentTime = time.clock() - experimentStartTime
            experimentFile.writeStatusTiming(experimentTime, roundTime, phase, "False")
            
            global pressesTotal
            pressesTotal += 1
            
            if data.resetAfterPush == True:
                return "END"
            elif data.jumpToEnd == True:
                return "JUMP"
        time.sleep(0.01)
    return 0
    
def phase2():
    phaseStartTime = time.clock()
#    Beep(2000, 50)
    
    phase = 2
    while (time.clock() - phaseStartTime <= data.times[1]):
        if (myArduino.isPushed() == True):             
            roundTime = time.clock() - roundStartTime
            experimentTime = time.clock() - experimentStartTime
            experimentFile.writeStatusTiming(experimentTime, roundTime, phase, "True")
            myArduino.feedMouse()
            
            global pressesTotal
            pressesTotal += 1
            global pressesCorrect
            pressesCorrect += 1
            
            if data.resetAfterPush == True:
                return "END"
            elif data.jumpToEnd == True:
                return "JUMP"
        time.sleep(0.01)
    return 0
                
            
def phase3(react = True):
    phaseStartTime = time.clock()
#    Beep(4000, 50)
    phase = 3
    
    while (time.clock() - phaseStartTime <= data.times[2]):
        if (myArduino.isPushed() == True):
            roundTime = time.clock() - roundStartTime
            experimentTime = time.clock() - experimentStartTime
            experimentFile.writeStatusTiming(experimentTime, roundTime, phase, "False")
            global pressesTotal
            pressesTotal += 1
            
            if react == True:
                if data.resetAfterPush == True:
                    return "END"
                elif data.jumpToEnd == True:
                    return "JUMP"        
        time.sleep(0.01)
    return 0
    
        
def singleRound():    
    global roundStartTime
    roundStartTime = time.clock()
    
    p1 = phase1()
    if p1 == "END":
        return
    elif p1 == "JUMP":
        phase3(react = False)
        return
        
    p2 = phase2()
    if p2 == "END":
        return
    elif p2 == "JUMP":
        phase3(react = False)
        return
    
#    edit, not to react, when moved to phase3
    p3 = phase3()
    if p3 == "END":
        return
    elif p3 == "JUMP":
        phase3()
        
    

def startExperiment():
    experimentFile.writeHeader(data.times, data.totalTime, data.repetitions) #*data.times should send 3 ints, it should unpack the list

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

    myWindow.closeWindow()    
    myArduino.reset()
    experimentFile.writeFooter()
    experimentFile.write("PRESSESTOTAL=%d" %pressesTotal)
    experimentFile.write("PRESSESCORRECT=%d" %pressesCorrect)
    
    print("\nTotal push: %d" %pressesTotal)
    print("Pushed right: %d" %pressesCorrect)
    time.sleep(5)
#    msvcrt.getch()


 
myArduino = arduino()
myArduino.connect()
myArduino.prepare()
#Beep(1500, 100)

data = experimentData()
name = input("File with settings: ")
data.setP(name)
data.check()
#Beep(2000, 100)

experimentFile = fileHandler()
experimentFile.setFileName(data.fileName) #pass the fileName to fileHandler

myWindow = window()

startExperiment()