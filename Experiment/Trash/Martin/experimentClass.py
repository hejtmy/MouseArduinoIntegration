import time

class Experiment():
    def __init__(self):
        self.correctImage = "D:\Git\MouseArduinoIntegration\Experiment\circle.gif" ##replace with proper img
        self.currentImage = None
        self.counter = 0
        
        self.imagesOrder = data.imageIndexes
#        set to "reps" list of random number of range "from 0 to len(images)"
#        or create it in inputData and copy from there
        
    def changeImg(self, path):
#       tell imageHandler class to show image
        imageWindow.changeImg(path)

    def showBlank(self):
        imageWindow.showWhite()
#        tell imageHandler to set image to blank
        
    def singleRound(self, number):
        clockStart = time.clock()
        ##fileHandler.write(time, correctTime, correctImage)
        self.currentImage = self.imagesOrder(number)
        self.changeImg(self.currentImage)
                
        
        ##first segment
        while( (time.clock() - clockStart) < data.times[0]):
            if(MyArduino.connection.readline() == b"PUSHED"):
                if (self.currentImage == self.correctImage):
                    fileHandler.write(time.clock(),"False","True", 1)
                else:
                    fileHandler.write(time.clock(),"False","False", 1)

        ##second segment
        while( (time.clock() - clockStart) < data.times[1]):
            if(MyArduino.connection.readline() == b"PUSHED"):
                if (self.currentImage == self.correctImage):
                    fileHandler.write(time.clock(),"True","True", 2)
                else:
                    fileHandler.write(time.clock(),"True","False", 2)

        ##third segment
        while( (time.clock() - clockStart) < data.times[2]):
            if(MyArduino.connection.readline() == b"PUSHED"):
                if (self.currentImage == self.correctImage):
                    fileHandler.write(time.clock(),"False","True", 3)
                else:
                    fileHandler.write(time.clock(),"Frue","False", 3)

        self.currentImg = None

    def startExperiment(self):
#        initialize window
        imageWindow.maximize()
        imageWindow.topmost()
        
        while (self.counter < data.reps):
#            show image
            singleRound(self.counter)
            counter += 1
        self.counter = 0
        
