#!/usr/bin/python2

import os,commands,time

def andos(c,username,password):
		os.system("dialog --menu 'Choose Your Flavour' 40 40 5 1 'REDHAT 7.2' 2 'UBUNTU' 3 'Windows' 4 'Exit' 5 'Back' 2>/tmp/fla.txt")
		no=open('/tmp/fla.txt')
		mo=no.read()
		no.close()
		c.send(mo)

		if mo == '1':
			#recieving id
			id  = c.recv(10)
			time.sleep(1)
			if id != '0':
				#recieving port
				port = c.recv(30) 
				os.system("dialog --msgbox 'Install VNC VIEWER app in your Mobile and type 192.168.122.1:{}' 30 30 ".format(port))

			else:
				os.system("dialog --msgbox 'No such OS exists'")

			 
		elif mo == '2':
			#recieving id
			id  = c.recv(10)
			time.sleep(1)
			if id != '0':
				#recieving port
				port = c.recv(30) 
				os.system("dialog --msgbox 'Install VNC VIEWER app in your Mobile and type 192.168.122.1:{}' 30 30 ".format(port))

			else:
				os.system("dialog --msgbox 'No such OS exists'")

		elif mo == '3':
			#recieving id
			id  = c.recv(10)
			time.sleep(1)
			if id != '0':
				#recieving port
				port = c.recv(30) 
				os.system("dialog --msgbox 'Install VNC VIEWER app in your Mobile and type 192.168.122.1:{}' 30 30 ".format(port))

				else:
					os.system("dialog --msgbox 'No such OS exists'")
	

			elif mo == '4':
				c.close()

			elif mo == '5':
				iaas(c,username,password)

