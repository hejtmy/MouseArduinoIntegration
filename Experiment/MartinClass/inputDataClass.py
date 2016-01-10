import string, random

class inputData():
    def __init__(self):
        self.times = []
        self.imageIndexes = None ##create list of indexes for image loading
        self.fileName = None
        self.reps = None
        
        self.totalTime = None
        
        self.fileNameSet = False
        self.timesSet = False
        self.repsSet = False


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
        self.imageIndexes = []
        for i in range(int(reps)):
            self.imageIndexes.append(random.randint(0,2)) ##change to correct number of images
