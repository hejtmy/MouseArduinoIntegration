# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:48:18 2016

@author: Smoothie
"""

import os

class fileHandler():
    def __init__(self):
        self.experimentFile = None
        self.fileName = None
        
        
        
    """FILE HANDLING FUNCTIONS"""
    def setFileName(self, givenName):
        self.fileName = givenName
    
    
    def createFile(self):
        if (os.path.exists(self.fileName) == True):
            print("File aready exists")
            raise FileExistsError("File with that name alerady exists!!!")
        elif (os.path.exists(self.fileName) == False):
            self.experimentFile = open("%s" % self.fileName, "w")
            self.experimentFile.close()

    def openFile(self):
        self.experimentFile = open("%s" % self.fileName, "a")
        
    def closeFile(self):
        self.experimentFile.close()

            
    def writeHeader(self):
        self.openFile()
        self.experimentFile.write("FORMAT\n")
        self.experimentFile.write("Experiment time; round time; Phase; Feeding\n")
        self.closeFile()
        
    def writeStatusImages(self, timer, correctTime, correctImage, phase, feeding):
        self.openFile()
        self.experimentFile.write("%.2f;%s;%s;%d;%s\n" %(timer, correctTime, correctImage, phase, feeding)) ##change the format
        self.closeFile()
    
    def writeStatusTiming(self, experimentTime, roundTime, phase, feeding):
        self.openFile()
        self.experimentFile.write("%.2f;%.2f;%d;%s\n" %(experimentTime, roundTime, phase, feeding))
        self.closeFile()
        
    def writeFooter(self):
        self.openFile()
        self.experimentFile.write("Succesfully ended blah blah")
        self.closeFile()