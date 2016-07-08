#!/usr/bin/python2

import os,commands,time

def samba(c,username,password):
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
                y = commands.getstatusoutput("rpm -q cifs-utils samba-client")
                if y[0]!=0:
                        os.system("yum install cifs-utils samba-client -y")
		os.system("mkdir /root/Desktop/{}".format(username))
		os.system("mount -o username={0}smb //192.168.122.1/{0} /root/Desktop/{0}".format(username))
		os.system("dialog --infobox 'DONE !! ;) Hehe' 10 30")


	else:
                os.system("dialog --infobox 'Error Occured!!!! ' 20 30 ")


