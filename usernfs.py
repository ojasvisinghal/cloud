#!/usr/bin/python2

import os,commands,time

def nfs(c,username,password):
	os.system("dialog --inputbox 'Enter harddisk size' 10 60 2>/tmp/size.txt")
	g = open("/tmp/size.txt")
	size = g.read()
	g.close()

	# sending size to server

	c.send(size)

	#getting signal what to do
	signal = c.recv(20)

	print signal
	if signal == "exists":
		print 'entered'
		os.system("dialog --menu 'Changes' 10 50 2 1 'Extend' 2 'Remove' 2>/tmp/hy.txt")
		fh = open("/tmp/hy.txt")
		si = fh.read()
		fh.close()
		
		print 'send'
		c.send(si)
		if si == '1':
			a = c.recv(30)
			if a == '0':
				os.system("dialog --infobox 'DONE check' 10 80")

		else:
			a = c.recv(30)
			if a == '0':
				os.system("dialog --infobox 'DONE check' 10 80")

	# client side processing started
	elif signal == 'not':
		#recieving successful signal from server
		d = c.recv(30)
		if d == '1':
			os.system("mkdir /root/Desktop/{}".format(username))
			os.system("mount 192.168.122.1:/home/nfs/{0} /root/Desktop/{0}".format(username))
		
			os.system("dialog --infobox 'All Done enjoy!!! Check ' 10 50")
	else:
		os.system("dialog --infobox 'ERROR' 10 80")
