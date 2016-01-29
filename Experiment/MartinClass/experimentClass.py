import time

class Experiment():
    def __init__(self):
        self.images = ["circle.jpg" , "square.jpg" , "triangle.jpg"] ##list of image names
        self.correctImage = None ##replace with proper img
        self.currentImage = None
        self.counter = 0
        self.images = ['circle.jpg', 'square,jpg', 'triangle.jpg']
        
        self.imagesOrder = None
#        set to "reps" list of random number of range "from 0 to len(images)"
#        or create it in inputData and copy from there
        
    def showImg(self):
#        tell imageHandler class to show image
        pass
    
    def setImage(self):
#        tell imageHandler to set next image                
        pass

    def showBlank(self):
#        tell imageHandler to set image to blank
        
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
