#!/usr/bin/python2

import os,commands,time
def paas(c,username,password):
	os.system("dialog --radiolist 'choose your platform' 30 80 3 1 'PYTHON' on 2 'PERL' off 3 'PHP' off 2>/tmp/sas.txt")
	o = open("/tmp/sas.txt")
	choice = o.read()
        o.close()
	
	#running dkr
	c.send(choice)

	if choice == '':
		os.system("dialog --infobox 'bye have a nice day !!!' 6 40 ")

	elif choice == '1':
		#recieving ip of docker
		ip = c.recv(30)
		os.system("route add -net 172.17.0.0/16 gw 192.168.122.1")
		os.system("ssh {}@{}".format(username,ip))
			
	elif choice == '2':
		 #recieving ip of docker
                ip = c.recv(30)
                os.system("route add -net 172.17.0.0/16 gw 192.168.122.1")
                os.system("ssh {}@{}".format(username,ip))
                        
	elif choice == '3':
		 #recieving ip of docker
                ip = c.recv(30)
                os.system("route add -net 172.17.0.0/16 gw 192.168.122.1")
                os.system("ssh {}@{}".format(username,ip))
                        


