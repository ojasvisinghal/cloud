#!/usr/bin/python2
import os,commands,time

def gallery(c,username,password):
	sig =c.recv(30)
	if sig == '0':
		os.system("dialog --infobox 'no os yet' 10 30")

	else:
		#p = c.recv(30) #recieving 1
		p1 = c.recv(20)
		p2 = c.recv(20)
		p3 = c.recv(20)


		print p1
		print p2
		print p3
		if p1 == '0':
			port1 = c.recv(30)	
			os.system("dialog --infobox 'Port no is {}' 10 30 ".format(port1))
			os.system("firefox http://192.168.122.1/vnc/?ip=192.168.122.1&port={}".format(port1))
			
		if p2 == '0':
			port2 = c.recv(30)	
			os.system("dialog --infobox 'Port no is {}' 10 30 ".format(port2))
			os.system("firefox http://192.168.122.1/vnc/?ip=192.168.122.1&port={}".format(port2))
			

		if p3 == '0':
			port3 = c.recv(30)	
			os.system("dialog --infobox 'Port no is {}' 10 30 ".format(port3))
			os.system("firefox http://192.168.122.1/vnc/?ip=192.168.122.1&port={}".format(port3))
		