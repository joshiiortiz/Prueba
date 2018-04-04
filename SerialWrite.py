# -*- coding: cp1252 -*-
import serial
#import matplotlib.pyplot as plt
#import numpy as np

ser = 0
temp = 0
def init_serial():
    COMNUM = 4  
    global ser
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM4'
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE
    ser.stopbits = 1
    ser.timeout = 2
    ser.open()
    if ser.isOpen():
        print ('Open: ' + ser.portstr)

init_serial()

while 1:
    temp = str(raw_input('¿Qué va a mandar?, luego presione enter: '))
    ser.write(temp.encode())

"""
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.grid(True)
plt.savefig("test.png")
plt.show()

"""
