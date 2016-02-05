# -*- coding: utf-8 -*-

import time, random, serial, os, string
from tkinter import PhotoImage as PIM, Canvas, Tk

class experimentClass():
    
    """INITIALIZE ALL VARIABLES, CLASSES ETC"""
    def __init__(self, baudrate = 9600, port = "COM3"):
        """ARDUINO INIT"""
        self.arduinoConnection = serial.Serial();
        self.arduinoConnection.baudrate = baudrate;
        self.arduinoConnection.port = port;
        
        
        """EXPERIMENT DATA INIT"""
        self.times = None
        self.totalTime = None
        self.fileName = None
        self.reps = None
        self.images = [r"D:\Git\MouseArduinoIntegration\Experiment\circle.gif",
                       r"D:\Git\MouseArduinoIntegration\Experiment\square.gif",
                       r"D:\Git\MouseArduinoIntegration\Experiment\triangle.gif"] ##list of image names
        self.imagesOrder = None
        
        self.fileNameSet = False
        self.timesSet = False
        self.repsSet = False
        
        self.counter = 0
        self.correctImagePath = r"D:\Git\MouseArduinoIntegration\Experiment\circle.gif"
        self.currentImagePath = None
               
        
        
        """FILE HANDLER INIT"""
        self.experimentFile = None
        
        
        """IMAGE WINDOW INIT"""
        self.myTk = Tk()
        self.myTk.geometry("%dx%d+0+0" % (self.myTk.winfo_screenwidth() / 2.0, self.myTk.winfo_screenheight() / 2.0))
        self.myTk.grid()
        
        self.currentImage = None
        self.blankImage = PIM(file = r"D:\Git\MouseArduinoIntegration\Experiment\white.gif")
        
        self.myCanvas = Canvas(bg = "white", height = self.myTk.winfo_screenheight(), width = self.myTk.winfo_screenwidth())
        self.myCanvas.grid(column = 0, row = 0) #sticky = "EW")
        
        self.canvasImg = self.myCanvas.create_image(self.myTk.winfo_screenwidth() / 2.0, self.myTk.winfo_screenheight() / 2.0, image = None) #image = path to white img
#        self.update()




    """ARDUINO FUNCTIONS"""
    def connect(self):
        try:
            self.arduinoConnection.open();
        except Exception:
            print("COULDN'T CONNECT TO ARDUINO!!!")
            
    def disconnect(self):
        self.arduinoConnection.close()
        
        
