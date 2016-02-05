import serial

class Arduino:
    #arduino class has a serial attribute connection
    def __init__(self, baudrate = 9600, port = "COM3"):
        self.connection = serial.Serial();
        self.connection.baudrate = baudrate;
        self.connection.port = port;
    
    ##connect to arduino
    def connect(self):
        try:
            self.connection.open();
        except Exception:
            raise ValueError("COULDN'T CONNECT TO ARDUINO!!!")

    def isConnected(self):
        return self.connection.isOpen();

    ##sends stop code "STOP" to let arduino know communication is OK
    def sendStop(self):
        if (self.isConnected()):
            self.connection.write(b"STOP")
    
    def feedMouse(self):
        if (self.isConnected()):
            self.connection.write(b"FEEDMOUSE")
            
    ##at the end of the experiment, reset arduino cycle = start sending "CX37"" again
    def resetArduino(self):
        if (self.isConnected()):
            self.connection.write(b"REPEAT")

    def prepareForExperiment(self):
        while(True):
            while (self.connection.inWaiting() == 0):
                pass
            if (self.connection.readline() == b"CX37"):
                self.receivedSignal()
                self.connection.flushOutput()
                self.connection.flushInput()
                break
            
    def disconnect(self):
        self.connection.close()