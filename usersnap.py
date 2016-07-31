#!/usr/bin/python2

import os,commands,userstaas

def snap(c,username,password):
	os.system("dialog --menu 'Choose to take snap back!!!' 15 60 6 1 'NFS snap' 2 'SSHFS snap' 3 'SAMBA snap' 4 'ISCSI snap' 5 'back' 6 'Exit' 2>/tmp/snap.txt")
	f = open("/tmp/snap.txt")
	choice = f.read()
	f.close()

	c.send(choice)

#cancel
	if choice == '':
		userstaas.staas(c,username,password)
#nfs snap
	elif choice == '1':
		signal = c.recv(40)
		print signal
		if signal == '1':
			os.system("mkdir /root/Desktop/{}nfssnap".format(username))
			os.system("mount 192.168.122.1:/media/{0}nfssnap /root/Desktop/{0}nfssnap".format(username))	
			os.system("dialog --infobox 'ALl DONE!!' 10 30")
		else:
			print 'ddd'
			os.system("dialog --infobox '######## ERROR' 10 30")

#sshfs snap
	elif choice == '2':
		signal = c.recv(40)
		if signal == "1":
			os.system("mkdir /root/Desktop/{}sshfssnap".format(username))
			os.system("mount 192.168.122.1:/media/{0}sshfssnap /root/Desktop/{0}sshfssnap".format(username))	
			os.system("dialog --infobox 'ALl DONE!!' 10 30")
		else:
			os.system("dialog --infobox '######## ERROR' 10 30")

	
#sambasnap
	elif choice == '3':	
		signal = c.recv(40)

		if signal == '1':
			os.system("mkdir /root/Desktop/{}sambasnap".format(username))
			os.system("mount 192.168.122.1:/media/{0}sambasnap /root/Desktop/{0}sambasnap".format(username))	
			os.system("dialog --infobox 'ALl DONE!!' 10 30")
		else:
			os.system("dialog --infobox '######## ERROR' 10 30")

	
#iscsi snap	
	elif choice == '4':
		signal = c.recv(40)

		if signal == '1':
			os.system("mkdir /root/Desktop/{}iscsisnap".format(username))
			os.system("mount 192.168.122.1:/media/{0}iscsisnap /root/Desktop/{0}iscsisnap".format(username))	
			os.system("dialog --infobox 'ALl DONE!!' 10 30")
		else:
			os.system("dialog --infobox '######## ERROR' 10 30")

	
#back
	elif choice == '5':
		userstaas.staas(c,username,password)

#exit
	elif choice == '6':
		os.system("dialog --infobox 'Logout successfully' 10 30")	
