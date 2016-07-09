#!/usr/bin/python2

import os,commands,user,MySQLdb,random,fileSend,onemenu,onenfs,onesshfs,onesamba,onesnap,oneextend,oneiscsi,onegallery,oneinstall,onesaas,onecaas,qrenco,onepaas

x=MySQLdb.connect("localhost")
y=x.cursor()

def staas(c,username,password):
	#recieving choice from client which service to start
	choice = c.recv(30)

	if choice == '':
		stass(c,username,password)

	elif choice == '1':
		#recieving which service user wants
		data = c.recv(30)
		#recieveing whether to extend add or remove
		#add = c.recv(30)
#nfs server
		if data == '1':
			onenfs.nfs(c,username,password)

#sshfs server
		elif data == '2':
			onesshfs.sshfs(c,username,password)

#samba server
		elif data == '3':
			onesamba.samba(c,username,password)


#mount snap
		elif data == '4':
			onesnap.snap(c,username,password)








		"""
#extend
		elif data == '4':
			oneextend.extend(c,username,password)
		"""
		"""
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
			"""


#block storage

	elif choice == '2':
		#recieving which service user wants
                data = c.recv(30)
#iscsi
		if data == '1':
			oneiscsi.iscsi(c,username,password)

		"""
#snapshot
		elif data == '2':
			import MySQLdb
			os.system("systemctl restart mariadb")
			x=MySQLdb.connect("localhost")
			y=x.cursor()
			y.execute("use cloud;")
			e = y.execute("select ISCSI from USER where USERNAME='{0}';".format(username))
			q = y.fetchall()
			if e == 1L and q[0][0]!= None:
				os.system("lvcreate --name {0}snap --size 2M -s {1}".format(username,q[0][0]))
				commands.getstatusoutput("mkdir /media/{0}snap".format(username))
				os.system("mount /dev/userVG/{0}snap /media/{0}snap".format(username))
				os.system("chown {0} /media/{0}snap".format(username))
				os.system("chmod 700 /media/{0}snap".format(username))
			
		                os.system("echo '/media/{0}snap *(rw,no_root_squash)' >>/etc/exports".format(username))
		                os.system("systemctl restart nfs-server")
		                os.system("systemctl enable nfs-server")
#sending signal to client to start his processing

				c.send("1")
			else:
				os.system("dialog --infobox 'error' 10 30")
			"""
# back option
	elif choice == '3':
		pass


###########################################      IAAS   ###################################################################

def iaas(c,username,password):
	#recieving choice
	choice = c.recv(30)


	if choice == '':
		c.close()
#gallery
	elif choice == '1':
		onegallery.gallery(c,username,password)
	
#install
	elif choice == '2':
		oneinstall.install(c,username,password)



	elif choice == '3':
		#qrencode collection
		qrenco.qren(c,username,password)












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

def paas(c,username,password):
	onepaas.paas(c,username,password)



def saas(c,username,password):
	onesaas.saas(c,username,password)


def caas(c,username,password):
	onecaas.caas(c,username,password)
#caas completed
