#!/usr/bin/python2

import os,commands,user,MySQLdb,random

x=MySQLdb.connect("localhost")
y=x.cursor()

def staas(c,username,password):
	#recieving choice from client which service to start
	choice = c.recv(30)
	os.system("dialog --infobox 'donw' 10 20")
	if choice == '1':
		#recieving which service user wants
		data = c.recv(30)
		#recieveing whether to extend add or remove
		#add = c.recv(30)

		if data == '1':
			#recieving hardisk size
			size = c.recv(30)
			y = commands.getstatusoutput("rpm -q nfs-utils")
			
			if y[0]!=0:
				commands.getstatusoutput("yum install nfs-utils -y")
	
			os.system("lvcreate --name {}nfs --size {} userVG".format(username,size))
                        os.system("mkfs.ext4 /dev/userVG/{}nfs".format(username))
			# all shared derives are stored in user's folder(nfs)
                        os.system("mkdir /home/{0}/{0}".format(username))
                        #mounting nfs folder to get shared
                        os.system("mount /dev/userVG/{0}nfs /home/{0}/{0}".format(username))
			
			#doing entry in database
			y.execute("use cloud;")
			k=y.execute("UPDATE USER SET NFS='/dev/userVG/{0}nfs' where USERNAME='{0}';".format(username))
			x.commit()

                        os.system("echo '/home/{0}/{0} *(rw,no_root_squash)' >> /etc/exports".format(username))
                        os.system("systemctl restart nfs-server")
                        os.system("systemctl enable nfs-server")

			#sending signal to client to start his processing

			c.send("1")
			
	
#sshfs server
		elif data == '2':
			#recieving hardisk size
                        size = c.recv(30)
			a = commands.getstatusoutput("rpm -q openssh-server")
                        if a[0] != 0:
                                commands.getstatusoutput("yum install openssh-server -y")
                        #commands.getstatusoutput("cp -rf /etc/skel /home/cloud/{}".format(username))
                        os.system("lvcreate --name {}sshfs --size {} userVG".format(username,size))
                        os.system("mkfs.ext4 /dev/mapper/userVG-{}sshfs".format(username))
                        os.system("mkdir /home/{0}/{0}".format(username))
                        os.system("mount /dev/mapper/userVG-{0}sshfs /home/{0}/{0}".format(username))
#for snapshot work
                        #commands.getstatusoutput("echo '/dev/mapper/userVG-{}' >>/root/Desktop/CloudServer/snapshotfile.txt")


			#doing entry in database
			y.execute("use cloud;")
			k=y.execute("UPDATE USER SET SSHFS='/dev/userVG/{0}sshfs' where USERNAME='{0}';".format(username))
			x.commit()			
			
                        os.system("chown {0} /home/{0}/{0}".format(username))
                        os.system("chmod 700 /home/{}/{0}".format(username))
                        os.system("systemctl restart sshd")
			os.system("systemctl enable sshd")
                        #sending signal to client to start processing
			c.send("1")
			#move = c.recv(30)

#samba server
		elif data == '3':
	#recieving hardisk size
                        size = c.recv(30)
                        a = commands.getstatusoutput("rpm -q samba*")
                        if a[0] != 0:
                                commands.getstatusoutput("yum install samba* -y")
			#creating partition to be shared
			os.system("lvcreate --name {} --size {} userVG".format(username,size))
                        os.system("mkfs.ext4 /dev/mapper/userVG-{}".format(username))
                       # os.system("mkdir /home/{0}/samba".format(username))
                        #os.system("mount /dev/mapper/userVG-{0} /home/{0}/samba".format(username))
#for snapshot work
                        #commands.getstatusoutput("echo '/dev/mapper/userVG-{}' >>/root/Desktop/CloudServer/snapshotfile.txt")
                        #os.system("chown {0} /home/{0}/samba".format(username))
                       # os.system("chmod 700 /home/{}/samba".format(username))
