import os

class fileHandler():
    def __init__(self, fileName):
        self.fileName = "%s.txt" % fileName
        self.experimentFile = None


    def createFile(self):
        if (os.path.exists(self.fileName) == True):
            print("File aready exists")
            raise FileExistsError("File with that name alerady exists!!!")
        elif (os.path.exists(self.fileName) == False):
            self.experimentFile = open("%s" % self.fileName, "w")
            self.experimentFile.close()



    def openFile(self):
        self.experimentFile = open("%s.txt" % self.fileName, "a")
        
    def closeFile(self):
        self.experimentFile.close()


            
    def writeHeader(self):
        self.openFile()
        self.experimentFile.write("Format\n")
        self.experimentFile.write("Time ; correctTime ; correctImage ; Phase\n")
        self.closeFile()
        
    def write(self, time, correctTime, correctImage, phase):
        self.openFile()
        self.experimentFile.write("%.2f;%s;%s;%d;\n" %(time, correctTime, correctImage, phase)) ##change the format
        self.closeFile()
        
    def writeEnd(self):
        self.openFile()
        self.experimentFile.write("succesfully ended blah blah")
        self.closeFile()

