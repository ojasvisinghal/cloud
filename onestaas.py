#!/usr/bin/python2
import os,commands,time,onenfs,onesshfs,onesamba,onesnap,onemenu,oneiscsi

def staas(c,username,password):
	choice = c.recv(30)

###cancel button
	if choice == '':
		onemenu.menu(c,username,password)

###object storage

	elif choice == '1':
		data = c.recv(30)
#cancel
		if data == '':
			staas(c,username,paasword),onemenu
#nfs server
		if data == '1':
			onenfs.nfs(c,username,password)
#sshfs server
		elif data == '2':
			onesshfs.sshfs(c,username,password)
#samba server
		elif data == '3':
			onesamba.samba(c,username,password)
#mount snap
		elif data == '4':
			onesnap.snap(c,username,password)
#remove disk
		elif data == '5':
			pass
#back
		elif data == '6':
			staas(c,username,password)
#exit
		elif data == '7':
			c.close()


####block storage

	elif choice == '2':
		oneiscsi.iscsi(c,username,password)

### back option
	elif choice == '3':
		onemenu.menu(c,username,password)

### Exit

	elif choice == '4':
		c.close()