#making entry to config file of samba
		#	os.system("echo '[{0}]\npath= /home/{0}/samba\nwritable=yes' >> /etc/samba/smb.conf".format(username))
			
			os.system("useradd -d /home/{0} -s /sbin/nologin {0}".format(username))
			os.system("echo {} | smbpasswd -a {} --stdin".format(password,username))
			os.system("mkdir /media/{0}".format(username))
                        os.system("mount /dev/mapper/userVG-{0}samba /media/{0}".format(username))
			os.system("echo '[{0}]\npath= /media/{0}\nwritable=yes' >> /etc/samba/smb.conf".format(username))

			# doing entery to cloud table
			y.execute("use cloud;")
			k=y.execute("UPDATE USER SET SAMBA='/dev/userVG/{0}samba' where USERNAME='{0}';".format(username))
			x.commit()

			os.system("systemctl restart smb")
			os.system("systemctl enable smb")
			#sending signal to client to start processing
                        c.send("1")
			#move = c.recv(30)





#extend
		elif data == '4':
			# checking database whether any drive exist with username
			# writing all existing lvs in a file


			fh = open("/root/Desktop/folderServer/derive.txt",'w')
			q =y.execute("select NFS from USER where USERNAME='{}';".format(username))
			if q[0][0]!= 'None':
				fh.write("{}\n".format(q[0][0]))
			q =y.execute("select SSHFS from USER where USERNAME='{}';".format(username))
			if q[0][0]!= 'None':
				fh.write("{}\n".format(q[0][0]))
			q =y.execute("select ISCSI from USER where USERNAME='{}';".format(username))
			if q[0][0]!= 'None':
				fh.write("{}\n".format(q[0][0]))
			q =y.execute("select SAMBA from USER where USERNAME='{}';".format(username))
			if q[0][0]!= 'None':
				fh.write("{}\n".format(q[0][0]))

			fh.close()

			#send this file to client
						

			#receiving name of hardisk
			name = c.recv(100)
			#recieving harddisk size
			size = c.recv(40)
			os.system("lvextend --name {} --size +{} userVG".format(username,size))
			os.system("resize2fs /dev/mapper/userVG-{}".format(username))
			#sending successful signal	
			c.send("1")	




# remove
		elif data == '5':
			

# checking database whether any drive exist with username
			# writing all existing lvs in a file


			fh = open("/root/Desktop/folderServer/derive.txt",'w')
			q =y.execute("select NFS from USER where USERNAME='{}';".format(username))
			if q[0][0]!= 'None':
				fh.write("{}\n".format(q[0][0]))
			q =y.execute("select SSHFS from USER where USERNAME='{}';".format(username))
			if q[0][0]!= 'None':
				fh.write("{}\n".format(q[0][0]))
			q =y.execute("select ISCSI from USER where USERNAME='{}';".format(username))
			if q[0][0]!= 'None':
				fh.write("{}\n".format(q[0][0]))
			q =y.execute("select SAMBA from USER where USERNAME='{}';".format(username))
			if q[0][0]!= 'None':
				fh.write("{}\n".format(q[0][0]))

			fh.close()

#send this file to client
						

			#receiving name of hardisk
			name = c.recv(100)
			os.system("lvremove /dev/mapper/userVG-{} -y".format(username))
			#sending successful signal	
			c.send("1")



#block storage
	elif choice == '2':
		#recieving which service user wants
                data = c.recv(30)
