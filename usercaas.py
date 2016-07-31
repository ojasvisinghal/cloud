#!/usr/bin/python2

import os,commands,time,usermenu

def caas(c,username,password):
	os.system("dialog --menu 'Container as a Service' 30 80 8 1 'Centos'  2 'Ubuntu' 3 'MintOS' 4 'Fedora' 5 'Redhat' 6 'Kali Linux' 7 'Back' 8 'Exit' 2>/tmp/sas.txt")
        o = open("/tmp/sas.txt")
	choice = o.read()
        o.close()
	
	c.send(choice)

#cancel
	if choice == '':
		usermenu(c,username,password)

#Centos
	elif choice == '1':
		ip = c.recv(30)
		os.system("ssh {}@{}".format(username,ip))
			
#Ubuntu	
	elif choice == '2':
		ip = c.recv(30)
		os.system("ssh {}@{}".format(username,ip))
			
#mintos	
	elif choice == '3':
		ip = c.recv(30)
		os.system("ssh {}@{}".format(username,ip))

#fedora
	elif choice == '4':
		ip = c.recv(30)
		os.system("ssh {}@{}".format(username,ip))

#redhat
	elif choice == '5':
		ip = c.recv(30)
		os.system("ssh {}@{}".format(username,ip))

#kali linux	
	elif choice == '6':
		ip = c.recv(30)
		os.system("ssh {}@{}".format(username,ip))
		
#back
	elif choice == '7':
		usermenu.menu(c,username,password)
	
#Exit
	elif choice == '8':
		os.system('dialog --infobox "BBye have a nice day" 10 50 ')	

