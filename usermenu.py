#!/usr/bin/python2

import os,commands,time,userstaas,userpass,useriaas,usercaas,usersaas

def menu(s,username,passwd):
		os.system("dialog --radiolist   'Choose what you want , We will provide !!!' 15 60 6 1 'Storage as a Service(STAAS)'   on     2 'Infrastructure as a Service(IAAS)'  off    3 'Platform as a Service(PAAS)'  off    4 'Software as a Service(SAAS)'     off  5 'Container as a Service(CAAS)' off 6 'EXIT' off    2>/tmp/a.txt")


	        fh = open("/tmp/a.txt")
	        data = fh.read()
	        fh.close()
		
        	s.send(data)

		if data == '':
			os.system("dialog --infobox 'bye have a nice day !!!' 6 40 ")

	        elif data == '1':
        	        userstaas.staas(s,username,passwd)

        	elif data == '2':
                	useriaas.iaas(s,username,passwd)

        	elif data == '3':
                	userpass.paas(s,username,passwd)

        	elif data == '4':
                	usersaas.saas(s,username,passwd)

		elif data == '5':
			usercaas.caas(s,username,passwd)

        	elif data == '6':
                	os.system("dialog --infobox 'Bye ! Have a nice day .....' 15 30")
                	time.sleep(2)

