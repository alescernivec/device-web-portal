import serial

class SerialBackend():
    
    serial = None
    
    def __init__(self, port=0, device='/dev/ttyS1', timeout=0, baudrate=9600, **args):
        self.serial = serial.Serial(device, baudrate, timeout)
        
    def read(self, number_of_bytes=1):
        self.serial.read(number_of_bytes)
        
    def write(self, data ):
        self.serial.write(data)
        
    def close(self):
        self.serial.close()