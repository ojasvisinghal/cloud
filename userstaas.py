#!/usr/bin/python2


import os,commands,time,usermenu,usernfs,usersshfs,usersamba,usersnap,useriscsi

def staas(c,username,password):
	os.system("dialog --menu 'CHOOSE STORAGE TYPE' 15 60 3 1 'Object storage' 2 'Block storage'  3 'Back' 4 'Exit' 2>/tmp/b.txt")


	fh = open("/tmp/b.txt")
	choice = fh.read()
	fh.close()

	c.send(choice)	

#Cancel button
	if choice == '':
		usermenu.menu(c,username,password)
#object
	elif choice == '1':
		os.system("dialog --menu 'Storage Services' 20 60 7 1 'Disk through NFS' 2 'Disk through SSHFS' 3 'Disk through SAMBA'  4 'MOUNT SNAPSHOT' 5 'Remove disk' 6 'Back' 7 'Exit'  2>/tmp/cd.txt")
		gh = open("/tmp/cd.txt")
		dat = gh.read()
		gh.close()

		# sending which type of server user want
		c.send(dat)
#cancel
		if dat == '':
			staas(c,username,password)
#nfs	
		if dat == '1':
			usernfs.nfs(c,username,password)			
#sshfs server
		elif dat == '2':
			usersshfs.sshfs(c,username,password)
#samba server
		elif dat == '3':
			usersamba.samba(c,username,password)
#mount snapshot
		elif dat == '4':
			usersnap.snap(c,username,password)		
#Remove disk
		elif dat == '5':
			pass		
#Back
		elif dat == '6':
			staas(c,username,password)
#Exit
		elif dat == '7':
			os.system("dialog --infobox 'Thanks for your precious time' 30 40")
		



#block storage
	elif choice == '2':
		useriscsi.iscsi(c,username,password)
#back
	elif choice == '3':
		usermenu.menu(c,username,password)
#exit option

	elif choice == '4':
		os.system("dialog --infobox 'BBye !! We will miss you .......' 30 40")
	



