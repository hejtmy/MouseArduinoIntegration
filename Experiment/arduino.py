##connect to arduino
def connect():
    global ard
    try:
        ard = serial.Serial("COM3", 9600)
    except Exception:
        raise ValueError("COULDN'T CONNECT TO ARDUINO!!!")

##sends stop code "STOP" to let arduino know communication is OK
def sendStop():
    ard.write(b'STOP')

##at the end of the experiment, reset arduino cycle = start sending "CX37"" again
def sendReset():
    ard.write(b'REPEAT')
