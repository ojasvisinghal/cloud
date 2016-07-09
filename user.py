#!/usr/bin/python2
import os,commands,time,usernfs,usersshfs,usersamba,useriscsi,userextend,usergallery,usersnap,useros,usercaas,userpaas,usersaas,usermenu,userqren



def staas(c,username,password):
	os.system("dialog --radiolist 'Choose your Storage' 15 60 3 1 'Object storage' on 2 'Block storage' off 3 'EXIT' off 2>/tmp/b.txt")


	fh = open("/tmp/b.txt")
	choice = fh.read()
	fh.close()

	#sending choice to server to start requested storage
	c.send(choice)	


	if choice == '':
		usermenu.menu(c,username,password)


#object
	elif choice == '1':
		os.system("dialog --radiolist 'Storage Services' 20 60 4 1 'NFS' on 2 'SSHFS' off 3 'SAMBA' off 4 'MOUNT SNAPSHOT' off 2>/tmp/cd.txt")
		gh = open("/tmp/cd.txt")
		dat = gh.read()
		gh.close()

		# sending which type of server user want
		c.send(dat)

		if dat == '':
			pass
#nfs	
		if dat == '1':
			usernfs.nfs(c,username,password)			
#sshfs server
		elif dat == '2':
			usersshfs.sshfs(c,username,password)
#samba server
		elif dat == '3':
			usersamba.samba(c,username,password)
#mount snapshot
		elif dat == '4':
			usersnap.snap(c,username,password)
		

		"""
#extend code

		elif dat == '4':
                        userextend.extend(c,username,password)

		#staas(c,username,password)
		"""
#block storage
	elif choice == '2':
		useriscsi.iscsi(c,username,password)

		"""
		os.system("dialog --radiolist 'choose among these' 15 60 2 1 'ISCSI' on 2 'SNAPSHOT' off 2>/tmp/block.txt")

		fd = open("/tmp/block.txt")
       		dat = fd.read()
        	fd.close()
#sending which type of service user want
		c.send(dat)



#iscsi
		if dat == '1':
			

			k = open("/tmp/size.txt")
                        size = k.read()
                        k.close()

                        # sending size to server

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
				os.system("dialog --infobox 'ALL DONE !! Check your Desktop' 10 30")	
			else:
				os.system("dialog --infobx 'Error Occured @@@@@@@@@@' 10 60")
#snapshot
		elif dat == '2':
			os.system("mkdir /root/Desktop/{}snap".format(username))
			os.system("mount 192.168.122.1:/media/{0}snap /root/Desktop/{0}snap".format(username))

		"""

######## EXIT ###############################


#exit option

	elif choice == '3':
		os.system("BBye !! We will miss you .......")
	
#staas completed



###############################################  IAAS  ####################################################



def iaas(c,username,password):
	os.system("dialog --radiolist 'OSREMOTE TOOL' 20 30 3 1 'OS GALLERY' on 2 'INSTALL OS' off  3 'OS using Qrencode' off 4 'OS list' off 5 'OS migrate' off  2>/tmp/qq.txt")
	f = open("/tmp/qq.txt")
        choice = f.read()
        f.close()

	#sending choice 
	c.send(choice)

	if choice == '':
		os.system("dialog --infobox 'bye have a nice day !!!' 6 40 ")

#os gallery
	if choice == '1':
		usergallery.gallery(c,username,password)
	
#install os
	if choice == '2':		
		useros.oss(c,username,password)

#os with qrencode
	if choice == '3':
		userqren.qr(c,username,password)
"""
#os system  list
	if choice == '4':
		userlist.listt(c,username,password)

#os migrate
	if choice == '5':
		usermigrate.migrate(c,username,password)

"""
#iaas completed


def paas(c,username,password):
	userpaas.paas(c,username,password)
	
#paas completed

def caas(c,username,password):
	usercaas.caas(c,username,password)

#caas done

def saas(c,username,password):
	usersaas.saas(c,username,password)

#saas completed

 
