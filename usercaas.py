#!/usr/bin/python2

import os,commands,time

def caas(c,username,password):
	os.system("dialog --radiolist 'Container as a Service' 30 80 3 1 'Centos' on 2 'Ubuntu' off 3 'MintOS' off 2>/tmp/sas.txt")
        o = open("/tmp/sas.txt")
	choice = o.read()
        o.close()
	
	#running dkr
	c.send(choice)
	if choice == '1':
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
				

