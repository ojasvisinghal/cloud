#!/usr/bin/python2

import servers,os,commands,socket,MySQLdb

s=socket.socket()
ip=""
port=3000
s.bind((ip,port))
s.listen(5)
c,addr=s.accept()

os.system("systemctl restart mariadb")
x=MySQLdb.connect("localhost")
y=x.cursor()

username = c.recv(40)
password = c.recv(40)

#recieving signal whether to login ar register
sign = c.recv(30)

#login
if sign == '1':
	y.execute("use cloud;")
	s=y.execute("select * from USER where USERNAME='{}' and PASSWORD='{}';".format(username,password))
	
	if s != 0L:#means user exists
		#checking password
		z=commands.getstatusoutput("sshpass -p {} ssh {}@192.168.122.116 ".format(password,username))
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
		elif data == '5':
		        servers.caas(c,username,password)
	else:
	#send signal that user does not exits
	#register page
		#c.send("0")
		pass


#register
else:
	#checking whether user alredy exists or not
	y.execute("use cloud;")
	s=y.execute("select * from USER where USERNAME='{}' and PASSWORD='{}';".format(username,password))
        if s != 0L:
		#sending signal user already exists
		#c.send("0")
		print 'ddddd'
		pass
	else:
		#doing entry to database as well as creating user
		y.execute("use cloud;")
		k=y.execute("insert into USER(USERNAME,PASSWORD) values('{}','{}');".format(username,password))
		#creating user

		x.commit()
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
		elif data == '5':
			servers.caas(c,username,password)




