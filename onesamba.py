#!/usr/bin/python2

import os,commands,time

def samba(c,username,password):
	#recieving hardisk size
	s = c.recv(30)
	if s == '1':
		size = c.recv(30)
		a = commands.getstatusoutput("rpm -q samba*")
		if a[0] != 0:
		        commands.getstatusoutput("yum install samba* -y")
		os.system("lvcreate --name {}samba --size {} userVG".format(username,size))
		os.system("mkfs.ext4 /dev/mapper/userVG-{}samba".format(username))
		os.system("useradd -s /sbin/nologin {0}smb".format(username))
		os.system("smbpasswd -a {}smb".format(username))
		os.system("mkdir /media/{0}".format(username))
		os.system("mount /dev/mapper/userVG-{0}samba /media/{0}".format(username))
		os.system("echo '[{0}]\npath= /media/{0}\nwritable=yes' >> /etc/samba/smb.conf".format(username))

		import MySQLdb
		os.system("systemctl restart mariadb")
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		#doing entry in database
		y.execute("use cloud;")
		k=y.execute("UPDATE USER SET SAMBA='/dev/userVG/{0}samba' where USERNAME='{0}';".format(username))
		x.commit()			
	
		os.system("chown {0} /home/samba/{0}".format(username))
		os.system("chmod 700 /home/samba/{0}".format(username))
		os.system("systemctl restart smb")
		os.system("systemctl enable smb")
		#sending signal to client to start processing
		c.send("1")

	elif s == '2':
		#recv size
		size = c.recv(20)
		import MySQLdb
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		y.execute("use cloud;")
		e = y.execute("select SAMBA from USER where USERNAME='{}';".format(username))
		q = y.fetchall()
		if e != 0L:
			if q[0][0]== '/dev/userVG/{0}samba'.format(username):
				os.system("lvextend --size +{1} /dev/userVG/{0}samba".format(username,size))
				os.system("resize2fs /dev/mapper/userVG-{}samba".format(username))
				#sending successful signal	
				c.send("1")

		else:
			c.send("0")


	elif s == '3':
		import MySQLdb
		os.system("systemctl restart mariadb")
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		y.execute("use cloud;")
		
		x.commit()
		e = y.execute("select SAMBA from USER where USERNAME='{0}';".format(username))
		q = y.fetchall()
		if e == 1L and q[0][0]!= None:
			os.system("lvcreate --name {0}sambasnap --size 2M -s {1}".format(username,q[0][0]))
			commands.getstatusoutput("mkdir /media/{0}sambasnap".format(username))
			os.system("mount /dev/userVG/{0}sambasnap /media/{0}sambasnap".format(username))
			os.system("chown {0} /media/{0}sambasnap".format(username))
			os.system("chmod 700 /media/{0}sambasnap".format(username))
	                os.system("echo '/media/{0}sambasnap *(rw,no_root_squash)' >>/etc/exports".format(username))
			o = y.execute("update SNAP set SAMBA='/media/{0}sambasnap' where USERNAME='{0}';".format(username))
			x.commit()
	                os.system("exportfs -r")
#sending signal to client to start his processing
			c.send("1")







	"""
        size = c.recv(30)


        a = commands.getstatusoutput("rpm -q samba*")
        if a[0] != 0:
                commands.getstatusoutput("yum install samba* -y")


	#creating partition to be shared
	os.system("lvcreate --name {}samba --size {} userVG".format(username,size))
        os.system("mkfs.ext4 /dev/mapper/userVG-{}samba".format(username))
	os.system("useradd -s /sbin/nologin {0}smb".format(username))
	os.system("smbpasswd -a {}smb".format(username))
	os.system("mkdir /media/{0}".format(username))
        os.system("mount /dev/mapper/userVG-{0}samba /media/{0}".format(username))
	os.system("echo '[{0}]\npath= /media/{0}\nwritable=yes' >> /etc/samba/smb.conf".format(username))

	# doing entry to cloud table
	import MySQLdb
	os.system("systemctl restart mariadb")
	x=MySQLdb.connect("localhost")
	y=x.cursor()
	y.execute("use cloud;")
	k=y.execute("UPDATE USER SET SAMBA='/dev/userVG/{0}samba' where USERNAME='{0}';".format(username))
	x.commit()

	os.system("systemctl restart smb")
	os.system("systemctl enable smb")
	#sending signal to client to start processing
        c.send("1")
	#move = c.recv(30)

	"""


