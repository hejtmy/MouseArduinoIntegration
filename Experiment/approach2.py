import serial, os, string, random, subprocess, time

class inputData():
    def __init__(self):
        self.times = []
        self.fileName = None
        self.reps = None
        self.fileNameSet = False
        self.timesSet = False
        self.repsSet = False
        self.totalTime = None

    def getTimes(self):
        allowedTimes = list(range(1,61))
        inputOK = False
        while (inputOK != True):
            times = (input("Format: 5,4,8 Times: ")).split(',')
            if len(times) == 3:
                try:
                    for time in times:
                        if int(time) in allowedTimes:
                            pass
                    inputOK = True
                except Exception:
                    pass
        self.times = times
        self.timesSet = True
        self.totalTime = sum(self.times)
        
    def getFileName(self):
        counter = None
        allowedChars = "()-_%s%s" % (string.ascii_letters, string.digits)
        while(counter != 0):
            counter = 0
            fileName = input("File name without .txt: ")
            for char in fileName:
                if char not in allowedChars:
                    counter += 1
        self.fileName = fileName
        self.fileNameSet = True
            
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
        self.repsSet = True


class fileHandler():
    def __init__(self, fileName):
        self.fileName = "%s.txt" % fileName
        self.experimentFile = None

    def createFile(self):
        if (os.path.exists(self.fileName) == True):
            print("File aready exists")
            raise FileExistsError("File with that name alerady exists!!!")
        elif (os.path.exists(self.fileName) == False):
            self.experimentFile = open("%s" % self.fileName, "w")
            self.experimentFile.close()

    def openFile(self):
        self.experimentFile = open("%s.txt" % self.fileName, "a")
            
    def writeHeader(self):
        self.openFile()
        self.experimentFile.write("blah header blah\n")
        self.closeFile()
        
    def write(self, time, correctTime, correctImage):
        self.openFile()
        self.experimentFile.write("%.2f;%s;%s\n" %(time, correctTime, correctImage)) ##change the format
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
    
class Experiment():
    def __init__(self):
        self.images = ["circle.jpg" , "square.jpg" , "triangle.jpg"] ##list of image names
        self.correctImage = None ##replace with proper img
        self.currentImage = None
        self.imageProcessID = None
        self.counter = 0
        self.randomInt = None
        self.imageDict = {
            1 : 'circle.jpg',
            2 : 'square.jpg',
            3 : 'triangle.jpg'
            }

    def createRandomInt(self):
        self.randomInt = random.randint(0,len(self.images)-1)
    
    def showImg(self):
        createRandomInt()
        self.currentImage = self.imageDict[self.randomInt]
        process = subprocess.Popen("mspaint %s" %self.imageDict[randomInt], shell = True)
        self.imageProcessID = process.pid
    
    def closeImg(self):
        subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=self.imageProcessID))
        self.imageProcessID = None

    def singleRound(self):
        self.showImg()
        timeNow = time.clock()

        ##fileHandler.write(correctTime, correctImage)
        
        ##first segment
        while( (time.clock() - timeNow) < inputData.times[0]):
            while(MyArduino.inWaiting() != b"PUSHED/n"):
                if (self.currentImage == self.correctImage):
                    fileHandler.write( time.clock(),"False","True")
                else:
                    fileHandler.write( time.clock(),"False","False")

        ##second segment
        while( (time.clock() - timeNow) < inputData.times[1]):
            while(MyArduino.inWaiting() != b"PUSHED/n"):
                if (self.currentImage == self.correctImage):
                    fileHandler.writeOK()
                else:
                    fileHandler.write(time.clock(),"True","False")

        ##third segment
        while( (time.clock() - timeNow) < inputData.times[2]):
            while(MyArduino.inWaiting() != b"PUSHED/n"):
                if (self.currentImage == self.correctImage):
                    fileHandler.write(time.clock(),"False","True")
                else:
                    fileHandler.write(time.clock(),"Frue","False")

        self.closeImg()
        self.currentImg = None
        self.imageProcessID = None

    def startExperiment(self):
        while (counter < inputData.reps):
            singleRound()
            counter += 1
        self.counter = 0
    
MyArduino = Arduino()
##MyArduino.connect()
##MyArduino.prepareForExperiment()
###ready for an experiment
##MyArduino.resetArduino()

dataFile = fileHandler("givenFileName")
dataFile.createFile()
dataFile.writeHeader()
dataFile.write(time.clock(),"False","True")
dataFile.closeFile()

##data = inputData()
##data.getTimes()
##data.getReps()
##data.getFileName()
