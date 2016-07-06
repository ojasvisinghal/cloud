import os,commands

def staas(c,username,password):
	os.system("dialog --radiolist 'choose' 20 40 3 1 'Object storage' on 2 'Block storage' off 3 'BACK' off 2>/tmp/b.txt")
	fh = open("/tmp/b.txt")
	choice = fh.read()
	fh.close()
	#sending choice to server to start requested storage
	c.send(choice)		
	if choice == '1':
		os.system("dialog --radiolist 'choose' 20 60 5 1 'NFS' on 2 'SSHFS' off 3 'SAMBA' off 4 'EXTEND' off  5 'REMOVE' off 2>/tmp/cd.txt")
		gh = open("/tmp/cd.txt")
		dat = gh.read()
		gh.close()
		# sending which type of server user want
		c.send(dat)
		"""
		#what you want
		os.system("dialog --radiolist '@@@@ WHAT YOU WANT @@@@' 40 70 3 1 'ADD' on  2 'EXTEND' off 3 'REMOVE' off 2>/tmp/add.txt")
		q = open("/tmp/add.txt")
		add = q.read()
		q.close()
		#sending what user want
		c.send(add)
		"""
#nfs
		if dat == '1':
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
				os.system("mkdir /root/Desktop/{}".format(username))
				os.system("mount 192.168.122.1:/home/{0}/{0} /root/Desktop/{0}".format(username))
				#doing entry to file after adding a partition using file handling
				#os.system("echo '/home/{0}/nfs' >>/media/{0}.txt".format(username))
				fi = open('/media/hdd.txt','w+')
				fi.write("/home/{0}/{0}".format(username))
				fi.close()
			# done
				#c.send("2")
				os.system("dialog --infobox 'All Done enjoy!!!' 10 50")
			else:
				os.system("dialog --infobox 'some error occured'10 80")
#sshfs server
		elif dat == '2':
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
				os.system("sshfs {0}@192.168.122.1:/home/{0}/{0} /root/Desktop/{0}".format(username))	
				os.system("dialog --infobox 'DONE !!check your Desktop to get access' 10 30")
			else:
				os.system("dialog --infobox 'Error Occured!!!! ' 20 30 ")

#samba server
		elif dat == '3':
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
				os.system("mount -o username={0} //192.168.122.1/{0} /root/Desktop/{0}".format(username))
				os.system("dialog --infobox 'DONE !! ;) Hehe' 10 30")


			else:
                                os.system("dialog --infobox 'Error Occured!!!! ' 20 30 ")
	

#extend code
		elif dat == '4':
                        # checking database whether any drive exist with username
                        # writing all existing lvs in a file
			os.system("dialog --inputbox 'Enter name of hardisk' 30 40 2>/tmp/ex.txt")
			gh = open("/tmp/size.txt")
			name = gh.read()
			gh.close()
			#sending name of HDD to server
			c.send(name)
				#recieving signal from server
			signals = c.recv(30)
			if signals == '1':
			#os.system("dialog --radiolist 'choose your derive' 30 70 ")
	                	os.system("dialog --inputbox 'Enter size to Extend' 20 60 2>/tmp/size.txt")
	                	g = open("/tmp/size.txt")
	                	size = g.read()
	                	g.close()

		                # sending size to server
	                	c.send(size)

		                #getting signal that server side processing is done
	                	signal = c.recv(20)
		                # client side processing started
	                	if signal == '1':
		                # done
	                        	os.system("dialog --infobox 'All Done enjoy!!!' 10 50")
	                	else:
	                        	os.system("dialog --infobox 'some error occured'10 80")
			else:
				os.system("dialog --infobox 'EROOR @@@@@@@@@@@@@@' 10 60")

	
#remove code
		elif dat == '5':
			print 'jeeooko'



		else:
			print 'xzzz'

