#!/usr/bin/python2

import os,commands

def snap(c,username,password):
	os.system("dialog --menu 'Choose to take snap back!!!' 15 60 4 1 'NFS' 2 'SSHFS' 3 'SAMBA' 4 'ISCSI' 2>/tmp/snap.txt")
	f = open("/tmp/snap.txt")
	choice = f.read()
	f.close()

	c.send(choice)


	if choice == '1':
		signal = c.recv(40)
		print signal
		if signal == '1':
			os.system("mkdir /root/Desktop/{}nfssnap".format(username))
			os.system("mount {0}@192.168.122.1:/media/{0}nfssnap /root/Desktop/{0}nfssnap".format(username))	
			os.system("dialog --infobox 'ALl DONE!!' 10 30")
		else:
			print 'ddd'
			os.system("dialog --infobox '######## ERROR' 10 30")




	elif choice == '2':
		signal = c.recv(40)
		if signal == "1":
			os.system("mkdir /root/Desktop/{}sshfssnap".format(username))
			os.system("mount {0}@192.168.122.1:/media/{0}sshfssnap /root/Desktop/{0}sshfssnap".format(username))	
			os.system("dialog --infobox 'ALl DONE!!' 10 30")
		else:
			os.system("dialog --infobox '######## ERROR' 10 30")

	



	elif choice == '3':	
		signal = c.recv(40)

		if signal == '1':
			os.system("mkdir /root/Desktop/{}sambasnap".format(username))
			os.system("mount {0}@192.168.122.1:/media/{0}sambasnap /root/Desktop/{0}sambasnap".format(username))	
			os.system("dialog --infobox 'ALl DONE!!' 10 30")
		else:
			os.system("dialog --infobox '######## ERROR' 10 30")

	
	
	elif choice == '4':
		signal = c.recv(40)

		if signal == '1':
			os.system("mkdir /root/Desktop/{}iscsisnap".format(username))
			os.system("mount {0}@192.168.122.1:/media/{0}iscsisnap /root/Desktop/{0}iscsisnap".format(username))	
			os.system("dialog --infobox 'ALl DONE!!' 10 30")
		else:
			os.system("dialog --infobox '######## ERROR' 10 30")

	
	
