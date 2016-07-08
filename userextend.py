#!/usr/bin/python2
import os,time,commands

def extend(c,username,password):
#recieving all name of disks
	a1 = c.recv(60)
	print a1
	a2 = c.recv(60)
	print a2
	a3 = c.recv(60)
	print a3
	a4 = c.recv(60)
	print a4

	
	f1 = a1.strip()
	f2 = a2.strip()
	f3 = a3.strip()
	f4 = a4.strip()
	print f1
	print f2
	print f3
	print f4
	
	os.system("dialog --radiolist 'Choose hardisk to Extend' 16 50 4 1 {} off 2 {} off 3 {} off 4 {} off 2>/tmp/ex.txt".format(f1,f2,f3,f4))
	gh = open("/tmp/size.txt")
	name = gh.read()
	gh.close()
	
	if name == '1' and a1 != 'None':
		os.system("dialog --inputbox 'Enter size to Extend' 10 30 2>/tmp/size.txt")
        	g = open("/tmp/size.txt")
        	size = g.read()
        	g.close()
		# sending type
		c.send("nfs") 
		# sending size to server
        	c.send(size)

		#getting signal that server side processing is done
        	signal = c.recv(20)

		if signal == '1':
                # done
                	os.system("dialog --infobox 'Size Extended successfully' 10 50")
        	else:
                	os.system("dialog --infobox 'some error occured' 10 80")

	
	elif name == '2' and a2 != 'None':
		os.system("dialog --inputbox 'Enter size to Extend' 10 30 2>/tmp/size.txt")
        	g = open("/tmp/size.txt")
        	size = g.read()
        	g.close()
		# sending type
		c.send("sshfs") 
		# sending size to server
        	c.send(size)

		#getting signal that server side processing is done
        	signal = c.recv(20)

		if signal == '1':
                # done
                	os.system("dialog --infobox 'Size Extended successfully' 10 50")
        	else:
                	os.system("dialog --infobox 'some error occured' 10 80")


	elif name == '3' and a3 != 'None':
		os.system("dialog --inputbox 'Enter size to Extend' 10 30 2>/tmp/size.txt")
        	g = open("/tmp/size.txt")
        	size = g.read()
        	g.close()
		# sending type
		c.send("iscsi") 
		# sending size to server
        	c.send(size)

		#getting signal that server side processing is done
        	signal = c.recv(20)

		if signal == '1':
                # done
                	os.system("dialog --infobox 'Size Extended successfully' 10 50")
        	else:
                	os.system("dialog --infobox 'some error occured' 10 80")

	elif name == '4' and a4 != 'None':
		os.system("dialog --inputbox 'Enter size to Extend' 10 30 2>/tmp/size.txt")
        	g = open("/tmp/size.txt")
        	size = g.read()
        	g.close()
		# sending type
		c.send("samba") 
		# sending size to server
        	c.send(size)

		#getting signal that server side processing is done
        	signal = c.recv(20)

		if signal == '1':
                # done
                	os.system("dialog --infobox 'Size Extended successfully' 10 50")
        	else:
                	os.system("dialog --infobox 'some error occured' 10 80")

	else:
		os.system('dialog --infobox "choose Valid disk" 5 40')



		"""
#sending name of HDD to server
	#c.send(name)
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
		"""

