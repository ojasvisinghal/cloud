#!/usr/bin/python2
import os,commands,time,oneiaas

def onebrowser(c,username,password):
	ids  = c.recv(40)
	import MySQLdb
	os.system("systemctl restart mariadb")
	x=MySQLdb.connect("localhost")
	y=x.cursor()
	y.execute("use cloud;")
	w1 = y.execute("select * from REDHAT where USERNAME='{}500' and ID='{}'".format(username,ids))
	w2 = y.execute("select * from UBUNTU where USERNAME='{}500' and ID='{}'".format(username,ids))
	w3 = y.execute("select * from WINDOWS where USERNAME='{}500' and ID='{}'".format(username,ids))
	w4 = y.execute("select * from FEDORA where USERNAME='{}500' and ID='{}'".format(username,ids))
	w5 = y.execute("select * from MINT where USERNAME='{}500' and ID='{}'".format(username,ids))
	w6 = y.execute("select * from KALI where USERNAME='{}500' and ID='{}'".format(username,ids))
	w7 = y.execute("select * from REDHAT where USERNAME='{}1024' and ID='{}'".format(username,ids))
	w8 = y.execute("select * from UBUNTU where USERNAME='{}1024' and ID='{}'".format(username,ids))
	w9 = y.execute("select * from WINDOWS where USERNAME='{}1024' and ID='{}'".format(username,ids))
	w10 = y.execute("select * from FEDORA where USERNAME='{}1024' and ID='{}'".format(username,ids))
	w11 = y.execute("select * from MINT where USERNAME='{}1024' and ID='{}'".format(username,ids))
	w12 = y.execute("select * from KALI where USERNAME='{}1024' and ID='{}'".format(username,ids))

	if w1 == 0L and w2 == 0L and w3 == 0L and w4 == 0L and w5 == 0L and w6 == 0L and w7 == 0L and w8 == 0L and w9 == 0L and w10 == 0L and w11 == 0L:
		#return signal that no os yet installed	
		c.send('0')
		oneiaas.iaas(c,username,password)
	else:
		
		c.send("1")
		time.sleep(3)
		if y.execute("select * from REDHAT where USERNAME='{}500' and ID='{}'".format(username,ids)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport1,cport1))
			oneiaas.iaas(c,username,password)
			
	
		elif y.execute("select * from UBUNTU where USERNAME='{}500'and ID='{}'".format(username,ids)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport1,cport1))
			oneiaas.iaas(c,username,password)
			

		elif y.execute("select * from WINDOWS where USERNAME='{}500'and ID='{}'".format(username,ids)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport1,cport1))
			oneiaas.iaas(c,username,password)
			
		
		elif y.execute("select * from FEDORA where USERNAME='{}500'and ID='{}'".format(username,ids)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport1,cport1))
			oneiaas.iaas(c,username,password)
			

		elif y.execute("select * from MINT where USERNAME='{}500'and ID='{}'".format(username,ids)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport1,cport1))
			oneiaas.iaas(c,username,password)
			
		
		elif y.execute("select * from KALI where USERNAME='{}500'and ID='{}'".format(username,ids)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport1,cport1))
			oneiaas.iaas(c,username,password)
			
#1024
		
		elif y.execute("select * from REDHAT where USERNAME='{}1024'and ID='{}'".format(username,ids)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport1,cport1))
			oneiaas.iaas(c,username,password)
			
 		
		elif y.execute("select * from UBUNTU where USERNAME='{}1024'and ID='{}'".format(username,ids)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport1,cport1))
			oneiaas.iaas(c,username,password)
			

		
		elif y.execute("select * from WINDOWS where USERNAME='{}1024'and ID='{}'".format(username,ids)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport1,cport1))
			oneiaas.iaas(c,username,password)
			
		
		
		elif y.execute("select * from FEDORA where USERNAME='{}1024'and ID='{}'".format(username,ids)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport1,cport1))
			oneiaas.iaas(c,username,password)
			

		
		elif y.execute("select * from MINT where USERNAME='{}1024'and ID='{}'".format(username,ids)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport1,cport1))
			oneiaas.iaas(c,username,password)
			
		
		elif y.execute("select * from KALI where USERNAME='{}1024'and ID='{}'".format(username,ids))== 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("/root/Desktop/websockify-master/run -D 192.168.122.1:{} 192.168.122.1:{}".format(sport1,cport1))
			oneiaas.iaas(c,username,password)
			

		
		
