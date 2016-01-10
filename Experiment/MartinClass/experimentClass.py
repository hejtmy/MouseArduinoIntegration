import subprocess, time, random

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
