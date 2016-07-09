#!/usr/bin/python2

import os,commands,time

def caas(c,username,password):
	os.system("dialog --radiolist 'Container as a Service' 30 80 3 1 'Centos' on 2 'Ubuntu' off 3 'MintOS' off 2>/tmp/sas.txt")
        o = open("/tmp/sas.txt")
	choice = o.read()
        o.close()
	
	#running dkr
	c.send(choice)

	if choice == '':
		os.system("dialog --infobox 'bye have a nice day !!!' 6 40 ")



	elif choice == '1':
		"""
		os.system("dialog --inputbox 'Enter no of Centos dockers you want' 10 30 2>/tmp/wd.txt")
		f = open("/tmp/wd.txt")
		doc = f.read()
		f.close()

		#sending no. of dockers to server
		c.send(doc)
		l = []
		d = int(doc)
		#recieving ips of docker
		for i in range(d):
			ip = c.recv(30)
			print ip
			l.extend(ip)

		# printing ips
		for i in range(d):
			print 'Docker {}  ip :  {}'.format(i+1,l[i])
			print 'Password {}'.format(password)
			print

		#os.system("ssh {}@{}".format(username,ip))
		"""
		#recieving ip of docker
		ip = c.recv(30)
		os.system("ssh {}@{}".format(username,ip))
			
	
	elif choice == '2':
		#recieving ip of docker
		ip = c.recv(30)
		os.system("ssh {}@{}".format(username,ip))
			
	
	elif choice == '3':
		#recieving ip of docker
		ip = c.recv(30)
		os.system("ssh {}@{}".format(username,ip))
				

