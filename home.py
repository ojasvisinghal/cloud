
#!/usr/bin/python2

import services,os,signal,commands,socket,time,sys,usermenu,user
s = socket.socket()

s.connect(("192.168.122.1",3000))



os.system("dialog --infobox 'W E L C O M E !!!! TO ORASCO CLOUD \ FASTER THAN OTHER CLOUD SERVICE PROVIDERS' 30 50")

time.sleep(3)

os.system("dialog --msgbox 'Click ok to continue....... \ else Press CTRL+C' 30 50")

os.system("dialog --inputbox 'Enter username' 7 40 2>/tmp/user.txt")
fh = open("/tmp/user.txt")
username = fh.read()
fh.close()

os.system("dialog --insecure --passwordbox 'Enter password' 7 40 2>/tmp/passwd.txt")
fk = open("/tmp/passwd.txt")
passwd = fk.read()
fk.close()

s.send(username)
s.send(passwd)

os.system("dialog --radiolist 'Login / Registration' 15 60 2 1 'Login' on 2 'register' off  2>/tmp/rgis.txt")
fk = open("/tmp/rgis.txt")
sign = fk.read()
fk.close()

#sending signal whether to login ar register
s.send(sign)


#login
if sign == '1':
#recieving signal
	sk = s.recv(30)
	if sk == '1':
		usermenu.menu(s,username,passwd)
		
	else:
		os.system("dialog --infobox 'No Username or password exist' 40 50")

#register
elif sign == '2':
#recieving signal
	sk = s.recv(30)
	if sk == '1':
		usermenu.menu(s,username,passwd)
		
	else:
		os.system("dialog --infobox 'Oops!! user with this username already exists' 40 50")

elif sign == '':
	os.system("dialog --infobox 'Thanks for visiting' 30 50")


