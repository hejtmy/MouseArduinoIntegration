# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:26:38 2016

@author: Smoothie
"""

import serial

class arduino():
    def __init__(self, port = "COM3", baudrate = 9600, timeout = 0.01):
        self.arduinoConnection = serial.Serial()
        self.arduinoConnection.port = port
        self.arduinoConnection.timeout = timeout
        self.arduinoConnection.baudrate = baudrate



    def connect(self):
        try:
            self.arduinoConnection.open();
        except FileNotFoundError:
            print("Couldn't connect to arduino!")
            
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
            time = args[0]
        else:
            time = input("Set feeding time: ")
        allowedTimes = list(range(1000, 11000, 1000))
        timeSet = False
        
        while (timeSet != True):
            if time in allowedTimes:
                self.arduinoConnection.write(b"SETFEEDTIME")
                time.sleep(0.2)
                self.arduinoConnection.write(time)
                timeSet = True
            else:
                time = input("Set feed time: ")
                
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
            if (self.arduinoConnection.readline() == b"PUSHED"):
                return True
        else:
            return False


