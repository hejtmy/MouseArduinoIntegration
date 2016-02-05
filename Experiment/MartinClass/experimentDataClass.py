import string, random

class experimentData():
    def __init__(self):
        ##main variables
        self.times = []
        self.totalTime = None
        self.fileName = None
        self.reps = None
        
        self.images = ["D:\Git\MouseArduinoIntegration\Experiment\circle.gif",
                       "D:\Git\MouseArduinoIntegration\Experiment\square.gif",
                       "D:\Git\MouseArduinoIntegration\Experiment\triangle.gif"] ##list of image names
        self.imageIndexes = []
        for i in range(self.reps):
            self.imageIndexes.append(random.randint(0, len(self.images)))
#        create list of indexes to be used during experiment
        
        #variables for checking if parametres are set
        self.fileNameSet = False
        self.timesSet = False
        self.repsSet = False


    def getTimes(self):
        allowedTimes = list(range(1,301)) # allowed times = 1-300s
        
        inputOK = False
        while (inputOK != True):
            times = (input("Format: 5,4,8 Times: ")).split(',')
            if len(times) == 3:
                try:
                    for time in times:
                        if int(time) in allowedTimes:
                            pass
                    inputOK = True
                except Exception: ##edit exception
                    pass
                
        self.times = times
        self.timesSet = True
        self.totalTime = sum(self.times)
        
    def getFileName(self):
        counter = None
        allowedChars = "()-_%s%s" % (string.ascii_letters, string.digits) ##only characters for file name allowed
        while(counter != 0):
            counter = 0
            fileName = input("File name without .txt: ")
            for char in fileName:
                if char not in allowedChars:
                    counter += 1
            if (counter > 0):
                print("Invalid input - %d chars invalid!" % counter)
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
        self.imageIndexes = []
        for i in range(int(reps)):
            self.imageIndexes.append(random.randint(0,2)) ##change to correct number of images
