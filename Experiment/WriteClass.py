import os.path              ##for checking if file exists
import time
class WriteClass:
    ###instantiate class

    def __init__(self, filename="arduino_experiment.txt"):
        self.filename = filename;

    def openFile(self):
        try:
            self.fileExists();
        except FileExistsError as ex:
            print("FIlE ALREADY EXISTS!!!");

            #asks to rewrite:

    ##check if file to be created already exists
    def fileExists(self):
        if (os.path.isfile(self.fileName)==True):
            raise FileExistsError("FIlE ALREADY EXISTS!!!")

class WriteClassSpecificExperiment(WriteClass):

    now = 0
    start = 0
    counter = 0
    ##write file header in specific format
    ##1st line - "Mouse experiment"
    ##2nd line - Date and time of creation
    ##3rd line - Repetitions to be made
    ##4th line - Free line for further notes
    ##5th line - Format of data sequence writing
    def writeHeader(self):
        dataFile = open("%s" % self.fileName, "w")
        dataFile.write("Mouse experiment\n")
        dataFile.write(time.strftime("%d/%m/%y\t%H:%M:%S\n"))
        dataFile.write("Repetitions to be made: %s\n" % str("I gues five? Needs to check"))#number or repetitions
        dataFile.write("\n")
        dataFile.write("Number\tStatus\tPicture\tTiming\tPhase\tElapsed\n")
        dataFile.close()

    ##write to file, when button is pushed UNCORRECTLY
    ##phase argument - during which phase button was pushed (1/2/3)
    ##elapsed time = timing = time since showing the picture
    def writeWrong(self,phase):
        elapsedTime = self.now - self.start               ##time elapsed from showing picture

        dataFile = open("%s" % self.fileName, "a")   ##open a file
        dataFile.write("%s\t" % str(self.counter))   ##write number of push
        dataFile.write("False\t")               ##write Status - False

        if (self.picture == self.correctPicture):           ##if the right picture was shown
            dataFile.write("True\t")            ##write Picture - True
        else:
            dataFile.write("False\t")           ##write Picture - False

        ###alternative - if (phase == 2):
        if (elapsedTime > (self.initLag) and elapsedTime < (self.initLag + self.imgLag)):
            dataFile.write("True\t")            ##write Timing - True
        else:
            dataFile.write("False\t")           ##write Timing - False
        dataFile.write("%d\t" % phase)          ##write Phase
        dataFile.write("%.2f\t" % elapsedTime)  ##write Elapsed time
        dataFile.write("\n")
        dataFile.close()

    ##write to file, when button is pushed CORRECTLY
    ##phase argument - during which phase button was pushed (1/2/3)
    ##elapsed time = timing = time since showing the picture
    def writeOK(self,phase):
        elapsedTime = self.now - self.start;              ##time elapsed from showing picture
        dataFile = open("%s" % self.fileName, "a")   ##open a file
        dataFile.write("%s\t" % str(self.counter))   ##write number of push
        dataFile.write("True\t")                ##write Status - True
        dataFile.write("True\t")                ##write Picture - True
        dataFile.write("True\t")                ##write Timing - True
        dataFile.write("%d\t" % phase)          ##write Phase
        dataFile.write("%.2f" % elapsedTime)    ##write Elapsed time
        dataFile.write("\n")
        dataFile.close()