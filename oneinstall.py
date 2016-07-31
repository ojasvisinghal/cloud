#!/usr/bin/python2

import os,commands,time,random,oneiaas

def install(c,username,password):
	choice = c.recv(30)
	
#cancel
	if choice == '':
		oneiaas.iaas(c,username,password)

#Redhat
	elif choice == '1':
		ram = c.recv(30)
	#cancel	
		if ram == '':
			install(c,username,password)
	#ram 500			
		elif ram == '1':
			r = '500'
			cpu = '1'
			cport = random.randint(13000,14000)	
			sport = random.randint(14000,15000)
			ids = random.randint(29000,234567)

			import MySQLdb
			os.system("systemctl restart mariadb")
			x=MySQLdb.connect("localhost")
			y=x.cursor()
			y.execute("use cloud;")
			a = y.execute("select * from REDHAT where USERNAME='{0}500'".format(username))
			if a == 0L:
				os.system("ln /var/lib/libvirt/images/name3.qcow2 /var/lib/libvirt/images/{}rhel500.qcow2".format(username))
				os.system("virt-install --name {0}rhel500 --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/{0}rhel500.qcow2 --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,r,cpu,cport))
				os.system("virsh destroy {}rhel500".format(username))
				y.execute("use cloud;")
				y.execute("insert into REDHAT(USERNAME,SPORT,CPORT,RAM,CPU,TYPE,ID,IMAGE) values('{0}500','{1}','{2}','{3}','{4}','rhel7','{5}','{0}rhel500.qcow2')".format(username,sport,cport,r,cpu,ids))
			
				x.commit()
				os.system("systemctl restart httpd")	
				c.send("1")
				time.sleep(2)
				c.send("{}".format(sport))
				time.sleep(2)
				c.send("{}".format(ids))
				os.system("qrencode -s 40*40 -o /var/www/html/{}rhel500.png http://192.168.122.1/vnc/?ip=192.168.122.1&port={}".format(username,sport))
				os.system("chmod 777 /var/www/html/{}rhel500.png".format(username))
				os.system("setenforce 0")
				y.execute("update REDHAT set QPATH = '{0}rhel500.png' where USERNAME = '{0}500' ".format(username))
				x.commit()
				
				#os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				oneiaas.iaas(c,username,password)
			else:
				c.send("0")
				time.sleep(1) 	
				y.execute("select SPORT,CPORT from REDHAT where USERNAME='{0}500'".format(username))
				b =  y.fetchall()
				spo = b[0][0]
				cpo = b[0][1] 
				os.system("systemctl restart httpd")	
				c.send("{}".format(spo))
				#os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				oneiaas.iaas(c,username,password)

	#ram 1024
		elif ram == '2':
			r = '1024'
			cpu = '1'
			cport = random.randint(13000,17000)	
			sport = random.randint(17000,28000)
			ids = random.randint(29000,234567)

			import MySQLdb
			os.system("systemctl restart mariadb")
			x=MySQLdb.connect("localhost")
			y=x.cursor()
			y.execute("use cloud;")
			a = y.execute("select * from REDHAT where USERNAME='{0}1024'".format(username))
			if a == 0L:
				os.system("ln /var/lib/libvirt/images/name3.qcow2 /var/lib/libvirt/images/{}rhel1024.qcow2".format(username))
				os.system("virt-install --name {0}rhel1024 --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/{0}rhel1024.qcow2 --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,r,cpu,cport))
				os.system("virsh destroy {}rhel1024".format(username))
				y.execute("use cloud;")
				y.execute("insert into REDHAT(USERNAME,SPORT,CPORT,RAM,CPU,TYPE,ID,IMAGE) values('{0}1024','{1}','{2}','{3}','{4}','rhel7','{5}','{0}rhel1024.qcow2')".format(username,sport,cport,r,cpu,ids))
				x.commit()
				os.system("systemctl restart httpd")	
				c.send("1")
				time.sleep(2)
				c.send("{}".format(sport))
				time.sleep(2)
				c.send("{}".format(ids))
				os.system("qrencode -s 40*40 -o /var/www/html/{}rhel1024.png http://192.168.122.1/vnc/?ip=192.168.122.1&port={}".format(username,sport))
				os.system("chmod 777 /var/www/html/{}rhel1024.png".format(username))
				os.system("setenforce 0")
				y.execute("update REDHAT set QPATH = '{0}rhel1024.png' where USERNAME = '{0}' ".format(username))
				x.commit()
				#os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				oneiaas.iaas(c,username,password)
			else:
				c.send("0")
				time.sleep(1) 
				os.system("systemctl restart httpd")	
				y.execute("select SPORT,CPORT from REDHAT where USERNAME='{0}1024'".format(username))
				b =  y.fetchall()
				spo = b[0][0]
				cpo = b[0][1] 
				os.system("systemctl restart httpd")	
				c.send("{}".format(spo))
				#os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				oneiaas.iaas(c,username,password)




	#back
		elif ram == '3':
			oneiaas.iaas(c,username,password)
	#exit
		elif ram == '4':
			c.close()
				
# UbUntu

	elif choice == '3':
		ram = c.recv(30)
	#cancel	
		if ram == '':
			pass
	#ram 500		
		elif ram == '1':
			r = '500'
			cpu = '1'
			cport = random.randint(13000,14000)	
			sport = random.randint(14000,15000)
			ids = random.randint(29000,234567)

			import MySQLdb
			os.system("systemctl restart mariadb")
			x=MySQLdb.connect("localhost")
			y=x.cursor()
			y.execute("use cloud;")
			a = y.execute("select * from WINDOWS where USERNAME='{0}500'".format(username))
			if a == 0L:
				os.system("qemu-img create -f qcow2 -b /var/lib/libvirt/images/windows.qcow2 /var/lib/libvirt/images/{}win500.qcow2".format(username))
				os.system("virt-install --name {0}win500 --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/{0}win500.qcow2 --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,r,cpu,cport))
				os.system("virsh destroy {}win500".format(username))
				y.execute("use cloud;")
				y.execute("insert into WINDOWS(USERNAME,SPORT,CPORT,RAM,CPU,TYPE,ID,IMAGE) values('{0}500','{1}','{2}','{3}','{4}','windows','{5}','{0}win500.qcow2')".format(username,sport,cport,r,cpu,ids))
			
				x.commit()
				os.system("systemctl restart httpd")	
				c.send("1")
				time.sleep(2)
				c.send("{}".format(sport))
				time.sleep(2)
				c.send("{}".format(ids))
				os.system("qrencode -s 40*40 -o /var/www/html/{}win500.png http://192.168.122.1/vnc/?ip=192.168.122.1&port={}".format(username,sport))
				os.system("chmod 777 /var/www/html/{}win500.png".format(username))
				os.system("setenforce 0")
				y.execute("update WINDOWS set QPATH = '{0}win500.png' where USERNAME = '{0}500' ".format(username))
				x.commit()
				
				#os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				oneiaas.iaas(c,username,password)
			else:
				c.send("0")
				time.sleep(1) 	
				y.execute("select SPORT,CPORT from WINDOWS where USERNAME='{0}500'".format(username))
				b =  y.fetchall()
				spo = b[0][0]
				cpo = b[0][1] 
				os.system("systemctl restart httpd")	
				c.send("{}".format(spo))
				#os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				oneiaas.iaas(c,username,password)
	#ram 1024
		elif ram == '2':
			r = '1024'
			cpu = '1'
			cport = random.randint(13000,17000)	
			sport = random.randint(17000,28000)
			ids = random.randint(29000,234567)

			import MySQLdb
			os.system("systemctl restart mariadb")
			x=MySQLdb.connect("localhost")
			y=x.cursor()
			y.execute("use cloud;")
			a = y.execute("select * from WINDOWS where USERNAME='{0}1024'".format(username))
			if a == 0L:
				os.system("qemu-img create -f qcow2 -b /var/lib/libvirt/images/windows.qcow2 /var/lib/libvirt/images/{}win1024.qcow2".format(username))
				os.system("virt-install --name {0}rhel1024 --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/{0}win1024.qcow2 --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,r,cpu,cport))
				os.system("virsh destroy {}win1024".format(username))
				y.execute("use cloud;")
				y.execute("insert into WINDOWS(USERNAME,SPORT,CPORT,RAM,CPU,TYPE,ID,IMAGE) values('{0}1024','{1}','{2}','{3}','{4}','rhel7','{5}','{0}win1024.qcow2')".format(username,sport,cport,r,cpu,ids))
				x.commit()
				os.system("systemctl restart httpd")	
				c.send("1")
				time.sleep(2)
				c.send("{}".format(sport))
				time.sleep(2)
				c.send("{}".format(ids))
				os.system("qrencode -s 40*40 -o /var/www/html/{}win1024.png http://192.168.122.1/vnc/?ip=192.168.122.1&port={}".format(username,sport))
				os.system("chmod 777 /var/www/html/{}win1024.png".format(username))
				os.system("setenforce 0")
				y.execute("update WINDOWS set QPATH = '{0}rhel1024.png' where USERNAME = '{0}' ".format(username))
				x.commit()
				#os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				oneiaas.iaas(c,username,password)
			else:
				c.send("0")
				time.sleep(1) 
				os.system("systemctl restart httpd")	
				y.execute("select SPORT,CPORT from WINDOWS where USERNAME='{0}1024'".format(username))
				b =  y.fetchall()
				spo = b[0][0]
				cpo = b[0][1] 
				os.system("systemctl restart httpd")	
				c.send("{}".format(spo))
				#os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				oneiaas.iaas(c,username,password)


	#back
		elif ram == '3':
			oneiaas.iaas(c,username,password)
	#exit
		elif ram == '4':
			c.close()

#windows
	elif choice == '2':
		ram = c.recv(30)
	#cancel	
		if ram == '':
			pass
	#ram 500		
		elif ram == '1':
			pass
	#ram 1024
		elif ram == '2':
			pass
	#back
		elif ram == '3':
			oneiaas.iaas(c,username,password)
	#exit
		elif ram == '4':
			c.close()

#fedora
	elif choice == '4':
		ram = c.recv(30)
	#cancel	
		if ram == '':
			pass
	#ram 500		
		elif ram == '1':
			pass
	#ram 1024
		elif ram == '2':
			pass
	#back
		elif ram == '3':
			oneiaas.iaas(c,username,password)
	#exit
		elif ram == '4':
			c.close()
#mintos
	elif choice == '5':
		ram = c.recv(30)
	#cancel	
		if ram == '':
			pass
	#ram 500		
		elif ram == '1':
			pass
	#ram 1024
		elif ram == '2':
			pass
	#back
		elif ram == '3':
			oneiaas.iaas(c,username,password)
	#exit
		elif ram == '4':
			c.close()

#kalilinux
	elif choice == '6':
		ram = c.recv(30)
	#cancel	
		if ram == '':
			pass
	#ram 500		
		elif ram == '1':
			pass
	#ram 1024
		elif ram == '2':
			pass
	#back
		elif ram == '3':
			oneiaas.iaas(c,username,password)
	#exit
		elif ram == '4':
			c.close()

#back
	elif choice == '7':
		ram = c.recv(30)
	#cancel	
		if ram == '':
			pass
	#ram 500		
		elif ram == '1':
			pass
	#ram 1024
		elif ram == '2':
			pass
	#back
		elif ram == '3':
			oneiaas.iaas(c,username,password)
	#exit
		elif ram == '4':
			c.close()

#exit
	elif choice == '8':
		c.close()