#iscsi
		if data == '1':
			#recieving hardisk size
                        size = c.recv(30)
                        a = commands.getstatusoutput("rpm -q scsi-target-utils")
                        if a[0] != 0:
                                commands.getstatusoutput("yum install scsi-target-utils -y")
			 #creating partition to be shared
                        os.system("lvcreate --name {}iscsi --size {} userVG".format(username,size))
                        os.system("mkfs.ext4 /dev/mapper/userVG-{}iscsi".format(username))
                        #no need of mount in iscsi
			#os.system("mkdir /home/{}/iscsi".format(username))
                        #os.system("mount /dev/mapper/userVG-{0} /home/{0}/iscsi".format(username))
			os.system("touch /etc/tgt/conf.d/{}.conf".format(username))
			os.system("echo '<target {0}>\nbacking-store /dev/mapper/userVG-{0}iscsi\n</target>' >>/etc/tgt/conf.d/{0}.conf".format(username))

			#doing entry in database
			y.execute("use cloud;")
			k=y.execute("UPDATE USER SET ISCSI='/dev/userVG/{0}iscsi' where USERNAME='{0}';".format(username))

			os.system("systemctl restart tgtd")
			os.system("systemctl enable tgtd")
			#sending signal to client to start processing
			c.send("1")
			


#snapshot
		elif data == '2':
			q =y.execute("select ISCSI from USER where USERNAME='{}';".format(username))
			if q[0][0]!= 'None':
				os.system("lvcreate --name {}snap --size 2M -s {}".format(q[0][0]))
				os.system("mkdir /media/{0}snap".format(username))
				os.system("mount /dev/userVG/{0}snap /media/{0}snap".format(username))
				os.system("chown {0} /media/{0}snap".format(username))
				os.system("chmod 700 /media/{0}snap".format(username))
			
		                os.system("echo '/media/{0}snap *(rw,no_root_squash)' >> /etc/exports".format(username))
		                os.system("systemctl restart nfs-server")
		                os.system("systemctl enable nfs-server")
#sending signal to client to start his processing

				c.send("1")
			

# back option
	elif choice == '3':
		pass


############################################################################################################################################

def iaas(c,username,password):
	#recieving choice
	choice = c.recv(30)
#gallery


	if choice == '1':
		#fetching all os with this user
		y.execute("use cloud;")
		q = y.execute("select * from GALLERY where USERNAME='{}'".format(username))
		if q == 0L:
			#return signal that no os yet installed	
			c.send('0')		
		else:
			c.send('1')
			p = y.fetchall()
			if p[0][1] != 'None':
				p1 = 0
				# picking UBuntu image
				port1 = p[0][2]
				print port1
			else:
				p1 = 1

			if p[0][3] != 'None':
				# picking UBuntu image
				p2 = 0
				port2 = p[0][4]
				print port2

			else:
				p2 = 1

			if p[0][5] != 'None':
				p3 = 0
				# picking UBuntu image
				port3 = p[0][6]
				print port3

			else:
				p3 = 1


			#sending p1 p2 p3
			c.send(p1)
			c.send(p2)
			c.send(p3)

			if p1 == '0':
				c.send(port1)
			if p2 == '0':
				c.send(port2)
			if p3 == '0':
				c.send(port3)

	
#install

	elif choice == '2':
	#recieving image
		image = c.recv(30)

	#recieving values from client
		ram = c.recv(20)
		print ram
		cpu = c.recv(30)
		print cpu
		hdd = c.recv(30)
		print hdd
		#os.system("yum install virt-install")
		

