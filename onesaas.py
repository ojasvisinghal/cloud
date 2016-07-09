#!/usr/bin/python2

import os,commands

def saas(c,username,password):
	choice = c.recv(30)
	if choice == '1':
		#getting signal to register user
		os.system("useradd -s /usr/bin/firefox  {0}fire".format(username))
		os.system("echo {} | passwd {}fire --stdin".format(password,username))
		#starting service and sending signal to user
		#c.send("1")
		os.system("systemctl restart sshd")
		os.system("systemctl enable sshd")
		c.send("1")

	elif choice == '2':
	        #getting signal to register user
	        os.system("useradd -s /usr/bin/gedit {0}gedit".format(username))
	        os.system("echo {} | passwd {}gedit".format(password,username))
	        #starting service and sending signal to user
	        #c.send("1")
	        os.system("systemctl restart sshd")
	        os.system("systemctl enable sshd")
		c.send("1")

	elif choice == '3':
		 #getting signal to register user
	        os.system("useradd  -s /usr/bin/vlc {0}vlc".format(username))
	        os.system("echo {} | passwd {}vlc".format(password,username))
	        #starting service and sending signal to user
	        #c.send("1")
	        os.system("systemctl restart sshd")
	        os.system("systemctl enable sshd")
		c.send("1")
#saas completed

