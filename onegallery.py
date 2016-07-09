#!/usr/bin/python2
import os,commands,time

#fetching all os with this user

def gallery(c,username,password):
	import MySQLdb
	os.system("systemctl restart mariadb")
	x=MySQLdb.connect("localhost")
	y=x.cursor()
	y.execute("use cloud;")
	w1 = y.execute("select * from REDHAT where USERNAME='{}'".format(username))
	w2 = y.execute("select * from UBUNTU where USERNAME='{}'".format(username))
	w3 = y.execute("select * from WINDOWS where USERNAME='{}'".format(username))

	if w1 == 0L and w2 == 0L and w3 == 0L:
		#return signal that no os yet installed	
		c.send('0')


		
	else:

		c.send("1")
		w1 = y.execute("select * from REDHAT where USERNAME='{}'".format(username))
		if w1 == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			val1 = '1'

		else:
			val1 = '0'

 		w2 = y.execute("select * from UBUNTU where USERNAME='{}'".format(username))
		if w2 == 1L:
			q = y.fetchall()
			sport2 = q[0][1]
			cport2 = q[0][2]
			val2 = '1'

		else:
			val2 = '0'

		w3 = y.execute("select * from WINDOWS where USERNAME='{}'".format(username))
		if w3 == 1L:
			q = y.fetchall()
			sport3 = q[0][1]
			cport3 = q[0][2]
			val3 = '1'

		else:
			val3 = '0'


		c.send(val1)
		c.send(val2)
		c.send(val3)

		if val1 == '1':
			print val1
			c.send(sport1)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport1,cport1))

		else:
			print 'error'
		if val2 == '1':
			print val2
			c.send(sport2)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport2,cport2))

		if val3 == '1':
			print val3
			c.send(sport3)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport3,cport3))
































###########################################
		"""
		c.send('1')
		p = y.fetchall()
		if p[0][1] != None:
			p1 = 0
		
			port1 = p[0][2]
			s1 = p[0][7]
			print port1
			print s1

		else:
			p1 = 1

		if p[0][3] != None:
		
			p2 = 0
			port2 = p[0][4]
			s2 = p[0][8]
			print port2
			print s2

		else:
			p2 = 1

		if p[0][5] != None:
			p3 = 0
		
			port3 = p[0][6]
			s3 = p[0][9]
			print port3
			print s3

		else:
			p3 = 1


		#sending p1 p2 p3
		c.send('{}'.format(p1))
		c.send('{}'.format(p2))
		c.send('{}'.format(p3))

		if p1 == '0':
			c.send(port1)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(port1,s1))

		if p2 == '0':
			c.send(port2)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(port2,s2))

		if p3 == '0':
			c.send(port3)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(port3,s3))

		"""
