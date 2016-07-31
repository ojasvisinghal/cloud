#!/usr/bin/python2
import os,commands,time,oneiaas,random

def ossnap(c,username,password):

	choice = c.recv(10)

#cancel
	if choice == '':
		oneiaas.iaas(c,username,password)

#take snap
	elif choice == '1':

		ids  = c.recv(40)
		import MySQLdb
		os.system("systemctl restart mariadb")
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		y.execute("use cloud;")
		w1 = y.execute("select * from REDHAT where USERNAME='{}500' and ID='{}'".format(username,ids))
		w2 = y.execute("select * from UBUNTU where USERNAME='{}500' and ID='{}'".format(username,ids))
		w3 = y.execute("select * from WINDOWS where USERNAME='{}500' and ID='{}'".format(username,ids))
		w4 = y.execute("select * from FEDORA where USERNAME='{}500' and ID='{}'".format(username,ids))
		w5 = y.execute("select * from MINT where USERNAME='{}500' and ID='{}'".format(username,ids))
		w6 = y.execute("select * from KALI where USERNAME='{}500' and ID='{}'".format(username,ids))
		w7 = y.execute("select * from REDHAT where USERNAME='{}1024' and ID='{}'".format(username,ids))
		w8 = y.execute("select * from UBUNTU where USERNAME='{}1024' and ID='{}'".format(username,ids))
		w9 = y.execute("select * from WINDOWS where USERNAME='{}1024' and ID='{}'".format(username,ids))
		w10 = y.execute("select * from FEDORA where USERNAME='{}1024' and ID='{}'".format(username,ids))
		w11 = y.execute("select * from MINT where USERNAME='{}1024' and ID='{}'".format(username,ids))
		w12 = y.execute("select * from KALI where USERNAME='{}1024' and ID='{}'".format(username,ids))

		if w1 == 0L and w2 == 0L and w3 == 0L and w4 == 0L and w5 == 0L and w6 == 0L and w7 == 0L and w8 == 0L and w9 == 0L and w10 == 0L and w11 == 0L:
			#return signal that no os yet installed	
			c.send("0")
			i = c.recv(20)
			if i == '':
				ossnap(c,username,password)
			oneiaas.iaas(c,username,password)

		else:
			time.sleep(2)
			c.send("1")
			if y.execute("select * from REDHAT where USERNAME='{}500' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				image = q[0][10]
				os.system("ln /var/lib/libvirt/images/{0} /var/lib/libvirt/images/{1}rhel500snap.qcow2".format(image,username))
				y.execute("update REDHAT set SNAP='{0}rhel500snap.qcow2' where USERNAME='{0}500' and ID='{1}'".format(username,ids))
				x.commit()
				c.send("2")#successfull signal
				print 'ffiiii'
				oneiaas.iaas(c,username,password)
			
	
			elif y.execute("select * from UBUNTU where USERNAME='{}500' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				sport1 = q[0][1]
				#os.system("virsh start {}ubun500".format(username))
				c.send(sport1)

			elif y.execute("select * from WINDOWS where USERNAME='{}500' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				sport1 = q[0][1]
				#os.system("virsh start {}win500".format(username))
				c.send(sport1)
		
		
			elif y.execute("select * from FEDORA where USERNAME='{}500' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				sport1 = q[0][1]
				#os.system("virsh start {}fed500".format(username))
				c.send(sport1)

			elif y.execute("select * from MINT where USERNAME='{}500' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				sport1 = q[0][1]
				#os.system("virsh start {}mint500".format(username))
				c.send(sport1)

		
			elif y.execute("select * from KALI where USERNAME='{}500' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				sport1 = q[0][1]
				#os.system("virsh start {}kali500".format(username))
				c.send(sport1)
	#1024
		
			elif y.execute("select * from REDHAT where USERNAME='{}1024' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				sport1 = q[0][1]
				#os.system("virsh start {}rhel1024".format(username))
				c.send(sport1)

	 		
			elif y.execute("select * from UBUNTU where USERNAME='{}1024' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				sport1 = q[0][1]
				#os.system("virsh start {}ubun1024".format(username))
				c.send(sport1)

		
			elif y.execute("select * from WINDOWS where USERNAME='{}1024' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				sport1 = q[0][1]
				#os.system("virsh start {}win1024".format(username))
				c.send(sport1)
		
		
			elif y.execute("select * from FEDORA where USERNAME='{}1024' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				sport1 = q[0][1]
				#os.system("virsh start {}fed1024".format(username))
				c.send(sport1)

		
			elif y.execute("select * from MINT where USERNAME='{}1024' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				sport1 = q[0][1]
				#os.system("virsh start {}mint1024".format(username))
				c.send(sport1)

		
			elif y.execute("select * from KALI where USERNAME='{}1024' and ID='{}'".format(username,ids))== 1L:
				q = y.fetchall()
				sport1 = q[0][1]
				#os.system("virsh start {}kali1024".format(username))
				c.send(sport1)

		
	
#see snap

	elif choice == '2':
		ids  = c.recv(40)
		import MySQLdb
		os.system("systemctl restart mariadb")
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		y.execute("use cloud;")
		w1 = y.execute("select * from REDHAT where USERNAME='{}500' and ID='{}'".format(username,ids))
		w2 = y.execute("select * from UBUNTU where USERNAME='{}500' and ID='{}'".format(username,ids))
		w3 = y.execute("select * from WINDOWS where USERNAME='{}500' and ID='{}'".format(username,ids))
		w4 = y.execute("select * from FEDORA where USERNAME='{}500' and ID='{}'".format(username,ids))
		w5 = y.execute("select * from MINT where USERNAME='{}500' and ID='{}'".format(username,ids))
		w6 = y.execute("select * from KALI where USERNAME='{}500' and ID='{}'".format(username,ids))
		w7 = y.execute("select * from REDHAT where USERNAME='{}1024' and ID='{}'".format(username,ids))
		w8 = y.execute("select * from UBUNTU where USERNAME='{}1024' and ID='{}'".format(username,ids))
		w9 = y.execute("select * from WINDOWS where USERNAME='{}1024' and ID='{}'".format(username,ids))
		w10 = y.execute("select * from FEDORA where USERNAME='{}1024' and ID='{}'".format(username,ids))
		w11 = y.execute("select * from MINT where USERNAME='{}1024' and ID='{}'".format(username,ids))
		w12 = y.execute("select * from KALI where USERNAME='{}1024' and ID='{}'".format(username,ids))

		if w1 == 0L and w2 == 0L and w3 == 0L and w4 == 0L and w5 == 0L and w6 == 0L and w7 == 0L and w8 == 0L and w9 == 0L and w10 == 0L and w11 == 0L:
			#return signal that no os yet installed	
			c.send("0")
			i = c.recv(20)
			if i == '':
				ossnap(c,username,password)
			oneiaas.iaas(c,username,password)

		else:
			time.sleep(2)
			c.send("1")
			if y.execute("select * from REDHAT where USERNAME='{}500' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				image = q[0][9]
				r = q[0][3]
				cpu = q[0][4]
				cport = random.randint(20000,30000)
				sport = random.randint(7000,9000)
				os.system("virt-install --name {0}rhel500snap --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/{4} --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,r,cpu,cport,image))
				c.send("{}".format(sport))
				os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				signal = c.recv(10)
				if signal == '3':
					os.system("virsh destroy {}rhel500snap".format(username))	
				oneiaas.iaas(c,username,password)
			
	
			elif y.execute("select * from UBUNTU where USERNAME='{}500' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				image = q[0][9]
				r = q[0][3]
				cpu = q[0][4]
				cport = random.randint(20000,30000)
				sport = random.randint(7000,9000)
				os.system("virt-install --name {0}ubun500snap --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/{4} --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,r,cpu,cport,image))
				c.send("{}".format(sport))
				os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				signal = c.recv(10)
				if signal == '3':
					os.system("virsh destroy {}ubun500snap".format(username))	
				oneiaas.iaas(c,username,password)

			elif y.execute("select * from WINDOWS where USERNAME='{}500' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				image = q[0][9]
				r = q[0][3]
				cpu = q[0][4]
				cport = random.randint(20000,30000)
				sport = random.randint(7000,9000)
				os.system("virt-install --name {0}win500snap --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/{4} --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,r,cpu,cport,image))
				c.send("{}".format(sport))
				os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				signal = c.recv(10)
				if signal == '3':
					os.system("virsh destroy {}win500snap".format(username))	
				oneiaas.iaas(c,username,password)
		
		
			elif y.execute("select * from FEDORA where USERNAME='{}500' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				image = q[0][9]
				r = q[0][3]
				cpu = q[0][4]
				cport = random.randint(20000,30000)
				sport = random.randint(7000,9000)
				os.system("virt-install --name {0}fed500snap --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/{4} --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,r,cpu,cport,image))
				c.send("{}".format(sport))
				os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				signal = c.recv(10)
				if signal == '3':
					os.system("virsh destroy {}fed500snap".format(username))	
				oneiaas.iaas(c,username,password)

			elif y.execute("select * from MINT where USERNAME='{}500' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				image = q[0][9]
				r = q[0][3]
				cpu = q[0][4]
				cport = random.randint(20000,30000)
				sport = random.randint(7000,9000)
				os.system("virt-install --name {0}mint500snap --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/{4} --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,r,cpu,cport,image))
				c.send("{}".format(sport))
				os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				signal = c.recv(10)
				if signal == '3':
					os.system("virsh destroy {}mint500snap".format(username))	
				oneiaas.iaas(c,username,password)

		
			elif y.execute("select * from KALI where USERNAME='{}500' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				image = q[0][9]
				r = q[0][3]
				cpu = q[0][4]
				cport = random.randint(20000,30000)
				sport = random.randint(7000,9000)
				os.system("virt-install --name {0}kali500snap --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/{4} --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,r,cpu,cport,image))
				c.send("{}".format(sport))
				os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				signal = c.recv(10)
				if signal == '3':
					os.system("virsh destroy {}kali500snap".format(username))	
				oneiaas.iaas(c,username,password)
	#1024
		
			elif y.execute("select * from REDHAT where USERNAME='{}1024' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				image = q[0][9]
				r = q[0][3]
				cpu = q[0][4]
				cport = random.randint(20000,30000)
				sport = random.randint(7000,9000)
				os.system("virt-install --name {0}rhel1024snap --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/{4} --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,r,cpu,cport,image))
				c.send("{}".format(sport))
				os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				signal = c.recv(10)
				if signal == '3':
					os.system("virsh destroy {}rhel1024snap".format(username))	
				oneiaas.iaas(c,username,password)

	 		
			elif y.execute("select * from UBUNTU where USERNAME='{}1024' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				image = q[0][9]
				r = q[0][3]
				cpu = q[0][4]
				cport = random.randint(20000,30000)
				sport = random.randint(7000,9000)
				os.system("virt-install --name {0}ubun1024snap --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/{4} --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,r,cpu,cport,image))
				c.send("{}".format(sport))
				os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				signal = c.recv(10)
				if signal == '3':
					os.system("virsh destroy {}ubun1024snap".format(username))	
				oneiaas.iaas(c,username,password)


		
			elif y.execute("select * from WINDOWS where USERNAME='{}1024' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				image = q[0][9]
				r = q[0][3]
				cpu = q[0][4]
				cport = random.randint(20000,30000)
				sport = random.randint(7000,9000)
				os.system("virt-install --name {0}win1024snap --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/{4} --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,r,cpu,cport,image))
				c.send("{}".format(sport))
				os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				signal = c.recv(10)
				if signal == '3':
					os.system("virsh destroy {}win1024snap".format(username))	
				oneiaas.iaas(c,username,password)

		
		
			elif y.execute("select * from FEDORA where USERNAME='{}1024' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				image = q[0][9]
				r = q[0][3]
				cpu = q[0][4]
				cport = random.randint(20000,30000)
				sport = random.randint(7000,9000)
				os.system("virt-install --name {0}fed1024snap --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/{4} --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,r,cpu,cport,image))
				c.send("{}".format(sport))
				os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				signal = c.recv(10)
				if signal == '3':
					os.system("virsh destroy {}fed1024snap".format(username))	
				oneiaas.iaas(c,username,password)


		
			elif y.execute("select * from MINT where USERNAME='{}1024' and ID='{}'".format(username,ids)) == 1L:
				q = y.fetchall()
				image = q[0][9]
				r = q[0][3]
				cpu = q[0][4]
				cport = random.randint(20000,30000)
				sport = random.randint(7000,9000)
				os.system("virt-install --name {0}mint1024snap --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/{4} --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,r,cpu,cport,image))
				c.send("{}".format(sport))
				os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				signal = c.recv(10)
				if signal == '3':
					os.system("virsh destroy {}mint1024snap".format(username))	
				oneiaas.iaas(c,username,password)


		
			elif y.execute("select * from KALI where USERNAME='{}1024' and ID='{}'".format(username,ids))== 1L:
				q = y.fetchall()
				image = q[0][9]
				r = q[0][3]
				cpu = q[0][4]
				cport = random.randint(20000,30000)
				sport = random.randint(7000,9000)
				os.system("virt-install --name {0}kali1024snap --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/{4} --vcpus {2} --os-type linux --noautoconsole --vnc --vncport={3} --vnclisten=0.0.0.0".format(username,r,cpu,cport,image))
				c.send("{}".format(sport))
				os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport,cport))
				signal = c.recv(10)
				if signal == '3':
					os.system("virsh destroy {}kali1024snap".format(username))	
				oneiaas.iaas(c,username,password)



#back

	elif choice == '3':
		oneiaas.iaas(c,username,password)

#exit
	elif choice == '4':
		c.close()
	