#    def isConnected(self):
#        return self.arduinoConnection.isOpen();
    def receivedSignal(self):
        if (self.arduinoConnection.isOpen() == True):
            self.arduinoConnection.write(b"STOP")

    def resetArduino(self):
        if (self.arduinoConnection.isOpen()):
            self.arduinoConnection.write(b"REPEAT")
    
    def feedMouse(self):
        if (self.arduinoConnection.isOpen()):
            self.arduinoConnection.write(b"FEEDMOUSE")

    def prepareForExperiment(self):
        if self.arduinoConnection.isOpen():
            self.arduinoConnection.read_all()
            while(True):
                while (self.arduinoConnection.inWaiting() == 0):
                    pass
                if (self.arduinoConnection.read(4) == b"CX37"):
                    self.receivedSignal()
                    self.arduinoConnection.flushOutput()
                    self.arduinoConnection.flushInput()
                    break



    """DATA FUNCTIONS"""
    def getTimes(self):
        allowedTimes = list(range(1,61)) # allowed times = 1-60s
        
        inputOK = False
        while (inputOK != True):
            times = (input("Format: 5,4,8 Times:   ")).split(',')
            if len(times) == 3:
                try:
                    for i in times:
                        if int(i) in allowedTimes:
                            pass
                    inputOK = True
                except Exception: ##edit exception
                    pass

        self.times = []
        for i in times:
            self.times.append(int(i))
        self.timesSet = True
        self.totalTime = sum(self.times)
        
    def getFileName(self):
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
            
    def getReps(self):
        allowedReps = list(range(1,60))
        inputOK = False
        while (inputOK != True):
            reps = input("Input reps:   ")
            try:
                if int(reps) in allowedReps:
                    inputOK = True
            except Exception:
                pass
        self.reps = int(reps)
        self.repsSet = True
        
        self.imagesOrder = []
        for i in range(int(reps)):
            self.imagesOrder.append(random.randint(0,len(self.images)-1))
    
    
    
    """FILE HANDLING FUNCTIONS"""
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
        self.experimentFile.write("Format\n")
        self.experimentFile.write("Time ; correctTime ; correctImage ; Phase; Feeding\n")
        self.closeFile()
        
    def writeStatus(self, timer, correctTime, correctImage, phase, feeding):
        self.openFile()
        self.experimentFile.write("%.2f;%s;%s;%d;%s\n" %(timer, correctTime, correctImage, phase, str(feeding))) ##change the format
        self.closeFile()
        
    def writeFooter(self):
        self.openFile()
        self.experimentFile.write("Succesfully ended blah blah")
        self.closeFile()
        
    
    
    """IMAGE WINDOW FUNCTIONS"""
    def maximize(self):
        self.myTk.attributes('-fullscreen', True)
        self.myTk.deiconify()
        self.myTk.update()
        
    def topmost(self):
        self.myTk.attributes('-topmost', True)
        self.myTk.update()

    def minimize(self):
        self.myTk.iconify()
        self.myTk.update()
        

    def setImage(self, number): #pass here index of the image
        index = self.imagesOrder[number]        
        path = self.images[index]
        
        self.currentImagePath = path
        self.currentImage = PIM(file = "%s" %path)
        self.myCanvas.itemconfig(self.canvasImg, image = self.currentImage)
        self.myTk.update_idletasks()
    
    def showWhite(self):
        self.myCanvas.itemconfig(self.canvasImg, image = self.blankImage)
        self.myTk.update_idletasks()



    """EXPERIMENT FUNCTIONS"""
    def checkValues(self):
        print("Times set: {}\t Timing: {},{},{}\t Total time: {}".format(self.timesSet, self.times[0], self.times[1], self.times[2], self.totalTime))
        print("Filename set: %r\t Filename: %s" %(self.fileNameSet, self.fileName))
        print("Repetitions set: %r\t Number of repetitions: %d" %(self.repsSet, self.reps))
     
    def singleRound(self, number):
        
        clockStart = time.clock()
        self.setImage(number)
        
        ##first segment
        while( (time.clock() - clockStart) < self.times[0]):
            if(self.arduinoConnection.inWaiting() > 0):
                text = self.arduinoConnection.read(6)
                if(text == b"PUSHED"):
                    timer = time.clock() - clockStart
                    if (self.currentImagePath == self.correctImagePath):
                        self.writeStatus(timer,"False","True", 1, "False")
                    else:
                        self.writeStatus(timer,"False","False", 1, "False")
                        
        ##second segment
        while( (time.clock() - clockStart) < (self.times[0] + self.times[1]) ):
            if(self.arduinoConnection.inWaiting() > 0):
                text = self.arduinoConnection.read(6)
                if(text == b"PUSHED"):
                    timer = time.clock() - clockStart
                    if (self.currentImagePath == self.correctImagePath):
                        self.writeStatus(timer,"True","True", 2, "True")
                        self.feedMouse()
                    else:
                        self.writeStatus(timer,"True","False", 2, "False")
#        winsound.Beep(2000, 100)
        ##third segment
        while( (time.clock() - clockStart) < self.totalTime):
            if(self.arduinoConnection.inWaiting() > 0):
                text = self.arduinoConnection.read(6)
                if(text == b"PUSHED"):
                    timer = time.clock() - clockStart
                    if (self.currentImagePath == self.correctImagePath):
                        self.writeStatus(timer,"False","True", 3, "False")
                    else:
                        self.writeStatus(timer,"True","False", 3, "False")
        self.currentImg = None

    def startExperiment(self):        
        self.maximize()
        self.topmost()
        
        self.arduinoConnection.flushInput()
        self.arduinoConnection.flushOutput()
        
        while (self.counter < self.reps):
            self.singleRound(self.counter)
            self.counter += 1
            
        self.counter = 0
        self.myTk.destroy()