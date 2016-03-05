# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:48:18 2016

@author: Smoothie
"""

import os, msvcrt, sys, time

class fileHandler():
    def __init__(self):
        self.experimentFile = None
        self.fileName = None
        self.lineNumber = 1
        
        
        
    def setFileName(self, givenName):
        self.fileName = givenName    
    
    def createFile(self):
        if (os.path.exists(self.fileName) == True):
            print("File aready exist!")
            msvcrt.getch()
            sys.exit(1)
            
        elif (os.path.exists(self.fileName) == False):
            self.experimentFile = open("%s" % self.fileName, "w")
            self.experimentFile.close()

    def openFile(self):
        self.experimentFile = open("%s" % self.fileName, "a")
        
    def closeFile(self):
        self.experimentFile.close()

    def write(self, string):
        self.openFile()
        self.experimentFile.write("%s\n" %string)
        self.closeFile()
            
    def writeHeader(self, times, totalTime, repetitions):
        self.openFile()
        self.experimentFile.write("Mouse experiment\n")
        self.experimentFile.write("%s" %time.strftime("%d/%m/%Y %H:%M\n"))
        self.experimentFile.write("Line; experiment time; round time; Phase; Feeding\n")
        self.experimentFile.write("TIMES=%d,%d,%d\n" %(times[0], times[1], times[2]))
        self.experimentFile.write("TOTALTIME=%d\n" %totalTime)
        self.experimentFile.write("REPETITIONS=%d\n" %repetitions)
        self.experimentFile.write("START\n")
        self.closeFile()
        
    def writeStatusImages(self, timer, correctTime, correctImage, phase, feeding):
        self.openFile()
        self.experimentFile.write("%d;%.2f;%s;%s;%d;%s\n" %(self.lineNumber, timer, correctTime, correctImage, phase, feeding)) ##change the format
        self.lineNumber += 1        
        self.closeFile()
    
    def writeStatusTiming(self, experimentTime, roundTime, phase, feeding):
        self.openFile()
        self.experimentFile.write("%d;%.2f;%.2f;%d;%s\n" %(self.lineNumber, experimentTime, roundTime, phase, feeding))
        self.lineNumber += 1
        self.closeFile()
        
    def writeFooter(self):
        self.openFile()
        self.experimentFile.write("END\n")
        self.closeFile()