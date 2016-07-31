#!/usr/bin/python2

import os,commands,onemenu,time

def caas(c,username,password):
	choice = c.recv(30)
#centos

	if choice == '':
		onemenu.menu(c,username,password)

	elif choice == '1':
		#mounting this to docker
		fh = open("/root/Desktop/folderServer/v.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("os.system('useradd {}')\n".format(username))
		fh.write("os.system('echo {} | passwd {} --stdin')\n".format(password,username))
		fh.close()

		n = c.recv(30)
		u = int(n)
		i = 0
		while i < u:
			y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dockall/caas:v1 bash")
			os.system("chmod +x /root/Desktop/folderServer/v.py")
			os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
			os.system("docker exec {} service sshd restart".format(y[1]))
			ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))
			print "{}".format(ip[1])
			fh = open("/root/Desktop/folderServer/shell.py",'w')
			fh.write("USER=shellinabox\n")
			fh.write("GROUP=shellinabox\n")
			fh.write("CERTDIR=/var/lib/shellinabox\n")
			fh.write("PORT=4200\n")
			fh.write("OPTS=\"-t -s /:SSH:{}\"".format(ip[1]))
			fh.close()	

			os.system("chmod +x /root/Desktop/folderServer/shell.py")
			os.system("docker exec {} cp /media/folderServer/shell.py /etc/sysconfig/shellinaboxd".format(y[1]))
			os.system("docker exec {} service shellinaboxd restart")


			#sending ip to client to connect through docker
			time.sleep(2)
			c.send(ip[1])
			i = i + 1
		onemenu.menu(c,username,password)

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

		os.system("chmod +x /root/Desktop/folderServer/v.py")
		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dock bash")
		os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
		os.system("docker exec {} service sshd restart".format(y[1]))
		ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))
		#sending ip to client to connect through docker
		c.send(ip[1])
		onemenu.menu(c,username,password)


#mint
	elif choice == '3':
		#mounting this to docker
		fh = open("/root/Desktop/folderServer/v.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("os.system('useradd {}')\n".format(username))
		fh.write("os.system('echo {} | passwd {} --stdin')\n".format(password,username))
		fh.close()

		os.system("chmod +x /root/Desktop/folderServer/v.py")
		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dock bash")
		os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
		os.system("docker exec {} service sshd restart".format(y[1]))
		ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))
		#sending ip to client to connect through docker
		c.send(ip[1])
		onemenu.menu(c,username,password)

#fedora
	elif choice == '4':
		#mounting this to docker
		fh = open("/root/Desktop/folderServer/v.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("os.system('useradd {}')\n".format(username))
		fh.write("os.system('echo {} | passwd {} --stdin')\n".format(password,username))
		fh.close()

		os.system("chmod +x /root/Desktop/folderServer/v.py")
		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dock bash")
		os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
		os.system("docker exec {} service sshd restart".format(y[1]))
		ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))
		#sending ip to client to connect through docker
		c.send(ip[1])
		onemenu.menu(c,username,password)

#redhat
	elif choice == '5':
		#mounting this to docker
		fh = open("/root/Desktop/folderServer/v.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("os.system('useradd {}')\n".format(username))
		fh.write("os.system('echo {} | passwd {} --stdin')\n".format(password,username))
		fh.close()

		os.system("chmod +x /root/Desktop/folderServer/v.py")
		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dock bash")
		os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
		os.system("docker exec {} service sshd restart".format(y[1]))
		ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))
		#sending ip to client to connect through docker
		c.send(ip[1])
		onemenu.menu(c,username,password)

#kali
	elif choice == '6':
		#mounting this to docker
		fh = open("/root/Desktop/folderServer/v.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("os.system('useradd {}')\n".format(username))
		fh.write("os.system('echo {} | passwd {} --stdin')\n".format(password,username))
		fh.close()

		os.system("chmod +x /root/Desktop/folderServer/v.py")
		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dock bash")
		os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
		os.system("docker exec {} service sshd restart".format(y[1]))
		ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))
		#sending ip to client to connect through docker
		c.send(ip[1])
		onemenu.menu(c,username,password)

#back
	elif choice == '7':
		onemenu.menu(c,username,password)
	
#exit
	elif choice == '8':
		c.close()
