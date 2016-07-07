#!/usr/bin/python2

import servers,os,commands,socket

s=socket.socket()
ip=""
port=3000
s.bind((ip,port))
s.listen(5)


def main(c):
	username = c.recv(40)
	password = c.recv(40)

	#recieving signal whether to login ar register
	sign = c.recv(30)
	#login
	if sign == '1':
		y= commands.getstatusoutput("cd /home/{}".format(username))
		if y[0]==0:
			#checking password
			z=commands.getstatusoutput("sshpass -p {} ssh {}@192.168.122.89 ".format(password,username))
			c.send("1")
			data = c.recv(30)
		        if data == '1':
		                servers.staas(c,username,password)
		        elif data == '2':
		                servers.iaas(c,username,password)
		        elif data == '3':
		                servers.paas(c,username,password)
		        elif data == '4':
		                servers.saas(c,username,password)

		else:
		#send signal that user does not exits
			c.send("0")


	#register
	else:
		y= commands.getstatusoutput("cd /home/{}".format(username))
		if y[0]==0:
			#sending signal user already exists
			c.send("0")
		else:
			os.system("useradd {}".format(username))
			os.system("echo {}| passwd {} --stdin".format(password,username))
	#sending signal for successful registration
			c.send("1")

			data = c.recv(30)
			if data == '1':
				servers.staas(c,username,password)
			elif data == '2':
				servers.iaas(c,username,password)
			elif data == '3':
				servers.paas(c,username,password)
			elif data == '4':
				servers.saas(c,username,password)



while True:
	c,addr=s.accept()
	main(c)
