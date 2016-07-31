#!/usr/bin/python2

import MySQLdb,os

def filee(username):
	os.system("systemctl restart mariadb")
	x=MySQLdb.connect("localhost")
	y=x.cursor()
	y.execute("use cloud;")
	fh = open("/root/Desktop/folderServer/derive.txt",'w')
	e = y.execute("select NFS from USER where USERNAME='{}';".format(username))

	q = y.fetchall()
	if q[0][0]!= None:
		fh.write("{}\n".format(q[0][0]))
	else:
		fh.write("None\n")

	e =y.execute("select SSHFS from USER where USERNAME='{}';".format(username))
	q = y.fetchall()
	if q[0][0]!= None:
		fh.write("{}\n".format(q[0][0]))
	else:
		fh.write("None\n")

	e =y.execute("select ISCSI from USER where USERNAME='{}';".format(username))
	q = y.fetchall()
	if q[0][0]!= None:
		fh.write("{}\n".format(q[0][0]))
	else:
		fh.write("None\n")

	e =y.execute("select SAMBA from USER where USERNAME='{}';".format(username))
	q = y.fetchall()
	if q[0][0]!= None:
		fh.write("{}\n".format(q[0][0]))
	else:
		fh.write("None\n")

	fh.close()
