#!/usr/bin/python2

import os,commands,time,usermenu

def paas(c,username,password):
	os.system("dialog --menu 'Choose your platform!! what you want' 30 80 7 1 'PYTHON'  2 'PERL'  3 'PHP' 4 'Ruby' 5 'MySQL' 6 'Back' 7 'Exit' 2>/tmp/sas.txt")
	o = open("/tmp/sas.txt")
	choice = o.read()
        o.close()
	
	c.send(choice)
#cancel
	if choice == '':
		usermenu.menu(c,username,password)

#python
	elif choice == '1':
		ip = c.recv(30)
		os.system("route add -net 172.17.0.0/16 gw 192.168.122.1")
		os.system("ssh {}@{}".format(username,ip))
#perl			
	elif choice == '2':
                ip = c.recv(30)
                os.system("route add -net 172.17.0.0/16 gw 192.168.122.1")
                os.system("ssh {}@{}".format(username,ip))
#php              
	elif choice == '3':
                ip = c.recv(30)
                os.system("route add -net 172.17.0.0/16 gw 192.168.122.1")
                os.system("ssh {}@{}".format(username,ip))
#ruby                       
	elif choice == '4':
                ip = c.recv(30)
                os.system("route add -net 172.17.0.0/16 gw 192.168.122.1")
                os.system("ssh {}@{}".format(username,ip))
                        
#MySQL
	elif choice == '5':
                ip = c.recv(30)
                os.system("route add -net 172.17.0.0/16 gw 192.168.122.1")
                os.system("ssh {}@{}".format(username,ip))
                        
#back
	elif choice == '6':
                usermenu.menu(c,username,password)
                        
#exit
	elif choice == '7':
		os.system("dialog --menu 'Bye Have a nice day !!!!' 10 50")

