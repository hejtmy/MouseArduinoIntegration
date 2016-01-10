# use a Tkinter label as a panel/frame with a background image
# note that Tkinter only reads gif and ppm images
# use the Python Image Library (PIL) for other image formats
# free from [url]http://www.pythonware.com/products/pil/index.htm[/url]
# give Tkinter a namespace to avoid conflicts with PIL
# (they both have a class named Image)
 
import tkinter as tk
from PIL import Image, ImageTk
import time
 
root = tk.Tk()
root.title('background image')
 
# pick an image file you have .bmp  .jpg  .gif.  .png
# load the file and covert it to a Tkinter image object
imageFile = "D:\Git\MouseArduinoIntegration\Experiment\circle.jpg"
image1 = ImageTk.PhotoImage(Image.open(imageFile))
 
# get the image size
w = image1.width()
h = image1.height()
 
# position coordinates of root 'upper left corner'
x = 0
y = 0
 
# make the root window the size of the image
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
 
# root has no image argument, so use a label as a panel
panel1 = tk.Label(root, image=image1)
panel1.pack(side='top', fill='both', expand='yes')
 
# put a button on the image panel to test it
button2 = tk.Button(panel1, text='button2')
button2.pack(side='top')
 
# save the panel's image from 'garbage collection'
panel1.image = image1
 
# start the event loop
root.update_idletasks()
root.update()
while True:
    img = Image.open("D:\Git\MouseArduinoIntegration\Experiment\square.jpg")
    photo = ImageTk.PhotoImage(img)
    panel1.configure(image = photo)
    root.update_idletasks()

    start = time.clock()
    while ((time.clock() - start) < 2):
        pass

    img = Image.open("D:\Git\MouseArduinoIntegration\Experiment\circle.jpg")
    photo = ImageTk.PhotoImage(img)
    panel1.configure(image = photo)
    root.update_idletasks()

    start = time.clock()
    while ((time.clock() - start) < 2):
        pass
