#!/usr/bin/python2
import os,commands,time

def saas(c,username,password):
	os.system("dialog --radiolist 'Software as a service' 30 80 3 1 'FIREFOX' on 2 'GEDIT' off 3 'VLC' off 2>/tmp/sas.txt")
	o = open("/tmp/sas.txt")
	choice = o.read()
	o.close()

	#sending choice to server to get permission
	c.send(choice)
	if choice == '1':

#firefox
		#setting signal to server to set password and create account for this user
		data = c.recv(30)
		if data == '1':
		#sending password to server
		#c.send(pswd)
			os.system("ssh -X {}fire@192.168.122.1".format(username))
			os.system("##################")
		else:
			os.system("###$$$$$$$ ERROR  FIREFOX $$$$########")
		

#gedit
	elif choice == '2':
		  #setting signal to server to set password and create account for this user
                data = c.recv(30)
                if data == 1:
                #sending password to server
                #c.send(pswd)
                        os.system("ssh -X {}gedit@192.168.122.1".format(username))
                else:
                        os.system("###$$$$$$$ ERROR  GEDIT $$$$########")

		
#vlc
	elif choice == '3':
		 #setting signal to server to set password and create account for this user
                data = c.recv(30)
                if data == 1:
                #sending password to server
                #c.send(pswd)
                        os.system("ssh -X {}@192.168.122.1".format(password,username))
                else:
                        os.system("###$$$$$$$ ERROR VLC $$$$########")


