# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 00:30:14 2016

@author: Smoothie
"""

from matplotlib import pyplot as plt

def openFile():
    global fileName
    fileName = input("file name: ")
    try:
        global myFile
        myFile = open(fileName, "r")
        print("File opened!")
        return
    except Exception as ex:
        print("Oh shit, file not found! Exception raised!")
        print(ex)
        openFile()
        
def makeGraph():
    lines = myFile.readlines()
    
    startIndex, endIndex = None, None
    for i in range(len(lines)):
        if lines[i] == "START\n":
            print("Start index: %d" %i)
            startIndex = i + 1
        if lines[i] == "END\n":
            print("End index: %d" %i)
            endIndex = i
    if startIndex == None or endIndex == None:
        print("Indexes not found!")
    
    
    phases = []
    times = []
    feedingStates = []
    
    start = 0
    end = 6    
    
    for i in range(startIndex, endIndex):
        line = lines[i].strip().split(";")
        phases.append(line[3])
        times.append(float(line[2]))
        feedingStates.append(line[4])
        
    for line in lines:
        if line.startswith("TOTALTIME"):
            end = int(list(line.split("="))[1])
            print("Total time: ",end)
        if line.startswith("TIMES"):
            experimentTimes = line.split("=")[1].split(",")            
            time1 = int(experimentTimes[0])
            time2 = int(experimentTimes[1])
            linePositions = []
            linePositions.append(time1)
            linePositions.append(time1 + time2)
            print("Line positions: ", linePositions)
    
    #histogram    
    plt.hist(times, bins = end*2, range = (start, end), color = 'blue')
    plt.axvline(linePositions[0], color = 'red', linewidth = 5)
    plt.axvline(linePositions[1], color = 'red', linewidth = 5)
    plt.xlabel('Time range [s]')
    plt.ylabel('Number of presses [-]')
    plt.grid()
    plt.show()

openFile()
makeGraph()