#linux
	if image == '1':
		#os.system("touch /var/lib/libvirt/{}.qcow2".format(username))
		#os.system("cp /var/lib/libvirt/images/{}.qcow2 /var/lib/libvirt/images/oja.qcow2".format(username))
		port = random.randint(6000,6999)	
		sss = random.randint(7000,8000)

		os.system("virt-install --name {0}rhel --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/name.qcow2 --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,ram,cpu,port))


		a = y.execute("select * from GALLERY where USERNAME='{0}'".format(username))
		if a == 0L:
		#checking whether user alredy exist ar not
			y.execute("use GALLERY;")
			y.execute("insert into GALLERY(USERNAME,REDHAT,PORT2) values('{0}','rhel7','{1}')".format(username,sss))
			x.commit()
		else:
			y.execute("use GALLERY;")
			y.execute("insert into GALLERY(REDHAT,PORT2) values('rhel7','{0}')".format(sss))
			x.commit()

		#os.system("yum install httpd -y")
		os.system("systemctl restart httpd")
		
		#pid = commands.getstatusoutput("netstat -tnlp | grep {}  | awk '{print $7}' | cut -d'/' -f 1".format(port))
		#os.system("kill {}".format(pid))
		


	#sending msg to client
		c.send("{}".format(sss))
                c.send("1")

		os.system("/root/Desktop/websockify-master/run 192.168.122.1:{} 192.168.122.1:{}".format(sss,port))
				


# UbUntu

	elif image == '2':
		
		port = random.randint(6000,6999)	
		sss = random.randint(7000,8000)

		os.system("virt-install --name {0}rhel --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/name.qcow2 --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,ram,cpu,port))


		a = y.execute("select * from GALLERY where USERNAME='{0}'".format(username))
		if a == 0L:
		#checking whether user alredy exist ar not
			y.execute("use GALLERY;")
			y.execute("insert into GALLERY(USERNAME,UBUNTU,PORT1) values('{0}','ubuntu','{1}')".format(username,sss))
			x.commit()
		else:
			y.execute("use GALLERY;")
			y.execute("insert into GALLERY(UBUNTU,PORT1) values('ubuntu','{0}')".format(sss))
			x.commit()
		os.system("systemctl restart httpd")
	#sending msg to client
		c.send("{}".format(sss))
                c.send("1")
		os.system("/root/Desktop/websockify-master/run 192.168.122.1:{} 192.168.122.1:{}".format(sss,port))


#windows


	elif image == '3':
		
		port = random.randint(6000,6999)	
		sss = random.randint(7000,8000)

		os.system("virt-install --name {0}rhel --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/name.qcow2 --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,ram,cpu,port))


		a = y.execute("select * from GALLERY where USERNAME='{0}'".format(username))
		if a == 0L:
		#checking whether user alredy exist ar not
			y.execute("use GALLERY;")
			y.execute("insert into GALLERY(USERNAME,WINDOWS,PORT3) values('{0}','ubuntu','{1}')".format(username,sss))
			x.commit()
		else:
			y.execute("use GALLERY;")
			y.execute("insert into GALLERY(WINDOWS,PORT3) values('ubuntu','{0}')".format(sss))
			x.commit()

		os.system("systemctl restart httpd")
	#sending msg to client
		c.send("{}".format(sss))
                c.send("1")
		os.system("/root/Desktop/websockify-master/run 192.168.122.1:{} 192.168.122.1:{}".format(sss,port))




###########################################################################################################################################
	#migrate
	"""
		os.system("virt-install --name {0} --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/oja.qcow2 --vcpus {2} --os-type linux --graphics vnc,port=5999,listen = 0.0.0.0".format(username,ram,cpu))

                os.system("setenforce 0")
                os.system("iptables -F")
                fh =open("/etc/exports",'a')
                fh.write("/var/lib/libvirt/images/oja.qcow2 *(rw)\n")
                fh.close()

                os.system("systemctl restart nfs-server")
                os.system("chmod 777 /var/lib/libvirt/images/*")
        #get ip of client in ip ip[1][0]        
                os.system("virsh migrate --live {} qemu+ssh://{}/system".format(username,ip))

	"""  

	
###############################################################################################################################################
def paas(c,username,password):
	#registering user for paas as a service
	#getting signal what user want
	choice = c.recv(30)
#python
	if choice == '1':
	#startting docker
	#register user
		
		#mounting this to docker
		fh = open("/root/Desktop/folderServer/v.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("os.system('useradd -s /usr/bin/python {}')\n".format(username))
		fh.write("os.system('echo {} | passwd {} --stdin')\n".format(password,username))
		fh.close()

		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dock bash")
		os.system("chmod +x /root/Desktop/folderServer/v.py")
		os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
		os.system("docker exec {} service sshd restart".format(y[1]))
		ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))
		#sending ip to client to connect through docker
		c.send(ip[1])
	
#mysql
	elif choice == '2':
		#mounting this to docker
		fh = open("/root/Desktop/folderServer/v.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("os.system('useradd -s /usr/bin/python {}')\n".format(username))
		fh.write("os.system('echo {} | passwd {} --stdin')\n".format(password,username))
		fh.close()

		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dock bash")
		os.system("chmod +x /root/Desktop/folderServer/v.py")
		os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
		os.system("docker exec {} service sshd restart".format(y[1]))
		ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))
		#ip = cco,ommands.getstatusoutput("hostname -i")
		#sending ip to client to connect through docker
		c.send(ip[1])

#go lang
	elif choice == '3':
		#mounting this to docker
		fh = open("/root/Desktop/folderServer/v.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("os.system('useradd -s /usr/bin/python {}')\n".format(username))
		fh.write("os.system('echo {} | passwd {} --stdin')\n".format(password,username))
		fh.close()

		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dock bash")
		os.system("chmod +x /root/Desktop/folderServer/v.py")
		os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
		os.system("docker exec {} service sshd restart".format(y[1]))
		ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))
		#ip = cco,ommands.getstatusoutput("hostname -i")
		#sending ip to client to connect through docker
		c.send(ip[1])