#block storage
	elif choice == '2':
		os.system("dialog --radiolist 'choose among these' 40 60 2 1 'ISCSI' on 2 'SNAPSHOT' off 2>/tmp/block.txt")

		fd = open("/tmp/block.txt")
       		dat = fd.read()
        	fd.close()
#sending which type of service user want
		c.send(dat)
#iscsi
		if dat == '1':
			os.system("dialog --inputbox 'Enter harddisk size' 20 60 2>/tmp/size.txt")
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
				os.system("yum install iscsi-initiator-utils")
				os.system("iscsiadm --mode discoverydb --type sendtargets --portal 192.168.122.1 --discover")
				os.system("iscsiadm --mode node --targetname {} --portal 192.168.122.1:3260 --login".format(username))
				os.system("dialog --infobox 'ALL DONE !! Check your Desktop' 10 30")	
			else:
				os.system("dialog --infobx 'Error Occured @@@@@@@@@@' 10 60")
#snapshot
		elif dat == '2':
			os.system("mkdir /root/Desktop/{}snap".format(username))
			os.system("mount 192.168.122.1:/media/{0}snap /root/Desktop/{0}snap".format(username))

#back option

	elif choice == '3':
		pass
	
	else:
		pass
	
#staas completed

def iaas(c,username,password):
	os.system("dialog --radiolist 'what you want to see' 20 30 2 1 'gallery' on 2 'install' off 2>/tmp/qq.txt")
	f = open("/tmp/qq.txt")
        choice = f.read()
        f.close()

	#sending choice 
	c.send(choice)

	if choice == '1':
		sig =c.recv(30)
		if sig == '0':
			os.system("dialog --infobox 'no os yet' 10 30")

		else:
			p = c.recv(30) #recieving 1
			p1 = c.recv(20)
			p2 = c.recv(20)
			p3 = c.recv(20)

			if p1 == '0':
				port1 = c.recv(30)	
				os.system("dialog --infobox 'Port no is {}' 10 30 ".format(port1))
				os.system("firefox 192.168.122.1/vnc/vnc.html")
				
			if p2 == '0':
				port2 = c.recv(30)	
				os.system("dialog --infobox 'Port no is {}' 10 30 ".format(port2))
				os.system("firefox 192.168.122.1/vnc/vnc.html")
				

			if p3 == '0':
				port3 = c.recv(30)	
				os.system("dialog --infobox 'Port no is {}' 10 30 ".format(port3))
				os.system("firefox 192.168.122.1/vnc/vnc.html")
				


	if choice == '2':		

		os.system("dialog --radiolist 'choose your image' 20 30 3 1 'UBUNTU' on 2 'REDHAT 7.2' off  3 'WINDOWS' off 2>/tmp/image.txt")
		fh = open("/tmp/image.txt")
		image = fh.read()
		fh.close()

		#send signal
		c.send(image)

		os.system("dialog --inputbox 'enter ram' 4 60 2>/tmp/ram.txt")
		os.system("dialog --inputbox 'enter cpu' 4 60 2>/tmp/cpu.txt")
		os.system("dialog --inputbox 'enter harddisk' 4 60 2>/tmp/hd.txt")
		a=open("/tmp/ram.txt")
		ram = a.read()
		a.close()

		a=open("/tmp/cpu.txt")
	        cpu = a.read()
	        a.close()

		a=open("/tmp/hd.txt")
	        hd = a.read()
	        a.close()
	
		#sending all three values to server
		c.send(ram)
		c.send(cpu)
		c.send(hd)
		if image == '1':
			#receiving port where to connect
			port = c.recv(50)
			#recieving successful signal
			signal = c.recv(20)
			
			if signal == '1':
				os.system("dialog --infobox 'Port no is {}' 10 30 ".format(port))
				commands.getstatusoutput("firefox 192.168.122.1/vnc/vnc.html")
			

		elif image == '2':
			#receiving port where to connect
			port = c.recv(50)
			#recieving successful signal
			signal = c.recv(20)
			
			if signal == '1':
				os.system("dialog --infobox 'Port no is {}' 10 30 ".format(port))
				commands.getstatusoutput("firefox 192.168.122.1/vnc/vnc.html")
			
		elif image == '3':
			#receiving port where to connect
			port = c.recv(50)
			#recieving successful signal
			signal = c.recv(20)
			
			if signal == '1':
				os.system("dialog --infobox 'Port no is {}' 10 30 ".format(port))
				commands.getstatusoutput("firefox 192.168.122.1/vnc/vnc.html")
			


