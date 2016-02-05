import time
from tkinter import PhotoImage as PIM, Canvas, Tk

class window():
    def __init__(self, parent):
        self.myTk = Tk()
#        self.myTk.parent = parent
        self.myTk.geometry("%dx%d+0+0" % (self.myTk.winfo_screenwidth() / 2.0, self.myTk.winfo_screenheight() / 2.0))
        self.myTk.grid()
        self.currentImg = None
        self.whiteImg = PIM(file = r"D:\Git\MouseArduinoIntegration\Experiment\white.gif")
        
        self.myCanvas = Canvas(parent, bg = "white", height = self.myTk.winfo_screenheight(), width = self.myTk.winfo_screenwidth())
        self.myCanvas.grid(column = 0, row = 0) #sticky = "EW")
        
        self.canvasImg = self.myCanvas.create_image(self.myTk.winfo_screenwidth() / 2.0, self.myTk.winfo_screenheight() / 2.0, image = None) #image = path to white img
        
        self.myTk.update()

    def maximize(self):
        self.myTk.attributes('-fullscreen', True)
        self.myTk.deiconify()
        self.myTk.update()
        
    def topmost(self):
        self.myTk.attributes('-topmost', True)
        self.myTk.update()
        

    def changeImg(self, path):
        self.currentImg = PIM(file = "%s" %path)
        self.myCanvas.itemconfig(self.canvasImg, image = self.currentImg)
        self.myTk.update_idletasks()
    
    def showWhite(self):
        self.myCanvas.itemconfig(self.canvasImg, image = self.whiteImg)
        self.myTk.update_idletasks()
        
    def minimize(self):
        self.myTk.iconify()
        self.myTk.update()
        

        
if __name__ == "__main__":
    
    myWindow = window(None)
    myWindow.topmost()
    
    start = time.clock()
        
    while ((time.clock() - start) < 1):
        pass
    myWindow.maximize()
    myWindow.topmost()
    
    while ((time.clock() - start) < 2):
        pass  
    myWindow.changeImg("D:\Git\MouseArduinoIntegration\Experiment\circle.gif")  
    
    while ((time.clock() - start) < 3):
        pass
    myWindow.minimize()
    
    while ((time.clock() - start) < 4):
        pass
    myWindow.maximize()
    
    while ((time.clock() - start) < 5):
        pass
    myWindow.changeImg("D:\Git\MouseArduinoIntegration\Experiment\square.gif")
    
    while ((time.clock() - start) < 6):
        pass
    myWindow.showWhite()
    
    while ((time.clock() - start) < 7):
        pass
    myWindow.myTk.destroy() 

#1 - initiate minimalized window object with proper parametres = window size, single container etc.
#2 - set functions for showBlank, showImage(circle.jpg / square.jpg / ...), closeWindow
#3 - 