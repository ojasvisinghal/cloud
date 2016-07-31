#!/usr/bin/python2
import os,commands,time,usernfs,usersshfs,usersamba,useriscsi,userextend,usergallery,usersnap,useros,usercaas,userpaas,usersaas,usermenu,userqren




###############################################  IAAS  ####################################################



def iaas(c,username,password):
	os.system("dialog --radiolist 'OSREMOTE TOOL' 30 60 6 1 'OS GALLERY' on 2 'INSTALL OS' off  3 'OS using Qrencode' off 4 'OS list' off 5 'OS migrate' off 6 'os in android' off 2>/tmp/qq.txt")
	f = open("/tmp/qq.txt")
        choice = f.read()
        f.close()

	#sending choice 
	c.send(choice)

	if choice == '':
		usermenu.menu(c,username,password)

#os gallery
	if choice == '1':
		usergallery.gallery(c,username,password)
	
#install os
	if choice == '2':		
		useros.oss(c,username,password)

#os with qrencode
	if choice == '3':
		userqren.qr(c,username,password)
	"""
	#os system  list
		if choice == '4':
		userlist.listt(c,username,password)

	#os migrate
	if choice == '5':
		usermigrate.migrate(c,username,password)

	"""


	if choice == '6':
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

#iaas completed


def paas(c,username,password):
	userpaas.paas(c,username,password)
	
#paas completed

def caas(c,username,password):
	usercaas.caas(c,username,password)

#caas done

def saas(c,username,password):
	usersaas.saas(c,username,password)

#saas completed


