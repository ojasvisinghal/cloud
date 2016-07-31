#!/usr/bin/python2
import os,commands,time,oneiaas

def launch(c,username,password):
	id  = c.recv(40)
	import MySQLdb
	os.system("systemctl restart mariadb")
	x=MySQLdb.connect("localhost")
	y=x.cursor()
	y.execute("use cloud;")
	w1 = y.execute("select * from REDHAT where USERNAME='{}500' and ID='{}'".format(username,id))
	w2 = y.execute("select * from UBUNTU where USERNAME='{}500' and ID='{}'".format(username,id))
	w3 = y.execute("select * from WINDOWS where USERNAME='{}500' and ID='{}'".format(username,id))
	w4 = y.execute("select * from FEDORA where USERNAME='{}500' and ID='{}'".format(username,id))
	w5 = y.execute("select * from MINT where USERNAME='{}500' and ID='{}'".format(username,id))
	w6 = y.execute("select * from KALI where USERNAME='{}500' and ID='{}'".format(username,id))
	w7 = y.execute("select * from REDHAT where USERNAME='{}1024' and ID='{}'".format(username,id))
	w8 = y.execute("select * from UBUNTU where USERNAME='{}1024' and ID='{}'".format(username,id))
	w9 = y.execute("select * from WINDOWS where USERNAME='{}1024' and ID='{}'".format(username,id))
	w10 = y.execute("select * from FEDORA where USERNAME='{}1024' and ID='{}'".format(username,id))
	w11 = y.execute("select * from MINT where USERNAME='{}1024' and ID='{}'".format(username,id))
	w12 = y.execute("select * from KALI where USERNAME='{}1024' and ID='{}'".format(username,id))

	if w1 == 0L and w2 == 0L and w3 == 0L and w4 == 0L and w5 == 0L and w6 == 0L and w7 == 0L and w8 == 0L and w9 == 0L and w10 == 0L and w11 == 0L:
		#return signal that no os yet installed	
		c.send("0")
		oneiaas.iaas(c,username,password)
	else:
		c.send("1")
		time.sleep(3)
		if y.execute("select * from REDHAT where USERNAME='{}500' and ID='{}'".format(username,id)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("virsh start {}rhel500".format(username))
			oneiaas.iaas(c,username,password)
 		
		elif y.execute("select * from UBUNTU where USERNAME='{}500' and ID='{}'".format(username,id)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("virsh start {}ubun500".format(username))
			oneiaas.iaas(c,username,password)
 		
		
		elif y.execute("select * from WINDOWS where USERNAME='{}500' and ID='{}'".format(username,id)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("virsh start {}win500".format(username))
			oneiaas.iaas(c,username,password)
 		
		
		
		elif y.execute("select * from FEDORA where USERNAME='{}500' and ID='{}'".format(username,id)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("virsh start {}fed500".format(username))
			oneiaas.iaas(c,username,password)
 		

		
		elif y.execute("select * from MINT where USERNAME='{}500'and ID='{}'".format(username,id)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("virsh start {}mint500".format(username))
			oneiaas.iaas(c,username,password)
 		
		
		elif y.execute("select * from KALI where USERNAME='{}500' and ID='{}'".format(username,id)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("virsh start {}kali500".format(username))
			oneiaas.iaas(c,username,password)
 		
#1024
		 
		elif y.execute("select * from REDHAT where USERNAME='{}1024' and ID='{}'".format(username,id)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("virsh start{}rhel1024".format(username))
			oneiaas.iaas(c,username,password)
			
 		
		elif y.execute("select * from UBUNTU where USERNAME='{}1024' and ID='{}'".format(username,id)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("virsh start{}ubun1024".format(username))
			oneiaas.iaas(c,username,password)
			

		#w9 = y.execute("select * from WINDOWS where USERNAME='{}1024'and ID='{}'".format(username,id))
		elif y.execute("select * from WINDOWS where USERNAME='{}1024' and ID='{}'".format(username,id)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("virsh start{}win1024".format(username))
			oneiaas.iaas(c,username,password)
			
		
		#w10 = y.execute("select * from FEDORA where USERNAME='{}1024'and ID='{}'".format(username,id))
		elif y.execute("select * from FEDORA where USERNAME='{}1024' and ID='{}'".format(username,id))== 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("virsh start{}fed1024".format(username))
			oneiaas.iaas(c,username,password)
			

		#w11 = y.execute("select * from MINT where USERNAME='{}1024'and ID='{}'".format(username,id))
		elif y.execute("select * from MINT where USERNAME='{}1024' and ID='{}'".format(username,id)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("virsh start{}mint1024".format(username))
			oneiaas.iaas(c,username,password)
			

		#w12 = y.execute("select * from KALI where USERNAME='{}1024'and ID='{}'".format(username,id))
		elif y.execute("select * from KALI where USERNAME='{}1024' and ID='{}'".format(username,id)) == 1L:
			q = y.fetchall()
			sport1 = q[0][1]
			cport1 = q[0][2]
			c.send(sport1)
			os.system("virsh start{}kali1024".format(username))
			oneiaas.iaas(c,username,password)
			

		
