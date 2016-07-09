#!/usr/bin/python2

import os,commands,time,random

def install(c,username,password):
	#recieving image
	image = c.recv(30)
	print image

	#recieving values from client
	ram = c.recv(20)
	print ram
	cpu = c.recv(30)
	print cpu
	#hdd = c.recv(30)
	#print hdd
	#os.system("yum install virt-install")



	if image == '1':
		#os.system("touch /var/lib/libvirt/{}.qcow2".format(username))
		#os.system("cp /var/lib/libvirt/images/{}.qcow2 /var/lib/libvirt/images/oja.qcow2".format(username))
		cport = random.randint(16000,17000)	
		sport = random.randint(7000,8000)

		os.system("virt-install --name {0}rhel --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/name1.qcow2 --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,ram,cpu,cport))


		import MySQLdb
		os.system("systemctl restart mariadb")
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		y.execute("use cloud;")
		a = y.execute("select * from REDHAT where USERNAME='{0}'".format(username))

#checking whether user alredy exist ar not
		if a == 0L:
			c.send("n")
			y.execute("use cloud;")
			y.execute("insert into REDHAT(USERNAME,SPORT,CPORT,RAM,CPU,TYPE) values('{0}','{1}','{2}','{3}','{4}','rhel7')".format(username,sport,cport,ram,cpu))
			
			x.commit()
			os.system("systemctl restart httpd")	
			c.send("{}".format(sport))
			c.send("1")
			os.system("qrencode -s 40*40 -o /media/{}rhel.png http://192.168.122.1/vnc/?ip=192.168.122.1&port={}".format(username,sport))
			y.execute("update REDHAT set QPATH = '/media/{0}rhel.png' where USERNAME = '{0}' ".format(username))
			x.commit()
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
		else:
			#show installed os to user
			c.send("e")
			#getting signal that user clicked 
			val = c.recv(30)
			if val == '1':
				y.execute("use cloud;")
				y.execute("select SPORT,CPORT from REDHAT where USERNAME='{0}'".format(username))
				b =  y.fetchall()
				spo = b[0][0]
				cpo = b[0][1] 
				os.system("virsh start {}rhel".format(username))
				os.system("systemctl restart httpd")	
				c.send("{}".format(spo))
				c.send("1")
				os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))

				#os.system("yum install httpd -y")
				#pid = commands.getstatusoutput("netstat -tnlp | grep {}  | awk '{print $7}' | cut -d'/' -f 1".format(port))
				#os.system("kill {}".format(pid))
		
		
		# UbUntu

	elif image == '2':

		cport = random.randint(6000,6999)	
		sport = random.randint(7000,8000)

		os.system("virt-install --name {0}ubun --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/name3.qcow2 --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,ram,cpu,cport))

		import MySQLdb
		os.system("systemctl restart mariadb")
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		y.execute("use cloud;")
		a = y.execute("select * from GALLERY where USERNAME='{0}'".format(username))
		if a == 0L:
			c.send("n")
			y.execute("use cloud;")
			y.execute("insert into UBUNTU(USERNAME,SPORT,CPORT,RAM,CPU,TYPE) values('{0}','{1}','{2}','{3}','{4}','ubuntu')".format(username,sport,cport,ram,cpu))
			x.commit()
			os.system("systemctl restart httpd")	
			c.send("{}".format(sport))
			c.send("1")
			os.system("qrencode -s 40*40 -o /media/{}ubun.png http://192.168.122.1/vnc/?ip=192.168.122.1&port={}".format(username,sport))
			y.execute("update UBUNTU set QPATH = '/media/{0}ubun.png' where USERNAME = '{0}' ".format(username))
			x.commit()
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
		else:
			#show installed os to user
			c.send("e")
			#getting signal that user clicked 
			val = c.recv(30)
			if val == '1':
				y.execute("use cloud;")
				y.execute("select SPORT,CPORT from UBUNTU where USERNAME='{0}'".format(username))
				b =  y.fetchall()
				spo = b[0][0]
				cpo = b[0][1] 
				os.system("virsh start {}ubun".format(username))
				os.system("systemctl restart httpd")	
				c.send("{}".format(spo))
				c.send("1")
				os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))

		#windows


	elif image == '3':

		cport = random.randint(6000,6999)	
		sport = random.randint(7000,8000)

		os.system("virt-install --name {0}win --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/name.qcow2 --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,ram,cpu,cport))

		import MySQLdb
		os.system("systemctl restart mariadb")
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		y.execute("use cloud;")
		a = y.execute("select * from GALLERY where USERNAME='{0}'".format(username))
		if a == 0L:
			c.send("n")
			y.execute("use cloud;")
			y.execute("insert into WINDOWS(USERNAME,SPORT,CPORT,RAM,CPU,TYPE) values('{0}','{1}','{2}','{3}','{4}','windows')".format(username,sport,cport,ram,cpu))
			x.commit()
			os.system("systemctl restart httpd")	
			c.send("{}".format(sport))
			c.send("1")
			os.system("qrencode -s 40*40 -o /media/{}win.png http://192.168.122.1/vnc/?ip=192.168.122.1&port={}".format(username,sport))
			y.execute("update WINDOWS set QPATH = '/media/{0}win.png' where USERNAME = '{0}' ".format(username))
			x.commit()
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))




		else:
			#show installed os to user
			c.send("e")
			#getting signal that user clicked 
			val = c.recv(30)
			if val == '1':
				y.execute("use cloud;")
				y.execute("select SPORT,CPORT from WINDOWS where USERNAME='{0}'".format(username))
				b =  y.fetchall()
				spo = b[0][0]
				cpo = b[0][1] 
				os.system("virsh start {}win".format(username))
				os.system("systemctl restart httpd")	
				c.send("{}".format(spo))
				c.send("1")
				os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))

