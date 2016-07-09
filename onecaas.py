#!/usr/bin/python2

import os,commands

def caas(c,username,password):
	choice = c.recv(30)
#centos

	if choice == '':
		c.close()

	elif choice == '1':
		#mounting this to docker
		fh = open("/root/Desktop/folderServer/v.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("os.system('useradd {}')\n".format(username))
		fh.write("os.system('echo {} | passwd {} --stdin')\n".format(password,username))
		fh.close()
		os.system("chmod +x /root/Desktop/folderServer/v.py")

		"""
		#receiving no.of dockers
		no = c.recv(30)
		n = int(no)
		l = []
		#running docker in loop
		for i in range(n):
			y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dock bash")
			os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
			os.system("docker exec {} service sshd restart".format(y[1]))
			ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))
			l.extend(ip)
		#sending ips to client to connect through docker

		for i in range(n):
			print ip[1]
			c.send(ip[1])
		"""

		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dock bash")
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

		os.system("chmod +x /root/Desktop/folderServer/v.py")
		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dock bash")
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

		os.system("chmod +x /root/Desktop/folderServer/v.py")
		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dock bash")
		os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
		os.system("docker exec {} service sshd restart".format(y[1]))
		ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))
		#sending ip to client to connect through docker
		c.send(ip[1])
