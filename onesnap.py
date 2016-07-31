#!/usr/bin/python2

import os,commands,onestaas

def snap(c,username,password):
	choice = c.recv(40)
	
#cancel
	if choice == '':
		onestaas.staas(c,username,password)
#nfs snap
	elif choice == '1':
		import MySQLdb
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		y.execute("use cloud;")
		e = y.execute("select NFS from SNAP where USERNAME='{}';".format(username))
		q = y.fetchall()
		sd = '/media/{0}nfssnap'.format(username)
		if q[0][0]== sd:
			c.send("1")
			os.system("exportfs -r")
			onestaas.staas(c,username,password)
		else:
			c.send("0")
			onestaas.staas(c,username,password)
# sshfs snap
		
	elif choice == '2':	
		import MySQLdb
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		y.execute("use cloud;")
		e = y.execute("select SSHFS from SNAP where USERNAME='{}';".format(username))
		q = y.fetchall()
		sd = '/media/{0}sshfssnap'.format(username)
		if q[0][0]== sd:
			c.send("1")
			os.system("exportfs -r")
			onestaas.staas(c,username,password)
		else:
			c.send("0")
			onestaas.staas(c,username,password)

# samba snap
	elif choice == '3':
		import MySQLdb
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		y.execute("use cloud;")
		e = y.execute("select SAMBA from SNAP where USERNAME='{}';".format(username))
		q = y.fetchall()
		sd = '/media/{0}sambasnap'.format(username)
		if q[0][0]== sd:
			c.send("1")
			os.system("exportfs -r")
			onestaas.staas(c,username,password)
		else:
			c.send("0")
			onestaas.staas(c,username,password)

# iscsi snap
	elif choice == '4':
		import MySQLdb
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		y.execute("use cloud;")
		e = y.execute("select ISCSI from SNAP where USERNAME='{}';".format(username))
		q = y.fetchall()
		sd = '/media/{0}iscsisnap'.format(username)
		if q[0][0]== sd:
			c.send("1")
			os.system("exportfs -r")
			onestaas.staas(c,username,password)
		else:
			c.send("0")
			onestaas.staas(c,username,password)

#back
	elif choice == '5':
		onestaas.staas(c,username,password)

#exit
	elif choice == '6':
		c.close()
