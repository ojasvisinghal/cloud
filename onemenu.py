#!/usr/bin/python2


import MySQLdb,os,commands,one

def menu(c,username,password):
		
		data = c.recv(30)
		if data == '':
			c.close()
		elif data == '1':
			one.staas(c,username,password)
		elif data == '2':
			one.iaas(c,username,password)
		elif data == '3':
			one.paas(c,username,password)
		elif data == '4':
			one.saas(c,username,password)
		elif data == '5':
			one.caas(c,username,password)

