import tkinter, time
from tkinter import PhotoImage as PIM, Canvas

class window(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.img = None
        self.geometry("%dx%d+0+0" % (300, 300)) #(self.winfo_screenwidth(), self.winfo_screenheight()))
#        self.geometry("%dx%d+0+0" %(self.winfo_screenwidth() ,self.winfo_screenheight()))
        
        self.path1 = None
        self.path2 = None
        self.myCanvas = None
        self.canvasImg = None

        self.initialize() #set / initialize the window, containers, size etc
        
    def initialize(self):
        self.grid()
        
#        self.myCanvas = Canvas(self)
#        self.myCanvas.grid(column = 0, row = 0, sticky = 'EW') #widnget stick to left and right (east west) edges of a window

        self.path1 = r"D:\Git\MouseArduinoIntegration\Experiment\circle.gif"
        self.path2 = r"D:\Git\MouseArduinoIntegration\Experiment\triangle.gif"
        self.img = PIM(file = self.path1)
        img_width = self.img.width()
        img_height = self.img.height()
        
        self.myCanvas = Canvas(height = img_height, width = img_width)
        self.myCanvas.grid(column = 0, row = 0, sticky = 'EW')
        self.x = img_width / 2.0
        self.y = img_height / 2.0
                
        self.canvasImg = self.myCanvas.create_image(self.x, self.y, image = self.img)
    
    def change_img(self):
        newPath = r"D:\Git\MouseArduinoIntegration\Experiment\triangle.gif"
        img = PIM(file = newPath)
        print("OK")
        self.myCanvas.itemconfig(self.canvasImg, image = img)
        
    def set_size(self):
        self.wm_state('iconic')

if __name__ == "__main__":
    myWindow = window(None)
#    myWindow.attributes('-fullscreen', True)
#    myWindow.attributes('-topmost', True)
#    myWindow.lift()

#    myWindow.update_idletasks()
#    myWindow.mainloop()
    myWindow.update()
    time.sleep(2)
    
#    myWindow.attributes('-topmost', True)
    myWindow.attributes('-fullscreen', True)
    myWindow.update()
    time.sleep(2)
    
    myWindow.change_img()
    time.sleep(2)
    
    myWindow.destroy()
#1 - initiate minimalized window object with proper parametres = window size, single container etc.
#2 - set functions for showBlank, showImage(circle.jpg / square.jpg / ...), closeWindow
#3 - 