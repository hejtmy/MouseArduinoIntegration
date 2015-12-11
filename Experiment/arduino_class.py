import serial               ##for communication with arduino
class Arduino:

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

    def is_connected(self):
        return self.connection.isOpen();

    ##sends stop code "STOP" to let arduino know communication is OK
    def sendConnectionOK(self):
        self.connection.write(b'STOP')

    ##at the end of the experiment, reset arduino cycle = start sending "CX37"" again
    def sendReset(self):
        self.connection.write(b'REPEAT')