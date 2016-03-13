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
    
#    def createFile(self):
#        if (os.path.exists(self.fileName) == True):
#            print("File aready exist!")
#            msvcrt.getch()
#            sys.exit(1)
#            
#        elif (os.path.exists(self.fileName) == False):
#            self.experimentFile = open("%s" % self.fileName, "w")
#            self.experimentFile.close()

    def openFile(self):
        if os.path.exists(self.fileName):
            self.experimentFile = open("%s" % self.fileName, "a")
        else:
            self.experimentFile = open("%s" % self.fileName, "w")
        
    def closeFile(self):
        self.experimentFile.close()

    def write(self, string):
        self.openFile()
        self.experimentFile.write("%s\n" %string)
        self.closeFile()
            
    def writeHeader(self, mode, times, totalTime, repetitions):
        self.openFile()
        self.experimentFile.write("Mouse experiment\n")
        self.experimentFile.write("%s" %time.strftime("%d/%m/%Y %H:%M\n"))
        self.experimentFile.write("Line number; Cycle number; Phase; Experiment time; Cycle time; Phase time\n")
        self.experimentFile.write("TIMES=%d,%d,%d\n" %(times[0], times[1], times[2]))
        self.experimentFile.write("TOTALTIME=%d\n" %totalTime)
        self.experimentFile.write("REPETITIONS=%d\n" %repetitions)
        self.experimentFile.write("MODE=%s\n" %mode)
        self.experimentFile.write("START\n")
        self.closeFile()
    
    def writeStatusTiming(self, cycle, phase, experimentTime, roundTime, phaseTime):
        self.openFile()
        self.experimentFile.write("%d;%d;%d;%.2f;%.2f;%.2f\n" %(self.lineNumber, cycle, phase, experimentTime, roundTime, phaseTime))
        self.lineNumber += 1
        self.closeFile()
        
    def writeFooter(self):
        self.openFile()
        self.experimentFile.write("END\n")
        self.closeFile()