# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:26:38 2016

@author: Smoothie
"""

import serial, time, msvcrt, sys

class arduino():
    def __init__(self, port = "COM3", baudrate = 9600, timeout = 0.01):
        self.arduinoConnection = serial.Serial()
        self.arduinoConnection.port = port
        self.arduinoConnection.timeout = timeout
        self.arduinoConnection.baudrate = baudrate



    def connect(self):
        try:
            self.arduinoConnection.open();
        except Exception as ex:
            print("Couldn't connect to arduino! Try ", ex)
            msvcrt.getch()
            sys.exit(1)
            
    def disconnect(self):
        try:
            self.arduinoConnection.close()
        except Exception:
            print("Couldn't disconnect from arduino!")

    def flush(self):
        self.arduinoConnection.flushInput()
        self.arduinoConnection.flushOutput()

    def stopSending(self):
        if (self.arduinoConnection.isOpen() == True):
            self.arduinoConnection.write(b"STOP")
        else:
            print("Arduino is not connected!")

    def reset(self):
        if (self.arduinoConnection.isOpen()):
            self.arduinoConnection.write(b"REPEAT")
        else:
            print("Arduino is not connected!")
    
    def feedMouse(self):
        if (self.arduinoConnection.isOpen()):
            self.arduinoConnection.write(b"FEEDMOUSE")
        else:
            print("Arduino is not connected!")
    
    def setFeedTime(self, *args):
        if (len(args) == 1):
            feedTime = args[0]
        else:
            feedTime = input("Set feeding time: ")
            
        allowedTimes = list(range(1000, 11000, 100))
        feedTimeSet = False

        try:
            feedTime = int(feedTime)
        except Exception as ex:
            print("Exception raised:\n", ex)
            
        while (feedTimeSet != True):
            if feedTime in allowedTimes:
                print("Set feed time to %dms" %feedTime)
                self.arduinoConnection.write(b"SETFEEDTIME")
                time.sleep(0.2)
                self.arduinoConnection.write(b"%s" %str(feedTime))
#                self.arduinoConnection.write(b"SETFEEDTIME%d" %time)
                feedTimeSet = True
            else:
                feedTime = input("Set feed time: ")
    
    def getFeedTime(self):
        self.arduinoConnection.write(b"TELLFEEDTIME")
        time.sleep(0.2)
        if self.arduinoConnection.in_waiting > 0:
            feedTime = self.arduinoConnection.readline()
            print("Feed time from arduino: ", feedTime)
            msvcrt.getch()
        else:
            print("Feed time not received from arduino!!!")
            msvcrt.getch()
            
    def beep(self):
        self.arduinoConnection.write(b"BEEP")
        
    def prepare(self):
        if self.arduinoConnection.isOpen():
            self.arduinoConnection.read_all()
            
            while(True):
                while (self.arduinoConnection.inWaiting() == 0):
                    pass
                if (self.arduinoConnection.readline() == b"CX37"):
                    self.stopSending()
                    self.arduinoConnection.flushOutput()
                    self.arduinoConnection.flushInput()
                    break
        else:
            print("Arduino is not connected!")
       
    def isPushed(self):
        if (self.arduinoConnection.in_waiting > 0):
#            before = time.clock()
            receivedText = self.arduinoConnection.readline()
#            after = time.clock()
#            print("Received text: ", receivedText, "Reading buffer took: %fs" %(after - before))
            if (receivedText == b"PUSHED"):
                return True
            else:
                print("Incorrect received text: ", receivedText)
                return False


