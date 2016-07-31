#!/usr/bin/python2


import MySQLdb,os,commands,onestaas,oneiaas,onepaas,onesaas,onecaas

def menu(c,username,password):
		
		data = c.recv(30)
		if data == '':
			c.close()
		elif data == '1':
			onestaas.staas(c,username,password)
		elif data == '2': 
			oneiaas.iaas(c,username,password)
		elif data == '3':
			onepaas.paas(c,username,password)
		elif data == '4':
			onesaas.saas(c,username,password)
		elif data == '5':
			onecaas.caas(c,username,password)
		elif data == '6':
			c.close()
