import serial

class Arduino (serial.Serial):
    def __init__(self):
        self.connected = False
        serial.Serial.__init__(self)
    
    def connect(self):
        self.port = "COM4"
        self.baudrate = 9600
        try:
            self.open()
            self.connected = True
        except Exception:
            print("Couldn't connect!")
            
    def receivedSignal(self):
        if (self.connected):
            self.write(b"STOP\n")

    def resetArduino(self):
        if (self.connected):
            self.write(b"RESET\n")

    def prepareForExperiment(self):
        while(True):
            while (self.inWaiting() == 0):
                pass
            if (self.readline() == b"CX37\n"):
                self.receivedSignal()
                self.flushOutput()
                self.flushInput()
                break
            
    def disconnect(self):
        self.close()

    def check(self):
        if (self.readline() == b"PUSHED\n"):
            ##call fileHandler to write to file
