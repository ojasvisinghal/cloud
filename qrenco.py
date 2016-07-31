#!/usr/bin/python2


import os,commands

def qren(c,username,password):
	import MySQLdb
	os.system("systemctl restart mariadb")
	x=MySQLdb.connect("localhost")
	y=x.cursor()
	y.execute("use cloud;")
	a = y.execute("select * from REDHAT where USERNAME='{0}'".format(username))
	b = y.execute("select * from UBUNTU where USERNAME='{0}'".format(username))
	d = y.execute("select * from WINDOWS where USERNAME='{0}'".format(username))

	a = y.execute("select * from REDHAT where USERNAME='{0}'".format(username))
	if a != 0L:
		c.send("1")
		q = y.fetchall()
		st = q[0][6]
		os.system("lvcreate --name {}Qrhel --size 1M userVG".format(username))
		os.system("mkfs.ext4 /dev/userVG/{}Qrhel".format(username))
		# all shared derives are stored in user's folder(nfs)
		os.system("mkdir /media/{0}rhel".format(username))
		
		#mounting nfs folder to get shared
		os.system("mount /dev/userVG/{0}Qrhel /media/{0}rhel".format(username))
		os.system("cp {} /media/{}rhel".format(st,username))
		os.system("echo '/media/{0}rhel *(rw,no_root_squash)' >> /etc/exports".format(username))
		os.system("exportfs -r")
	else:
		c.send("0")

	b = y.execute("select * from UBUNTU where USERNAME='{0}'".format(username))
	
	if b != 0L:
		c.send("1")
		t = y.fetchall()
		st = t[0][6]
		os.system("lvcreate --name {}Qub --size 1M userVG".format(username))
		os.system("mkfs.ext4 /dev/userVG/{}Qub".format(username))
		# all shared derives are stored in user's folder(nfs)
		os.system("mkdir /media/{0}ub".format(username))
		
		#mounting nfs folder to get shared
		os.system("mount /dev/userVG/{0}Qub /media/{0}ub".format(username))
		os.system("cp {} /media/{}ub".format(st,username))
		os.system("echo '/media/{0}ub *(rw,no_root_squash)' >> /etc/exports".format(username))
		os.system("exportfs -r")
	else:
		c.send("0")


	
	d = y.execute("select * from WINDOWS where USERNAME='{0}'".format(username))
		
	if d != 0L:
		c.send("1")
		f = y.fetchall()
		st = f[0][6]
		os.system("lvcreate --name {}Qwin --size 1M userVG".format(username))
		os.system("mkfs.ext4 /dev/userVG/{}Qwin".format(username))
		# all shared derives are stored in user's folder(nfs)
		os.system("mkdir /media/{0}win".format(username))
		
		#mounting nfs folder to get shared
		os.system("mount /dev/userVG/{0}Qwin /media/{0}win".format(username))
		os.system("cp {} /media/{}win".format(st,username))
		os.system("echo '/media/{0}win *(rw,no_root_squash)' >> /etc/exports".format(username))
		os.system("exportfs -r")
	else:
		c.send("0")

	os.system("exportfs -r")

	
