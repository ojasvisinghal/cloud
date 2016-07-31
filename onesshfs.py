#!/usr/bin/python2
import commands,os,time,onestaas

def sshfs(c,username,password):

	s = c.recv(30)
#cancel 
	if s == '':
		onestaas.staas(c,username,password)

#add
	elif s == '1':
		size = c.recv(30)
		a = commands.getstatusoutput("rpm -q openssh-server")
		if a[0] != 0:
		        commands.getstatusoutput("yum install openssh-server -y")
		#commands.getstatusoutput("cp -rf /etc/skel /home/cloud/{}".format(username))
		os.system("lvcreate --name {}sshfs --size {} userVG".format(username,size))
		os.system("mkfs.ext4 /dev/mapper/userVG-{}sshfs".format(username))
		os.system("mkdir /home/sshfs/{0}".format(username))
		os.system("mount /dev/mapper/userVG-{0}sshfs /home/sshfs/{0}".format(username))

		import MySQLdb
		os.system("systemctl restart mariadb")
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		#doing entry in database
		y.execute("use cloud;")
		k=y.execute("UPDATE USER SET SSHFS='/dev/userVG/{0}sshfs' where USERNAME='{0}';".format(username))
		x.commit()			
	
		os.system("chown {0} /home/sshfs/{0}".format(username))
		os.system("chmod 700 /home/sshfs/{0}".format(username))
		os.system("systemctl restart sshd")
		os.system("systemctl enable sshd")
		#sending signal to client to start processing
		c.send("1")
		onestaas.staas(c,username,password)

#extend
	elif s == '2':
		#recv size
		size = c.recv(20)
		import MySQLdb
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		y.execute("use cloud;")
		e = y.execute("select SSHFS from USER where USERNAME='{}';".format(username))
		q = y.fetchall()
		if e != 0L:
			if q[0][0]== '/dev/userVG/{0}sshfs'.format(username):
				os.system("lvextend --size +{1} /dev/userVG/{0}sshfs".format(username,size))
				os.system("resize2fs /dev/mapper/userVG-{}sshfs".format(username))
				#sending successful signal	
				c.send("1")
				onestaas.staas(c,username,password)

		else:
			c.send("0")
			onestaas.staas(c,username,password)


#snapshot
	elif s == '3':
		import MySQLdb
		os.system("systemctl restart mariadb")
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		y.execute("use cloud;")
		
		x.commit()
		e = y.execute("select SSHFS from USER where USERNAME='{0}';".format(username))
		q = y.fetchall()
		if e == 1L and q[0][0]!= None:
			os.system("lvcreate --name {0}sshfssnap --size 2M -s {1}".format(username,q[0][0]))
			commands.getstatusoutput("mkdir /media/{0}sshfssnap".format(username))
			os.system("mount /dev/userVG/{0}sshfssnap /media/{0}sshfssnap".format(username))
			os.system("chown {0} /media/{0}sshfssnap".format(username))
			os.system("chmod 700 /media/{0}sshfssnap".format(username))
	                os.system("echo '/media/{0}sshfssnap *(rw,no_root_squash)' >>/etc/exports".format(username))
			o = y.execute("update SNAP set SSHFS='/media/{0}sshfssnap' where USERNAME='{0}';".format(username))
			x.commit()
	                os.system("exportfs -r")
		#sending signal to client to start his processing
			c.send("1")
			onestaas.staas(c,username,password)

#back
	elif s == '4':
		onestaas.staas(c,username,password)

#exit
	elif s == '5':
		c.close()
