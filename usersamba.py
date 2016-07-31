#!/usr/bin/python2

import os,commands,time,userstaas

def samba(c,username,password):
	os.system("dialog --menu 'Choose' 15 65 5 1 'ADD disk here' 2 'EXTEND your disk' 3 'Take SNAPSHOT here' 4 'back' 5 'Exit' 2>/tmp/aas.txt")
	gh = open("/tmp/aas.txt")
        s = gh.read()
        gh.close()
	c.send(s)


#cancel
	if s == '':
		userstaas.staas(c,username,password)
#add
	elif s == '1':
		os.system("dialog --inputbox 'Enter harddisk size' 20 60 2>/tmp/size.txt")
		g = open("/tmp/size.txt")
		size = g.read()
		g.close()
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
			os.system("dialog --infobox 'DONE !!check your Desktop to get access' 10 30")
		else:
			os.system("dialog --infobox 'Error Occured!!!! ' 20 30 ")

		
#extend 
	elif s == '2':
		os.system("dialog --inputbox 'Enter harddisk size' 20 60 2>/tmp/size.txt")
		g = open("/tmp/size.txt")
		size = g.read()
		g.close()
		c.send(size)

		sure = c.recv(40)
		if sure == '1':
			os.system("dialog --infobox 'enjoy !!' 10 30")
		else:
			os.system("dialog --infobox 'No derive yet !!' 10 30")

#snapshot
	elif s == '3':
		snap = c.recv(30)
		os.system("dialog --infobox 'snap taken successfully !!' 10 30")
	

#back
	elif s == '4':
		userstaas.staas(c,username,password)

#exit
	elif s == '5':
		os.system("dialog --infobox 'bbye have a nice day' 10 30")


	"""
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

	"""
