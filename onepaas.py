#!/usr/bin/python2

import os,commands,time,onemenu

def paas(c,username,password):
	choice = c.recv(30)
	#cancel

	if choice == '':
		onemenu.menu(c,username,password)

	#python
	elif choice == '1':
		#mounting this to docker
		fh = open("/root/Desktop/folderServer/v.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("os.system('useradd -s /usr/bin/python {}')\n".format(username))
		fh.write("os.system('echo {} | passwd {} --stdin')\n".format(password,username))
		fh.close()

		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dockall/caas:v1 bash")
		os.system("chmod +x /root/Desktop/folderServer/v.py")
		os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
		os.system("docker exec {} service sshd restart".format(y[1]))
		ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))

		fh = open("/root/Desktop/folderServer/shell.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("USER=shellinabox\n")
		fh.write("GROUP=shellinabox\n")
		fh.write("CERTDIR=/var/lib/shellinabox\n")
		fh.write("PORT=4200\n")
		fh.write("OPTS='-t -s /:SSH:{}'".format(ip[1]))
		fh.close()	

		os.system("chmod +x /root/Desktop/folderServer/shell.py")
		os.system("docker exec {} cp /media/folderServer/shell.py /etc/sysconfig/shellinaboxd".format(y[1]))
		os.system("docker exec {} service shellinaboxd restart")


		#sending ip to client to connect through docker
		c.send(ip[1])
		onemenu.menu(c,username,password)

	#perl
	elif choice == '2':
		#mounting this to docker
		fh = open("/root/Desktop/folderServer/v.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("os.system('useradd -s /usr/bin/perl {}')\n".format(username))
		fh.write("os.system('echo {} | passwd {} --stdin')\n".format(password,username))
		fh.close()

		
		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dockall/caas:v1 bash")
		os.system("chmod +x /root/Desktop/folderServer/v.py")
		os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
		os.system("docker exec {} service sshd restart".format(y[1]))
		ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))

		fh = open("/root/Desktop/folderServer/shell.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("USER=shellinabox\n")
		fh.write("GROUP=shellinabox\n")
		fh.write("CERTDIR=/var/lib/shellinabox\n")
		fh.write("PORT=4200\n")
		fh.write("OPTS='-t -s /:SSH:{}'".format(ip[1]))
		fh.close()	

		os.system("chmod +x /root/Desktop/folderServer/shell.py")
		os.system("docker exec {} cp /media/folderServer/shell.py /etc/sysconfig/shellinaboxd".format(y[1]))
		os.system("docker exec {} service shellinaboxd restart")

		#sending ip to client to connect through docker
		c.send(ip[1])
		onemenu.menu(c,username,password)


	#ruby
	elif choice == '3':
		#mounting this to docker
		
		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dockall/caas:v1 bash")
		os.system("chmod +x /root/Desktop/folderServer/v.py")
		os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
		os.system("docker exec {} service sshd restart".format(y[1]))
		ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))

		fh = open("/root/Desktop/folderServer/shell.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("USER=shellinabox\n")
		fh.write("GROUP=shellinabox\n")
		fh.write("CERTDIR=/var/lib/shellinabox\n")
		fh.write("PORT=4200\n")
		fh.write("OPTS='-t -s /:SSH:{}'".format(ip[1]))
		fh.close()	

		os.system("chmod +x /root/Desktop/folderServer/shell.py")
		os.system("docker exec {} cp /media/folderServer/shell.py /etc/sysconfig/shellinaboxd".format(y[1]))
		os.system("docker exec {} service shellinaboxd restart")

		#sending ip to client to connect through docker
		c.send(ip[1])
		onemenu.menu(c,username,password)

	#mysql
	elif choice == '4':
		#mounting this to docker
		
		y = commands.getstatusoutput("docker run -itd --privileged  -v /root/Desktop/:/media/ dockall/caas:v1 bash")
		os.system("chmod +x /root/Desktop/folderServer/v.py")
		os.system("docker exec {} /media/folderServer/v.py".format(y[1]))
		os.system("docker exec {} service sshd restart".format(y[1]))
		ip = commands.getstatusoutput("docker exec {} hostname -i".format(y[1]))

		fh = open("/root/Desktop/folderServer/shell.py",'w')
		fh.write("#!/usr/bin/python2\n")
		fh.write("import os\n")
		fh.write("USER=shellinabox\n")
		fh.write("GROUP=shellinabox\n")
		fh.write("CERTDIR=/var/lib/shellinabox\n")
		fh.write("PORT=4200\n")
		fh.write("OPTS='-t -s /:SSH:{}'".format(ip[1]))
		fh.close()	

		os.system("chmod +x /root/Desktop/folderServer/shell.py")
		os.system("docker exec {} cp /media/folderServer/shell.py /etc/sysconfig/shellinaboxd".format(y[1]))
		os.system("docker exec {} service shellinaboxd restart")

		#sending ip to client to connect through docker
		c.send(ip[1])
		onemenu.menu(c,username,password)

	#back
	elif choice == '5':
		onemenu.menu(c,username,password)
	
	#exit
	elif choice == '6':
		c.close()






