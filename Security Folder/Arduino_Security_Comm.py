import smbus
import time
import subprocess

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

#def writeNumber(value):
#    bus.write_byte(address, value)
    #bus.write_byte_data(address, 0, value)
#    return -1

def readNumber():
    number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    return number

while True:
    time.sleep(.1)
    number = readNumber()

    print number

    if number == 1:
        print "Motion Detected"
        print "Start Recording..."
        subprocess.call("Camera_Trigger.sh")
        print "End Recording"
        sleep(60)
    