##############################################################################################################################################

def saas(c,username,password):
	choice = c.recv(30)
	if choice == '1':
		#getting signal to register user
		os.system("useradd -s /usr/bin/firefox  {0}fire".format(username))
		os.system("echo {} | passwd {}fire --stdin".format(password,username))
		#starting service and sending signal to user
		#c.send("1")
		os.system("systemctl restart sshd")
		os.system("systemctl enable sshd")
		c.send("1")

	elif choice == '2':
                #getting signal to register user
                os.system("useradd -s /usr/bin/gedit {0}gedit".format(username))
                os.system("echo {} | passwd {}gedit".format(password,username))
                #starting service and sending signal to user
                #c.send("1")
                os.system("systemctl restart sshd")
                os.system("systemctl enable sshd")
		c.send("1")

	elif choice == '3':
		 #getting signal to register user
                os.system("useradd  -s /usr/bin/vlc {0}vlc".format(username))
                os.system("echo {} | passwd {}vlc".format(password,username))
                #starting service and sending signal to user
                #c.send("1")
                os.system("systemctl restart sshd")
                os.system("systemctl enable sshd")
		c.send("1")
#saas completed



##############################################################################################################################################

def caas(c,username,password):
	choice = c.recv(30)
#centos
	if choice == '1':
		#mounting this to docker
		fh = open("/root/Desktop/folderServer/v.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("os.system('useradd {}')\n".format(username))
		fh.write("os.system('echo {} | passwd {} --stdin')\n".format(password,username))
		fh.close()

		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dock bash")
		os.system("chmod +x /root/Desktop/folderServer/v.py")
		os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
		os.system("docker exec {} service sshd restart".format(y[1]))
		ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))
		#sending ip to client to connect through docker
		c.send(ip[1])
	

#ubuntu
	elif choice == '2':
                #startting docker
	#register user
		
		#mounting this to docker
		fh = open("/root/Desktop/folderServer/v.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("os.system('useradd {}')\n".format(username))
		fh.write("os.system('echo {} | passwd {} --stdin')\n".format(password,username))
		fh.close()

		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dock bash")
		os.system("chmod +x /root/Desktop/folderServer/v.py")
		os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
		os.system("docker exec {} service sshd restart".format(y[1]))
		ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))
		#sending ip to client to connect through docker
		c.send(ip[1])


#mint
	elif choice == '3':
		#mounting this to docker
		fh = open("/root/Desktop/folderServer/v.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("os.system('useradd {}')\n".format(username))
		fh.write("os.system('echo {} | passwd {} --stdin')\n".format(password,username))
		fh.close()

		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dock bash")
		os.system("chmod +x /root/Desktop/folderServer/v.py")
		os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
		os.system("docker exec {} service sshd restart".format(y[1]))
		ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))
		#sending ip to client to connect through docker
		c.send(ip[1])
#caas completed
###############################################################################################################################################
