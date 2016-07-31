#!/usr/bin/python2

import os,commands,socket,MySQLdb,onemenu

s=socket.socket()
ip=""
port=3000
s.bind((ip,port))
s.listen(5)

os.system("systemctl restart mariadb")
x=MySQLdb.connect("localhost")
y=x.cursor()

def main(c):
	username = c.recv(40)
	password = c.recv(40)

	#recieving signal whether to login ar register
	sign = c.recv(30)



#login
	if sign == '1':
		x=MySQLdb.connect("localhost")
		y=x.cursor()
		y.execute("use cloud;")
		s=y.execute("select * from USER where USERNAME='{}' and PASSWORD='{}';".format(username,password))
	
		if s != 0L:
			c.send("1")
			onemenu.menu(c,username,password)
	
#register
	else:

		x=MySQLdb.connect("localhost")
		y=x.cursor()
		#doing entry to database as well as creating user
		y.execute("use cloud;")
		k=y.execute("insert into USER(USERNAME,PASSWORD) values('{}','{}');".format(username,password))
		r = y.execute("insert into SNAP(USERNAME) values('{0}')".format(username))	
		x.commit()
		os.system("useradd {}".format(username))
		os.system("echo {}| passwd {} --stdin".format(password,username))
		#sending signal for successful registration
		c.send("1")
		onemenu.menu(c,username,password)

while True:
	c,addr=s.accept()
	main(c)
