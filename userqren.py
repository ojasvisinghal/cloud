#!/usr/bin/python2

import os,commands
def qr(c,username,password):
	a = c.recv(10)
	b = c.recv(10)
	d = c.recv(10)
	if a == '1':
		os.system("mkdir /root/Desktop/{}r".format(username))
		os.system("mount 192.168.122.1:/media/{0}rhel /root/Desktop/{0}r".format(username))
		
	if b == '1':
		os.system("mkdir /root/Desktop/{}u".format(username))
		os.system("mount 192.168.122.1:/media/{0}ub /root/Desktop/{0}u".format(username))
		
	if d == '1':
		os.system("mkdir /root/Desktop/{}w".format(username))
		os.system("mount 192.168.122.1:/media/{0}win /root/Desktop/{0}w".format(username))
		
	
