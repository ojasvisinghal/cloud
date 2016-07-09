#!/usr/bin/python2

import os,commands,time

def oss(c,username,password):
		os.system("dialog --radiolist 'ISO IMAGES' 20 30 3 1 'REDHAT 7.2' on 2 'UBUNTU' off  3 'WINDOWS' off 2>/tmp/image.txt")
		fh = open("/tmp/image.txt")
		image = fh.read()
		fh.close()

		#send signal
		c.send(image)

		os.system("dialog --inputbox 'enter ram' 7 30 2>/tmp/ram.txt")
		os.system("dialog --inputbox 'enter cpu' 7 30 2>/tmp/cpu.txt")
		os.system("dialog --inputbox 'enter harddisk' 7 30 2>/tmp/hd.txt")
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
		#c.send(hd)
		if image == '1':
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
				os.system("dialog --radiolist 'Run It' 6 60 1 1 'rhel7'  on 2>/tmp/ii.txt")
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
			"""
			#receiving port where to connect
			port = c.recv(50)
			#recieving successful signal
			signal = c.recv(20)
			
			if signal == '1':
				os.system("dialog --infobox 'Port no is {}' 10 30 ".format(port))
				commands.getstatusoutput("firefox http://192.168.122.1/vnc/?ip=192.168.122.1&port={}".format(port))
			
			"""
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



