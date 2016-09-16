#launch with "python -u catty.py"
import sys
import os
import time

#q = "quit"
ttime = time.strftime("_%H:%M:%S")
date = time.strftime("%d.%m.%Y")
name = 'catty_log_'+ date + ttime + '.txt'

f = open(name,'w+')


from serial import Serial
#os.system("dmesg | grep ttyUSB")
#usbport = raw_input("Type USB port number (press Enter for USB0)\n")
#if (usbport == ""):
#	usbport = "0"
#string = "/dev/ttyUSB" + usbport
#baud = raw_input("Type baudrate (press Enter for 74880) \n")
#if (baud == ""):
#	baud = 74880
#elif (baud == "1"):
#	baud = 115200
string = "/dev/ttyUSB0"
baud = 115200
dev = Serial(string, baud)
while True:
	c = dev.read(1)
	f.write(c)
	sys.stdout.write(c)

	#if q !== raw_input("Type quit to return to shell \n"):
	#	sys.exit("Exiting program")
