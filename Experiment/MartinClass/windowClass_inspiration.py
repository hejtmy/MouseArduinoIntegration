import time
from tkinter import PhotoImage as PIM, Canvas, Tk

class window(Tk, Canvas):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.grid()
        self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))
#        self.geometry("%dx%d+0+0" %(self.winfo_screenwidth() ,self.winfo_screenheight()))
        
        self.path1 = r"D:\Git\MouseArduinoIntegration\Experiment\circle.gif"
        self.path2 = r"D:\Git\MouseArduinoIntegration\Experiment\triangle.gif"
        
        self.img1 = PIM(file = self.path1)
        self.img1_width = self.img1.width()
        self.img1_height = self.img1.height()
        
        self.img2 = PIM(file = self.path2)
        self.img2_width = self.img2.width()
        self.img2_height = self.img2.height()
        

        self.myCanvas = Canvas(parent, bg = "white", height = self.winfo_screenheight(), width = self.winfo_screenwidth())        
#        self.myCanvas = Canvas(parent, height = self.winfo_screenheight(), width = self.winfo_screenwidth())
        
        self.myCanvas.grid(column = 0, row = 0) #sticky = "EW")
        
        self.canvasImg = self.myCanvas.create_image(self.winfo_screenwidth() / 2.0, self.winfo_screenheight() / 2.0, image = self.img1)
#        self.canvasImg = self.myCanvas.create_image(self.img1_width, self.img1_height, image = self.img1)
        
#        self.x = img_width / 2.0
#        self.y = img_height / 2.0
        
        
    def change_img(self):
        self.myCanvas.itemconfig(self.canvasImg, image = self.img2)
        
    def minimize(self):
        self.wm_state('iconic')
        
    def show_blank(self):
#        self.image_to_show = PIM(path to folder + "blank.gif")
        self.myCanvas.itemconfig(self.canvasImg, image = self.img2)
        
if __name__ == "__main__":
    
    myWindow = window(None)
    
    myWindow.attributes('-topmost', True)
    myWindow.attributes('-fullscreen', True)
#    myWindow.lift()
    
    myWindow.update()
    time.sleep(2)
    
    myWindow.change_img()
    myWindow.update()
    time.sleep(2)
    
    x = 0
    while (x < 100):
        myWindow.myCanvas.move(myWindow.canvasImg, 10, 0)
        myWindow.update()
        time.sleep(0.01)
        x += 1
    
    myWindow.destroy()
#1 - initiate minimalized window object with proper parametres = window size, single container etc.
#2 - set functions for showBlank, showImage(circle.jpg / square.jpg / ...), closeWindow
#3 - 