#!/usr/bin/python2

import os,commands,time,fileSend

def extend(c,username,password):

# checking database whether any drive exist with username
	# writing all existing lvs in a file
	fileSend.filee(username)

	#opening this file in read mode and sending it to client
	fh = open("/root/Desktop/folderServer/derive.txt")
	i = 0
	while i < 4:
		d = next(fh)
		c.send(d)
		i = i + 1				

	#receiving name of hardisk
	#name = c.recv(100)
	#recieving type
	typee = c.recv(30)
	#recieving harddisk size
	size = c.recv(40)

	if typee == 'nfs':
		os.system("lvextend --name {} --size +{} userVG".format(username,size))
		os.system("resize2fs /dev/mapper/userVG-{}nfs".format(username))
		#sending successful signal	
		c.send("1")	
	elif typee == 'sshfs':
		os.system("lvextend --name {} --size +{} userVG".format(username,size))
		os.system("resize2fs /dev/mapper/userVG-{}sshfs".format(username))
		#sending successful signal	
		c.send("1")
	elif typee == 'iscsi':
		os.system("lvextend --name {} --size +{} userVG".format(username,size))
		os.system("resize2fs /dev/mapper/userVG-{}iscsi".format(username))
		#sending successful signal	
		c.send("1")
	elif typee == 'samba':
		os.system("lvextend --name {} --size +{} userVG".format(username,size))
		os.system("resize2fs /dev/mapper/userVG-{}smb".format(username))
		#sending successful signal	
		c.send("1")



