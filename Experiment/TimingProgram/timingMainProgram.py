# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:04:39 2016

@author: Smoothie
"""

import time, msvcrt, sys

from winsound import Beep

from arduinoClass import arduino
from experimentDataClass import experimentData
from fileHandlerClass import fileHandler
from windowClass import window

#counters of presses
pressesTotal = 0
pressesCorrect = 0

experimentStartTime = None
roundStartTime = None

roundCounter = 0

def phase1():
    phaseStartTime = time.clock()
    myWindow.black()     
    myWindow.blinkWhite()
    
    phase = 1
    while (time.clock() - phaseStartTime <= data.times[0]): #time[0] = phase 1 time
        if (myArduino.isPushed() == True): #if pushed
            experimentTime = time.clock() - experimentStartTime            
            roundTime = time.clock() - roundStartTime
            phaseTime = time.clock() - phaseStartTime
            experimentFile.writeStatusTiming(roundCounter, phase, experimentTime, roundTime, phaseTime)
            
            global pressesTotal
            pressesTotal += 1
            
            if (data.mode == "FIX1" or data.mode == "FIX2"):
                pass
            if (data.mode == "DRL1" or data.mode == "DRL2"):
                print(data.mode)
                return "END"
        time.sleep(0.01)
    print("phase 1 mode: ", data.mode)
    return 0
    
def phase2():
    phaseStartTime = time.clock()
#    Beep(2000, 50)
    phase = 2
    
    while (time.clock() - phaseStartTime <= data.times[1]): #times[1] = phase 2 time
        if (myArduino.isPushed() == True):             
            experimentTime = time.clock() - experimentStartTime            
            roundTime = time.clock() - roundStartTime
            phaseTime = time.clock() - phaseStartTime
            experimentFile.writeStatusTiming(roundCounter, phase, experimentTime, roundTime, phaseTime)
            myArduino.feedMouse()
            
            global pressesTotal
            pressesTotal += 1
            global pressesCorrect
            pressesCorrect += 1
            
            if (data.mode == "FIX1" or data.mode == "DRL1"):
                pass
            if (data.mode == "FIX2" or data.mode == "DRL2"):
                return "JUMP"
        time.sleep(0.01)
    return 0
                
            
def phase3():
    phaseStartTime = time.clock()
    Beep(4000, 50)
    phase = 3
    
    while (time.clock() - phaseStartTime <= data.times[2]):
        if (myArduino.isPushed() == True):
            experimentTime = time.clock() - experimentStartTime            
            roundTime = time.clock() - roundStartTime
            phaseTime = time.clock() - phaseStartTime
            experimentFile.writeStatusTiming(roundCounter, phase, experimentTime, roundTime, phaseTime)
            
            global pressesTotal
            pressesTotal += 1
            
            if (data.mode == "FIX1" or data.mode == "FIX2"):
                pass
            if (data.mode == "DRL1" or data.mode == "DRL2"):
                return "END"
        time.sleep(0.01)
    return 0
    
        
def singleRound():    
    global roundStartTime
    roundStartTime = time.clock()
    
    p1 = phase1()
    if p1 == "END":
        return
        
    p2 = phase2()
    if p2 == "END":
        return
    elif p2 == "JUMP":
        phase3()
        return
    
    p3 = phase3()
    if p3 == "END":
        return
        


def startExperiment():
    experimentFile.writeHeader(data.mode, data.times, data.totalTime, data.repetitions) #*data.times should send 3 ints, it should unpack the list

    myArduino.flush()    
    
    myWindow.topmost()
    myWindow.maximize()    
    myWindow.white()
    
    global experimentStartTime
    experimentStartTime = time.clock()
    
    global roundCounter
    roundCounter = 1
    while (roundCounter <= data.repetitions):
        global roundStartTime
        roundStartTime = time.clock()
        
        singleRound()
        roundCounter += 1

    myWindow.closeWindow()    
#    myArduino.reset()
    experimentFile.writeFooter()
    experimentFile.write("PRESSESTOTAL=%d" %pressesTotal)
    experimentFile.write("PRESSESCORRECT=%d" %pressesCorrect)
    
    print("\nTotal push: %d" %pressesTotal)
    print("Pushed right: %d" %pressesCorrect)
    msvcrt.getch()
#    sys.exit(0)


 
myArduino = arduino()
myArduino.connect()
myArduino.prepare()

Beep(1000, 200)

print("Enter: Start experiment")
print("Space: Feed mouse")
print("S: Set parametres")
print("F: Set feed time")
print("G: Get feed time")
print("C: check parametres")

parametresSet = False

while(True):
    print("\nPress key")    
    key = msvcrt.getch()
    if (key == b'\x1b'):
        sys.exit(1)
    if (key == b' '):
        myArduino.feedMouse()
        print("Feeding mouse!")
    if (key == b'\r'): #pressed Enter
        if parametresSet == True:
            startExperiment()
        else:
            print("Parametres not set!")
            
    if (key == b's'): #pressed s    
        data = experimentData()
        name = input("File with settings: ")
        data.setP(myArduino, name) #pass myArduino object, to set the feedtime
        
        experimentFile = fileHandler()
        experimentFile.setFileName(data.fileName) #pass the fileName to fileHandler
        
        myWindow = window()
        myWindow.minimize()
        
        parametresSet = True
    if (key == b'f'): #pressed f
        myArduino.setFeedTime()
    if (key == b'g'): #pressed f
        myArduino.getFeedTime()
    if (key == b'c'): #pressed c
        if parametresSet == True:
            data.check()
        else:
            print("Parametres are not set!")