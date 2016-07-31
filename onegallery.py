#!/usr/bin/python2
import os,commands,time

#fetching all os with this user

def gallery(c,username,password):
	import MySQLdb
	os.system("systemctl restart mariadb")
	x=MySQLdb.connect("localhost")
	y=x.cursor()
	y.execute("use cloud;")
	w1 = y.execute("select * from REDHAT where USERNAME='{}500'".format(username))
	w2 = y.execute("select * from UBUNTU where USERNAME='{}500'".format(username))
	w3 = y.execute("select * from WINDOWS where USERNAME='{}500'".format(username))
	w4 = y.execute("select * from FEDORA where USERNAME='{}500'".format(username))
	w5 = y.execute("select * from MINT where USERNAME='{}500'".format(username))
	w6 = y.execute("select * from KALI where USERNAME='{}500'".format(username))
	w7 = y.execute("select * from REDHAT where USERNAME='{}1024'".format(username))
	w8 = y.execute("select * from UBUNTU where USERNAME='{}1024'".format(username))
	w9 = y.execute("select * from WINDOWS where USERNAME='{}1024'".format(username))
	w10 = y.execute("select * from FEDORA where USERNAME='{}1024'".format(username))
	w11 = y.execute("select * from MINT where USERNAME='{}1024'".format(username))
	w12 = y.execute("select * from KALI where USERNAME='{}1024'".format(username))


	if w1 == 0L and w2 == 0L and w3 == 0L and w4 == 0L and w5 == 0L and w6 == 0L and w7 == 0L and w8 == 0L and w9 == 0L and w10 == 0L and w11 == 0L:
		#return signal that no os yet installed	
		c.send('0')
	
	else:
		c.send("1")


		w1 = y.execute("select * from REDHAT where USERNAME='{}500'".format(username))
		if w1 == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			val1 = '1'

		else:
			val1 = '0'

 		w2 = y.execute("select * from UBUNTU where USERNAME='{}500'".format(username))
		if w2 == 1L:
			q = y.fetchall()
			sport2 = q[0][1]
			cport2 = q[0][2]
			val2 = '1'

		else:
			val2 = '0'

		w3 = y.execute("select * from WINDOWS where USERNAME='{}500'".format(username))
		if w3 == 1L:
			q = y.fetchall()
			sport3 = q[0][1]
			cport3 = q[0][2]
			val3 = '1'

		else:
			val3 = '0'
		
		w4 = y.execute("select * from FEDORA where USERNAME='{}500'".format(username))
		if w4 == 1L:
			q = y.fetchall()
			sport4 = q[0][1]
			cport4 = q[0][2]
			val4 = '1'

		else:
			val4 = '0'


		w5 = y.execute("select * from MINT where USERNAME='{}500'".format(username))
		if w5 == 1L:
			q = y.fetchall()
			sport5 = q[0][1]
			cport5 = q[0][2]
			val5 = '1'

		else:
			val5 = '0'

		w6 = y.execute("select * from KALI where USERNAME='{}500'".format(username))
		if w6 == 1L:
			q = y.fetchall()
			sport6 = q[0][1]
			cport6 = q[0][2]
			val6 = '1'

		else:
			val6 = '0'
#1024
		w7 = y.execute("select * from REDHAT where USERNAME='{}1024'".format(username))
		if w7 == 1L:
			q = y.fetchall()
			sport7 = q[0][1]
			cport7 = q[0][2]
			val7 = '1'

		else:
			val7 = '0'

 		w8 = y.execute("select * from UBUNTU where USERNAME='{}1024'".format(username))
		if w8 == 1L:
			q = y.fetchall()
			sport8 = q[0][1]
			cport8 = q[0][2]
			val8 = '1'
		else:
			val8 = '0'

		w9 = y.execute("select * from WINDOWS where USERNAME='{}1024'".format(username))
		if w9 == 1L:
			q = y.fetchall()
			sport9 = q[0][1]
			cport9 = q[0][2]
			val9 = '1'

		else:
			val9 = '0'
		
		w10 = y.execute("select * from FEDORA where USERNAME='{}1024'".format(username))
		if w10 == 1L:
			q = y.fetchall()
			sport10 = q[0][1]
			cport10 = q[0][2]
			val10 = '1'

		else:
			val10 = '0'


		w11 = y.execute("select * from MINT where USERNAME='{}1024'".format(username))
		if w11 == 1L:
			q = y.fetchall()
			sport11 = q[0][1]
			cport11 = q[0][2]
			val11 = '1'

		else:
			val11 = '0'

		w12 = y.execute("select * from KALI where USERNAME='{}1024'".format(username))
		if w12 == 1L:
			q = y.fetchall()
			sport12 = q[0][1]
			cport12 = q[0][2]
			val12 = '1'

		else:
			val12 = '0'


		c.send(val1)
		time.sleep(1)
		c.send(val2)
		time.sleep(1)
		c.send(val3)
		time.sleep(1)
		c.send(val4)
		time.sleep(1)
		c.send(val5)
		time.sleep(1)
		c.send(val6)
		time.sleep(1)
		c.send(val7)
		time.sleep(1)
		c.send(val8)
		time.sleep(1)
		c.send(val9)
		time.sleep(1)
		c.send(val10)
		time.sleep(1)
		c.send(val11)
		time.sleep(1)
		c.send(val12)
		time.sleep(1)

		if val1 == '1':
			print val1
			c.send(sport1)
			time.sleep(1)
			print commands.getstatusoutput("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport1,cport1))

		else:
			print 'error'
		if val2 == '1':
			print val2
			c.send(sport2)
			time.sleep(1)
			print commands.getstatusoutput("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport2,cport2))
		else:
			print 'getlost once more'
		if val3 == '1':
			print val3
			c.send(sport3)
			time.sleep(1)
			print commands.getstatusoutput("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport3,cport3))
		else:
			print 'getlost once more'
		if val4 == '1':
			print val4
			c.send(sport4)
			time.sleep(1)
			print commands.getstatusoutput("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport4,cport4))
		else:
			print 'getlost once more'
		
		if val5 == '1':
			print val5
			c.send(sport5)
			time.sleep(1)
			print commands.getstatusoutput("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport5,cport5))
		else:
			print 'getlost once more'

		if val6 == '1':
			print val6
			c.send(sport6)
			time.sleep(1)
			print commands.getstatusoutput("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport6,cport6))
		else:
			print 'getlost once more'
#1024
		if val7 == '1':
			print val7
			c.send(sport7)
			time.sleep(1)
			print commands.getstatusoutput("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport7,cport7))

		else:
			print 'error'
		if val8 == '1':
			print val8
			c.send(sport8)
			time.sleep(1)
			print commands.getstatusoutput("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport8,cport8))
		else:
			print 'getlost once more'
		if val9 == '1':
			print val9
			c.send(sport9)
			time.sleep(1)
			print commands.getstatusoutput("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport9,cport9))
		else:
			print 'getlost once more'
		if val10 == '1':
			print val10
			c.send(sport10)
			time.sleep(1)
			print commands.getstatusoutput("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport10,cport10))
		else:
			print 'getlost once more'
		
		if val11 == '1':
			print val11
			c.send(sport11)
			time.sleep(1)
			print commands.getstatusoutput("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport11,cport11))
		else:
			print 'getlost once more'

		if val12 == '1':
			print val12
			c.send(sport12)
			time.sleep(1)
			print commands.getstatusoutput("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport12,cport12))
		else:
			print 'getlost once more'						
