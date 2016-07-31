#!/usr/bin/python2

import os,commands,time,useriaas

def oss(c,username,password):
	os.system("dialog --menu 'Available IMAGES to get your OS' 20 30 8 1 'REDHAT 7.2' 2 'UBUNTU'   3 'WINDOWS' 4 'Kali Linux' 5 'Fedora' 6 'MintOS' 7 'BACk' 8 'EXIT' 2>/tmp/image.txt")
	fh = open("/tmp/image.txt")
	choice = fh.read()
	fh.close()

	c.send(choice)
#cancel
	if choice == '':
		useriaas.iaas(c,username,password)
#Redhat
	elif choice == '1':
		os.system("dialog --menu 'Choose flavour' 15 60 4 1 'RAM -> 500Mb  CPU -> 1' 2 'RAM -> 1024Mb  CPU -> 1' 3 'BACK' 4 'Exit' 2>/tmp/in.txt")
		k = open("/tmp/in.txt")
		ram = k.read()
		k.close()
		time.sleep(2)
		c.send(ram)
#cancel 
		if ram == '':
			useriaas.iaas(c,username,password)	
#ram 500
		elif ram == '1':
			signal = c.recv(20)
			if signal == '1':
				os.system("dialog --infobox 'Successfully installed' 10 30")
				time.sleep(1)
				port = c.recv(30)
				os.system("dialog --msgbox 'Connect through this port {}' 10 30".format(port))
			elif signal == '0':
				os.system("dialog --infobox 'Alredy installed' 10 30")
				time.sleep(1)
				port = c.recv(30)
				os.system("dialog --msgbox 'Connect through this port {}' 10 30".format(port))
	
#ram 1024
		elif ram == '2':
			signal = c.recv(20)
			if signal == '1':
				os.system("dialog --infobox 'Successfully installed' 10 30")
				time.sleep(1)
				port = c.recv(30)
				os.system("dialog --msgbox 'Connect through this port {}' 10 30".format(port))
			elif signal == '0':
				os.system("dialog --infobox 'Alredy installed' 10 30")
				time.sleep(1)
				port = c.recv(30)
				os.system("dialog --msgbox 'Connect through this port {}' 10 30".format(port))
	

#back
		elif ram == '3':
			useriaas.iaas(c,username,password)
#exit
		elif ram == '4':
			os.system("dialog --infobox 'Bye Have a nice day' 10 30")


		"""

		if v == 'n':
			#receiving port where to connect
			port = c.recv(50)
			#recieving successful signal
			signal = c.recv(20)
		
			if signal == '1':
				os.system("dialog --infobox 'Port no is {}' 10 30 ".format(port))
				commands.getstatusoutput("firefox 'http://192.168.122.1/vnc/?ip=192.168.122.1&port={}'".format(port))
		else:
			os.system("dialog --radiolist 'Run your redhat os' 6 60 1 1 'rhel7'  on 2>/tmp/ii.txt")
			k = open("/tmp/ii.txt")
			sw = k.read()
			k.close()
			#sending signal that user clicked
			c.send(sw)

			if sw == '1':
				port= c.recv(30)
				ui =  c.recv(30)					
				if ui == '1':
					os.system("dialog --infobox 'Port no is {}' 10 30 ".format(port))
					commands.getstatusoutput("firefox http://192.168.122.1/vnc/?ip=192.168.122.1&port={}".format(port))




	elif image == '2':
		
		#receiving port where to connect
		port = c.recv(50)
		#recieving successful signal
		signal = c.recv(20)
		
		if signal == '1':
			os.system("dialog --infobox 'Port no is {}' 10 30 ".format(port))
			commands.getstatusoutput("firefox http://192.168.122.1/vnc/?ip=192.168.122.1&port={}".format(port))
		
		
		v = c.recv(10)
		if v == 'n':
			#receiving port where to connect
			port = c.recv(50)
			#recieving successful signal
			signal = c.recv(20)
		
			if signal == '1':
				os.system("dialog --infobox 'Port no is {}' 10 30 ".format(port))
				commands.getstatusoutput("firefox http://192.168.122.1/vnc/?ip=192.168.122.1&port={}".format(port))
		else:
			os.system("dialog --radiolist 'Run It' 6 60 1 1 'ubuntu'  on 2>/tmp/ii.txt")
			k = open("/tmp/ii.txt")
			sw = k.read()
			k.close()
			#sending signal that user clicked
			c.send(sw)

			if sw == '1':
				port= c.recv(30)
				ui =  c.recv(30)					
				if ui == '1':
					os.system("dialog --infobox 'Port no is {}' 10 30 ".format(port))
					commands.getstatusoutput("firefox http://192.168.122.1/vnc/?ip=192.168.122.1&port={}".format(port))








	elif image == '3':
		v = c.recv(10)
		if v == 'n':
			#receiving port where to connect
			port = c.recv(50)
			#recieving successful signal
			signal = c.recv(20)
		
			if signal == '1':
				os.system("dialog --infobox 'Port no is {}' 10 30 ".format(port))
				commands.getstatusoutput("firefox http://192.168.122.1/vnc/?ip=192.168.122.1&port={}".format(port))
		else:
			os.system("dialog --radiolist 'Run It' 6 60 1 1 rhel7  on 2>/tmp/ii.txt")
			k = open("/tmp/ii.txt")
			sw = k.read()
			k.close()
			#sending signal that user clicked
			c.send(sw)

			if sw == '1':
				port= c.recv(30)
				ui =  c.recv(30)					
				if ui == '1':
					os.system("dialog --infobox 'Port no is {}' 10 30 ".format(port))
					commands.getstatusoutput("firefox http://192.168.122.1/vnc/?ip=192.168.122.1&port={}".format(port))

		"""

