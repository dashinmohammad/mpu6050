import serial
from time import sleep
import sys
import re

COM = '/dev/rfcomm0'
BAUD = 115200

ser = serial.Serial(COM, BAUD, timeout = .1)

print('Waiting for device');
sleep(3)
print(ser.name)

while True:
	val = str(ser.readline().decode().strip('\r\n'))#Capture serial output as a decoded string
	valA = val.split()
	print(valA, end="\r", flush=True)
	a = valA[0]
	print (a, end="\r", flush=True)
	

	
