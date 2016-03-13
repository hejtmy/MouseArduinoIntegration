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
    
    times = []
    
    start = 0
    end = 6  
    
    pressesTotal = 0
    pressesCorrect = 0
        
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
            print("Line positions (phase times): ", linePositions)
        if line.startswith("PRESSESTOTAL"):
            pressesTotal = int(line.split("=")[1])
        if line.startswith("PRESSESCORRECT"):
            pressesCorrect = int(line.split("=")[1])        
    
    for i in range(startIndex, endIndex):
        line = lines[i].strip().split(";")
        if len(line) == 6:
            if int(line[2]) != 3:
#                phases.append(line[3])
                times.append(float(line[4]))
#                feedingStates.append(line[4])
            
    #histogram
    plt.hist(times, bins = end*2, range = (start, end), color = 'blue')

    plt.axvline(linePositions[0], color = 'red', linewidth = 5)
    plt.axvline(linePositions[1], color = 'red', linewidth = 5)
    plt.xlabel('Time range [s]')
    plt.ylabel('Number of presses [-]')
    plt.grid()
    
    plt.figtext(0.05, 0.95, "Total presses without 3rd phase: %d" %len(times))
    plt.figtext(0.6, 0.95, "Correct presses: %d" %pressesCorrect)
    plt.show()

openFile()
makeGraph()