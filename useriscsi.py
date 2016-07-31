#!/usr/bin/python2

import os,commands,time,userstaas

def iscsi(c,username,password):
	os.system("dialog --menu 'Choose' 15 65 2 1 'ADD disk from here' 2 'Take SNAPSHOT' 2>/tmp/aas.txt")
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
			y = commands.getstatusoutput("rpm -q iscsi-initiator-utils")
			if y[0]!=0:	
				os.system("yum install iscsi-initiator-utils -y")
			os.system("iscsiadm --mode discoverydb --type sendtargets --portal 192.168.122.1 --discover")
			os.system("iscsiadm --mode node --targetname {0} --portal 192.168.122.1:3260 --login".format(username))	
			os.system("dialog --infobox 'DONE !!check your Desktop to get access' 10 30")
		else:
			os.system("dialog --infobox 'Error Occured!!!! ' 20 30 ")

		
#snapshot 
	elif s == '2':
		snap = c.recv(30)
		os.system("dialog --infobox 'snap taken successfully !!' 10 30")
	

#back
	elif s == '3':
		userstaas.staas(c,username,password)

#exit
	elif s == '4':
		os.system("dialog --infobox 'Logout successfully' 10 30")






