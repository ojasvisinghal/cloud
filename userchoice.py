#!/usr/bin/python2

import os,commands,time

def choice(c,username,password):
		os.system("dialog --inputbox 'enter ram' 7 30 2>/tmp/ram.txt")
		os.system("dialog --inputbox 'enter cpu' 7 30 2>/tmp/cpu.txt")
		os.system("dialog --inputbox 'enter harddisk' 7 30 2>/tmp/hd.txt")
		a=open("/tmp/ram.txt")
		ram = a.read()
		a.close()

		a=open("/tmp/cpu.txt")
	        cpu = a.read()
	        a.close()

		a=open("/tmp/hd.txt")
	        hd = a.read()
	        a.close()
	
		#sending all three values to server
		c.send(ram)
		time.sleep(1)
		c.send(cpu)
		time.sleep(1)
		c.send(hd)
		time.sleep(1)
