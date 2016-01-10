import time
import tkinter as tk
from PIL import Image, ImageTk

class Experiment():
    def __init__(self):
        self.images = ["circle.jpg" , "square.jpg" , "triangle.jpg"] ##list of image names
        self.correctImage = None ##replace with proper img
        self.currentImage = None
        self.imageProcessID = None
        self.counter = 0
        self.imageDict = {
            1 : 'circle.jpg',
            2 : 'square.jpg',
            3 : 'triangle.jpg'
            }

        ##variables for tkinter 
        self.imageFile = None
        self.image1 = None
        self.panel1 = None
        self.root = None        
    
    def showImg(self):
        ##initialize tkinter object
        root = tk.Tk()
        root.title('Mouse experiment')
        
        ##check timing??
        
    def setImage(self):
        self.imageFile = "D:\Git\MouseArduinoIntegration\Experiment\black.jpg"
        self.image1 = ImageTk.PhotoImage(Image.open(self.imageFile))
        # get the image size
        w = self.image1.width()
        h = self.image1.height()
        
        # position coordinates of root 'upper left corner'
        x = 0
        y = 0
        # make the root window the size of the image
        root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        # root has no image argument, so use a label as a panel
        self.panel1 = tk.Label(root, image=self.image1)
        self.panel1.pack(side='top', fill='both', expand='yes')
        self.panel1.image = image1

    def changeImage(self):
        ##change size of the image
        self.imageFile = "D:\Git\MouseArduinoIntegration\Experiment\%s" % self.imageDict[data.imageIndexes[self.counter]]
        self.image1 = ImageTk.PhotoImage(Image.open(imageFile))
        self.panel1.configure(
        img = Image.open("D:\Git\MouseArduinoIntegration\Experiment\square.jpg")
        photo = ImageTk.PhotoImage(img)
        panel1.configure(image = photo)
                    
    def closeImg(self):
        ##replace with tkinter widget
        pass

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