#iaas completed

def paas(c,username,password):
	os.system("dialog --radiolist 'choose your platform' 30 80 3 1 'PYTHON' on 2 'EDITOR' off 3 'PHP' off 2>/tmp/sas.txt")
        o = open("/tmp/sas.txt")
	choice = o.read()
        o.close()
	
	#running dkr
	c.send(choice)
	if choice == '1':
		#recieving ip of docker
		ip = c.recv(30)
		os.system("route add -net 172.17.0.0/16 gw 192.168.122.1")
		os.system("ssh {}@{}".format(username,ip))
			
	elif choice == '2':
		 #recieving ip of docker
                ip = c.recv(30)
                os.system("route add -net 172.17.0.0/16 gw 192.168.122.1")
                os.system("ssh {}@{}".format(username,ip))
                        
	elif choice == '3':
		 #recieving ip of docker
                ip = c.recv(30)
                os.system("route add -net 172.17.0.0/16 gw 192.168.122.1")
                os.system("ssh {}@{}".format(username,ip))
                        


	
#paas completed


def caas(c,username,password):
	os.system("dialog --radiolist 'choose your container' 30 80 3 1 'Centos' on 2 'Ubuntu' off 3 'Mint' off 2>/tmp/sas.txt")
        o = open("/tmp/sas.txt")
	choice = o.read()
        o.close()
	
	#running dkr
	c.send(choice)
	if choice == '1':
		#recieving ip of docker
		ip = c.recv(30)
		os.system("ssh {}@{}".format(username,ip))
			
	elif choice == '2':
		#recieving ip of docker
		ip = c.recv(30)
		os.system("ssh {}@{}".format(username,ip))
			
	
	elif choice == '3':
		#recieving ip of docker
		ip = c.recv(30)
		os.system("ssh {}@{}".format(username,ip))
				





def saas(c,username,password):
	os.system("dialog --radiolist 'choose your software' 30 80 3 1 'FIREFOX' on 2 'GEDIT' off 3 'VLC' off 2>/tmp/sas.txt")
	o = open("/tmp/sas.txt")
	choice = o.read()
	o.close()

	#sending choice to server to get permission
	c.send(choice)
	if choice == '1':
		"""
		os.system("dialog --inputbox 'Enter firefox accounts password' 20 80 2>/tmp/pswd.txt")
		d = open("/tmp/pswd.txt")
		pswd = d.read()
		d.close()
		"""
		#setting signal to server to set password and create account for this user
		data = c.recv(30)
		if data == '1':
		#sending password to server
		#c.send(pswd)
			os.system("ssh -X {}fire@192.168.122.4".format(username))
			os.system("##################")
		else:
			os.system("###$$$$$$$ ERROR  FIREFOX $$$$########")
		

#gedit
	elif choice == '2':
		  #setting signal to server to set password and create account for this user
                data = c.recv(30)
                if data == 1:
                #sending password to server
                #c.send(pswd)
                        os.system("ssh -X {}gedit@192.168.122.4".format(username))
                else:
                        os.system("###$$$$$$$ ERROR  GEDIT $$$$########")

		
#vlc
	elif choice == '3':
		 #setting signal to server to set password and create account for this user
                data = c.recv(30)
                if data == 1:
                #sending password to server
                #c.send(pswd)
                        os.system("sshpass -p {} ssh -X {}@192.168.122.4".format(password,username))
                else:
                        os.system("###$$$$$$$ ERROR VLC $$$$########")

#saas completed
