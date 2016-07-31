#!/usr/bin/python2

import os,commands,time

def vnc(c,username,password):
	os.system("dialog --inputbox 'enter id of your os' 10 30 2>/tmp/id.txt")
	fh = open("/tmp/id.txt")
        id = fh.read()
        fh.close()

	c.send(id)

	time.sleep(1)
	signal = c.recv(20)
	if signal == '1':
		port = c.recv(30)
		os.system("dialog --infobox 'connecting..... to this port' 10 40 ")
		time.sleep(4)
		os.system("vncviewer 192.168.122.1:{}".format(port))
	elif signal == '0':
		os.system("dialog --infobox 'no such id exists' 10 30")
	
