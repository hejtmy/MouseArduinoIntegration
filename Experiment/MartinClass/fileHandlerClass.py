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
            
    def writeHeader(self):
        self.openFile()
        self.experimentFile.write("blah header blah\n")
        self.closeFile()
        
    def write(self, time, correctTime, correctImage):
        self.openFile()
        self.experimentFile.write("%.2f;%s;%s\n" %(time, correctTime, correctImage)) ##change the format
        self.closeFile()
        
    def closeFile(self):
        self.experimentFile.close()
