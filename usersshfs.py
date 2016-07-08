#!/usr/bin/python2

import os,commands,time

def sshfs(c,username,password):
	os.system("dialog --inputbox 'Enter harddisk size' 20 60 2>/tmp/size.txt")
        g = open("/tmp/size.txt")
        size = g.read()
        g.close()

        # sending size to server

        c.send(size)

        #getting signal that server side processing is done
        signal = c.recv(20)
        # client side processing started
        if signal == '1':
		y = commands.getstatusoutput("rpm -q fuse-sshfs")
		if y[0]!=0:	
			os.system("yum install fuse-sshfs")
		os.system("mkdir /root/Desktop/{}".format(username))
		os.system("sshfs {0}@192.168.122.1:/home/sshfs/{0} /root/Desktop/{0}".format(username))	
		os.system("dialog --infobox 'DONE !!check your Desktop to get access' 10 30")
	else:
		os.system("dialog --infobox 'Error Occured!!!! ' 20 30 ")



