# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:39:31 2016

@author: Smoothie
"""

import string, random, msvcrt, sys, time

class experimentData():
    def __init__(self):
        self.fileName = ""
        self.repetitions = 0
        self.times = [0,0,0]
        self.totalTime = 0
        self.beepLength = 500 #ms
        
        self.beep = False
        self.resetAfterPush = False
        self.jumpToEnd = False

        self.images = [r"D:\Git\MouseArduinoIntegration\Experiment\circle.gif",
                       r"D:\Git\MouseArduinoIntegration\Experiment\square.gif",
                       r"D:\Git\MouseArduinoIntegration\Experiment\triangle.gif",
                       r"D:\Git\MouseArduinoIntegration\Experiment\hexagon.gif"]
        self.blankBlack = r"D:\Git\MouseArduinoIntegration\Experiment\black.gif"
        self.blankWhite = r"D:\Git\MouseArduinoIntegration\Experiment\white.gif"
                       
        self.correctImage = r"D:\Git\MouseArduinoIntegration\Experiment\circle.gif"
        self.currentImage = None
        self.imagesOrder = None

        self.fileNameSet = False
        self.timesSet = False
        self.repetitionsSet = False
        self.totalTimeSet = False
        self.imagesOrderSet = False


    def setFileName(self):
        counter = None
        allowedChars = "().-_%s%s" % (string.ascii_letters, string.digits) ##only characters for file name allowed
        
        while(counter != 0):
            counter = 0
            fileName = input("File name:   ")
            for char in fileName:
                if char not in allowedChars:
                    counter += 1
            if (counter > 0):
                print("Invalid input - %d chars invalid!" % counter)
        self.fileName = fileName
        self.fileNameSet = True
        
        
    def setBeep(self, *args):
        if len(args) == 1:
            if (args[0] == True or args[0] == False):
                self.beep = args[0]
                return
        else:
            beep = input("Beep at the beginning of each round? Y/N")
            if (beep == "Y" or beep == "y"):
                self.beep = True
            elif (beep == "N" or beep == "n"):
                self.beep = False
            else:
                self.setBeep()                
        
        
    def setTimes(self, *args):
        allowedTimes = list(range(1,61)) # allowed times = 1-60s
        inputOK = False
        if (len(args) == 1):
            times = args[0]
        else:
            times = (input("Format: 5,4,8 Times:   "))
        while (inputOK != True):
            times = times.split(',')
            if len(times) == 3:
                try:
                    for i in times:
                        if int(i) in allowedTimes:
                            pass
                    inputOK = True
                except Exception: ##edit exception
                    times = (input("Format: 5,4,8 Times:   "))
                    
        self.times = []
        for i in times:
            self.times.append(int(i))            
        self.timesSet = True
        
        self.totalTime = sum(self.times)
        self.totalTimeSet = True 
        
        
        
    def setRepetitions(self, *args):
        allowedRepetitions = list(range(1,60))
        inputOK = False
        
        if (len(args) == 1):
                repetitions = args[0]
        else:
            repetitions = input("Input reps:")
            
        while (inputOK != True):
            try:
                if int(repetitions) in allowedRepetitions:
                    inputOK = True
            except Exception:
                repetitions = input("Input reps:")
                
        self.repetitions = int(repetitions)
        self.repetitionsSet = True
        
        self.imagesOrder = []
        for i in range(int(repetitions)):
            self.imagesOrder.append(random.randint(0,len(self.images)-1))
            self.imagesOrderSet = True
            
            
    
    def setP(self, *args):
        self.setFileName()
        if len(args) == 1:
            try:
                file = open("%s" %args[0], "r").readlines()
                for line in file:
                    if line.startswith("REPETITIONS"):
                        repetitions = int((line.split("="))[1].strip())
                        self.setRepetitions(repetitions)
                    if line.startswith("TIMES"):
                        times = (line.split("="))[1].strip()
                        self.setTimes(times)
                    if line.startswith("FEEDTIME"):
                        feedTime = (line.split("="))[1].strip()
                        myArduino.setFeedTime(feedTime)
                    if line.startswith("JUMPTOEND"):
                        status = (line.split("="))[1].strip()
                        if status == "TRUE":
                            self.jumpToEnd = True
                        elif status == "FALSE":
                            self.jumpToEnd = False
                    if line.startswith("RESETAFTERPUSH"):
                        status = (line.split("="))[1].strip()
                        if status == "TRUE":
                            self.resetAfterPush = True
                        elif status == "FALSE":
                            self.resetAfterPush = False
                            
#                set parametres from file
            except FileNotFoundError:
                print("File not found!")

        if (self.timesSet == False):
            self.setTimes()
        if (self.repetitionsSet == False):
            self.setRepetitions()
        
            
                
                
    def check(self):
        print("All parametres set: %r" %(self.fileNameSet and self.timesSet and self.repetitionsSet and self.imagesOrderSet))
        print("Times set: \t{}\t Timing: {},{},{}\t Total time: {}".format(self.timesSet, self.times[0], self.times[1], self.times[2], self.totalTime))
        print("Filename set: \t%r\t Filename: %s" %(self.fileNameSet, self.fileName))
        print("Repetitions set: \t%r\t Number of repetitions: %d" %(self.repetitionsSet, self.repetitions))
        print("Images order set: %r" %(self.imagesOrderSet))
        print("Reset after push: %r" %(self.resetAfterPush))
        print("Jump to phase 3 after push: %r" %(self.jumpToEnd))
        time.sleep(5)
#        if msvcrt.getch() == b"\x1b":
#            sys.exit(1)
