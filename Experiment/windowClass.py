# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 21:18:34 2016

@author: Smoothie
"""

from time import sleep
from tkinter import Tk, Canvas, PhotoImage as PIM
from winsound import Beep

class window():
    def __init__(self):
        """IMAGE WINDOW INIT"""
        self.myWindow = Tk()
        self.myWindow.geometry("%dx%d+0+0" % (self.myWindow.winfo_screenwidth() / 2.0, self.myWindow.winfo_screenheight() / 2.0))
        self.myWindow.grid()
        
#        self.currentImage = None
        self.white = r"D:\Git\MouseArduinoIntegration\Experiment\white.gif"
        self.black = r"D:\Git\MouseArduinoIntegration\Experiment\black.gif"
        
        self.image = None
        
        self.myCanvas = Canvas(bg = "black", height = self.myWindow.winfo_screenheight(), width = self.myWindow.winfo_screenwidth())
        self.myCanvas.grid(column = 0, row = 0) #sticky = "EW")
        
        self.canvasImg = self.myCanvas.create_image(self.myWindow.winfo_screenwidth() / 2.0, self.myWindow.winfo_screenheight() / 2.0, image = None) #image = path to white img
#        self.myWindow.update()
        
        
        
        """IMAGE WINDOW FUNCTIONS"""
    def maximize(self):
        self.myWindow.attributes('-fullscreen', True)
        self.myWindow.deiconify()
        self.myWindow.update()
        
    def topmost(self):
        self.myWindow.attributes('-topmost', True)
        self.myWindow.update()

    def minimize(self):
        self.myWindow.iconify()
        self.myWindow.update()
        
        

    def setImage(self, imagePath): #pass here index of the image
        self.image = PIM(file = "%s" %imagePath)
        self.myCanvas.itemconfig(self.canvasImg, image = self.image)
        self.myWindow.update_idletasks()
    
    
    def blankWhite(self):
        self.image = PIM(file = "%s" %self.white)
        self.myCanvas.itemconfig(self.canvasImg, image = self.image)
        self.myWindow.update_idletasks()
    
    def blankBlack(self):
        self.image = PIM(file = "%s" %self.black)
        self.myCanvas.itemconfig(self.canvasImg, image = self.image)
        self.myWindow.update_idletasks()
        
    def blinkWhite(self):
        previousImage = self.image
        self.image = PIM(file = "%s" %self.white)
        self.myCanvas.itemconfig(self.canvasImg, image = self.image)
        self.myWindow.update_idletasks()

        Beep(1000, 500)
        
        self.image = previousImage
        self.myCanvas.itemconfig(self.canvasImg, image = self.image)
        self.myWindow.update_idletasks()
        
    def blinkBlack(self):
        previousImage = self.image
        self.image = PIM(file = "%s" %self.black)
        self.myCanvas.itemconfig(self.canvasImg, image = self.image)
        self.myWindow.update_idletasks()

        Beep(1000, 500)
        
        self.image = previousImage
        self.myCanvas.itemconfig(self.canvasImg, image = self.image)
        self.myWindow.update_idletasks()
        
    def closeWindow(self):
        self.myWindow.destroy()


#myWindow = window()
#myWindow.maximize()
#myWindow.topmost()
#myWindow.blinkBlack()
#myWindow.closeWindow()