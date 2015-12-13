import serial, os, string, random


class inputData():
    def __init__(self):
        self.times = []
        self.fileName = None
        self.reps = None

    def getTimes(self):
        allowedTimes = list(range(1,61))
        inputOK = False
        while (inputOK != True):
            times = (input("Format: 1,60,31 Times: ")).split(',')
            if len(times) == 3:
                try:
                    for time in times:
                        if int(time) in allowedTimes:
                            pass
                    inputOK = True
                except Exception:
                    pass
        self.times = times     
        
    def getFileName(self):
        counter = None
        allowedChars = "()-_%s%s" % (string.ascii_letters, string.digits)
        while(counter != 0):
            counter = 0
            fileName = input("File Name without .txt: ")
            for char in fileName:
                if char not in allowedChars:
                    counter += 1
        self.fileName = fileName
            
    def getReps(self):
        allowedReps = list(range(1,100))
        inputOK = False
        while (inputOK != True):
            reps = input("Input reps: ")
            try:
                if int(reps) in allowedReps:
                    inputOK = True
            except Exception:
                pass
        self.reps = reps 


class fileHandler():
    def __init__(self, fileName):
        self.fileName = fileName
        self.experimentFile = None

    def createFile(self):
        if (os.path.exists(self.fileName) == True):
            print("File aready exists")
        elif (os.path.exists(self.fileName) == False):
            self.experimentFile = open("%s.txt" % self.fileName, "w")
            self.experimentFile.close()

    def openFile(self):
        self.experimentFile = open("%s.txt" % self.fileName, "a")
            
    def writeHeader(self):
        self.openFile()
        self.experimentFile.write("blah header blah\n")
        self.closeFile()

    def writeOK(self):
        self.openFile()
        self.experimentFile.write("blah OK blah\n")
        self.closeFile()
        
    def writeWrong(self):
        self.openFile()
        self.experimentFile.write("blah OK blah\n")
        self.closeFile()
        
    def closeFile(self):
        self.experimentFile.close()

        
class Arduino (serial.Serial):
    def __init__(self):
        self.connected = False
        serial.Serial.__init__(self)
    
    def connect(self):
        self.port = "COM4"
        self.baudrate = 9600
        try:
            self.open()
            self.connected = True
        except Exception:
            print("Couldn't connect!")
            
    def receivedSignal(self):
        if (self.connected):
            self.write(b"STOP\n")

    def resetArduino(self):
        if (self.connected):
            self.write(b"RESET\n")

    def prepareForExperiment(self):
        while(True):
            while (self.inWaiting() == 0):
                pass
            if (self.readline() == b"CX37\n"):
                self.receivedSignal()
                self.flushOutput()
                self.flushInput()
                break
            
    def disconnect(self):
        self.close()
    
##MyArduino = Arduino()
##MyArduino.connect()
##MyArduino.prepareForExperiment()
###ready for an experiment
##MyArduino.resetArduino()

##dataFile = fileHandler("fileName.txt")
##dataFile.createFile()
##dataFile.writeHeader()
##dataFile.writeOK()
##dataFile.writeWrong()
##dataFile.closeFile()

##data = inputData()
##data.getTimes()
##data.getReps()
##data.getFileName()
