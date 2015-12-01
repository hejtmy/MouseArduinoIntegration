import serial
import time
import struct

arduino = serial.Serial('com4', 9600, timeout=1)
time.sleep(5)

while(True):
    ##arduino.write(struct.pack('>B', cislo)), jak poslat arduinu int, nefunguje?
    time.sleep(1) ##prodleva
    if (arduino.inWaiting()>0):
        data = arduino.readline()
        print data,
        rep = raw_input("Python Arduinu: ")
        arduino.write(rep)
        time.sleep(1)
