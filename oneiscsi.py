#!/usr/bin/python2

import os,commands,time,onestaas

def iscsi(c,username,password):
	choice = c.recv(30)
	
#cancel
	if choice == '':
		onestaas.staas(c,username,password)
#add
	elif choice == '1':
	#recieving hardisk size
		size = c.recv(30)
		print size
		a = commands.getstatusoutput("rpm -q scsi-target-utils")
		if a[0] != 0:
		        commands.getstatusoutput("yum install scsi-target-utils -y")
		 #creating partition to be shared
		os.system("lvcreate --name {}iscsi --size {} userVG".format(username,size))
		os.system("mkfs.ext4 /dev/mapper/userVG-{}iscsi".format(username))
		#os.system("touch /etc/tgt/conf.d/{}.conf".format(username))
		os.system("echo '<target {0}>\nbacking-store /dev/mapper/userVG-{0}iscsi\n</target>\n' >>/etc/tgt/conf.d/share.conf".format(username))

		#doing entry in database
		import MySQLdb
		os.system("systemctl restart mariadb")
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		y.execute("use cloud;")
		k=y.execute("UPDATE USER SET ISCSI='/dev/userVG/{0}iscsi' where USERNAME='{0}';".format(username))
		x.commit()
		os.system("setenforce 0")
		os.system("systemctl restart tgtd")
		os.system("systemctl enable tgtd")
		#sending signal to client to start processing
		c.send("1")
		onestaas.staas(c,username,password)
		
#snapshot		
	elif choice == '2':
		import MySQLdb
		os.system("systemctl restart mariadb")
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		y.execute("use cloud;")
		
		x.commit()
		e = y.execute("select ISCSI from USER where USERNAME='{0}';".format(username))
		q = y.fetchall()
		if e == 1L and q[0][0]!= None:
			os.system("lvcreate --name {0}iscsisnap --size 4M -s {1}".format(username,q[0][0]))
			commands.getstatusoutput("mkdir /media/{0}iscsisnap".format(username))
			os.system("mount /dev/userVG/{0}iscsisnap /media/{0}iscsisnap".format(username))
			os.system("chown {0} /media/{0}iscsisnap".format(username))
			os.system("chmod 700 /media/{0}iscsisnap".format(username))
	                os.system("echo '/media/{0}iscsisnap *(rw,no_root_squash)' >>/etc/exports".format(username))
			o = y.execute("update SNAP set ISCSI='/media/{0}iscsisnap' where USERNAME='{0}';".format(username))
			x.commit()
	                os.system("exportfs -r")
#sending signal to client to start his processing
			c.send("1")
			onestaas.staas(c,username,password)
	


#back
	elif choice == '3':
		onestaas.staas(c,username,password)

#exit
	elif choice == '4':
		c.close()	
