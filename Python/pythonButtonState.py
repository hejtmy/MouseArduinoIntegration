import serial
import time

arduinoSerialData = serial.Serial('com4',9600) ##create serial object
times = open('times.txt', 'w') ##vytvorit soubor na zapis dat

##pridat vyjimku pro pripad, ze soubor uz existuje, at se nespremaze

while (True):
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline()
        print("Time: " + time.strftime('%X %x') ) ##vypsat cas stisku
        times.write(time.strftime('%X %x') + "\n") ##zapsat cas stisku do souboru
        times.close() ##zavrit soubor
        times = open('times.txt', 'a') ##znovu otevrit soubor, at se pri chybe nesmaze vse
