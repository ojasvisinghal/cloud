#!/usr/bin/python2

import os,commands,time

def paas(c,username,password):
	choice = c.recv(30)
	#python

	if choice == '':
		c.close()


	elif choice == '1':
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
		fh.write("os.system('useradd -s /usr/bin/perl {}')\n".format(username))
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



