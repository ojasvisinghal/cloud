#!/usr/bin/python2
import os,commands,time,usermenu

def saas(c,username,password):
	os.system("dialog --menu 'Choose your software Software as a service' 30 80 5 1 'Firefox' 2 'Gedit' 3 'Vlc' 4 'Back' 5 'Exit' 2>/tmp/sas.txt")
	o = open("/tmp/sas.txt")
	choice = o.read()
	o.close()

	c.send(choice)
#firefox
	if choice == '1':
		data = c.recv(30)
		if data == '1':
			os.system("ssh -X {}fire@192.168.122.1".format(username))
		else:
			os.system("###$$$$$$$ ERROR IN  FIREFOX $$$$########")
		
#gedit
	elif choice == '2':
                data = c.recv(30)
                if data == 1:
                        os.system("ssh -X {}gedit@192.168.122.1".format(username))
                else:
                        os.system("###$$$$$$$ ERROR IN GEDIT $$$$########")
		
#vlc
	elif choice == '3':
                data = c.recv(30)
                if data == 1:
                        os.system("ssh -X {}@192.168.122.1".format(password,username))
                else:
                        os.system("###$$$$$$$ ERROR IN VLC $$$$########")

#back
	elif choice == '4':
		usermenu.menu(c,username,password)

#exit
	elif choice == '5':
		os.system("dialog --infobox 'Bye Have a nice day' 10 40")

