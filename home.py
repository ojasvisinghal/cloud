
#!/usr/bin/python2

import services,os,signal,commands,socket,time,sys
s = socket.socket()

s.connect(("192.168.122.1",3000))

os.system("dialog --inputbox 'Enter username' 7 60 2>/tmp/user.txt")
fh = open("/tmp/user.txt")
user = fh.read()
fh.close()

os.system("dialog --insecure --passwordbox 'Enter password' 7 60 2>/tmp/passwd.txt")
fk = open("/tmp/passwd.txt")
passwd = fk.read()
fk.close()

s.send(user)
s.send(passwd)

os.system("dialog --radiolist 'Login / Registration' 15 60 2 1 'Login' on 2 'register' off  2>/tmp/rgis.txt")
fk = open("/tmp/rgis.txt")
sign = fk.read()
fk.close()

#sending signal whether to login ar register
s.send(sign)
if sign == '1':
#recieving signal
	sk = s.recv(30)
	if sk == '1':
		os.system("dialog --radiolist   'Choose what you want , We will provide !!!' 15 60 6 1 'Storage as a Service(STAAS)'   on     2 'Infrastructure as a Service(IAAS)'  off    3 'Platform as a Service(PAAS)'  off    4 'Software as a Service(SAAS)'     off  5 'Container as a Service(CAAS)' off 6 'EXIT' off    2>/tmp/a.txt")


	        fh = open("/tmp/a.txt")
	        data = fh.read()
	        fh.close()

        	s.send(data)
	        if data == '1':
        	        services.staas(s,user,passwd)

        	elif data == '2':
                	services.iaas(s,user,passwd)

        	elif data == '3':
                	services.paas(s,user,passwd)

        	elif data == '4':
                	services.saas(s,user,passwd)

		elif data == '5':
			services.caas(s,user,passwd)
        	else:
                	os.system("dialog --infobox 'Bye ! Have a nice day .....' 15 30")
                	time.sleep(2)
                	s.close()

		
	else:
		os.system("dialog --infobox 'No Username or password exist' 5 50")

#register

elif sign == '2':
#recieving signal
	sk = s.recv(30)
	if sk == '1':
		os.system("dialog --infobox 'Registration Successful' 5 80")
		os.system("dialog --radiolist   'Choose what you want , We will provide !!!' 15 60 6 1 'Storage as a Service(STAAS)'   on     2 'Infrastructure as a Service(IAAS)'  off    3 'Platform as a Service(PAAS)'  off    4 'Software as a Service(SAAS)'     off  5 'Container as a Service(CAAS)' off 6 'EXIT' off    2>/tmp/a.txt")

		fh = open("/tmp/a.txt")
		data = fh.read()
		fh.close()

		s.send(data)
		if data == '1':
			services.staas(s,user,passwd)

		elif data == '2':
			services.iaas(s,user,passwd)

		elif data == '3':
			services.paas(s,user,passwd)

		elif data == '4':
			services.saas(s,user,passwd)

		elif data == '5':
			services.caas(s,user,passwd)

		else:
			os.system("dialog --infobox 'Bye ! Have a nice day .....' 15 30")
			time.sleep(2)
			s.close()

	else:
		os.system("dialog --infobox 'Oops!! user with this username already exists' 7 70")




