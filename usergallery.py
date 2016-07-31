#!/usr/bin/python2
import os,commands,time

def gallery(c,username,password):
	sig =c.recv(30)

	if sig == '0':
		os.system("dialog --infobox 'no os yet' 10 30")

	elif sig == '1':
		p1 = c.recv(20)
		print p1
		p2 = c.recv(20)
		print p2
		p3 = c.recv(20)
		print p3
		p4 = c.recv(20)
		print p4
		p5 = c.recv(20)
		print p5
		p6 = c.recv(20)
		print p6
		p7 = c.recv(20)
		print p7
		p8 = c.recv(20)
		print p8
		p9 = c.recv(20)
		print p9
		p10 = c.recv(20)
		print p10
		p11 = c.recv(20)
		print p11
		p12 = c.recv(20)
		print p12
		l = []
		if p1 != '0':
			sport1 = c.recv(30)
			print sport1
			l.append('http://192.168.122.1/vnc/?ip=192.168.122.1&port={}'.format(sport1))
			
		if p2 != '0':
			sport2 = c.recv(30)
			print sport2
			l.append('http://192.168.122.1/vnc/?ip=192.168.122.1&port={}'.format(sport2))
		
		if p3 != '0':
			sport3 = c.recv(30)
			print sport3
			l.append('http://192.168.122.1/vnc/?ip=192.168.122.1&port={}'.format(sport3))
		
		if p4 != '0':
			sport4 = c.recv(30)
			print sport4
			l.append('http://192.168.122.1/vnc/?ip=192.168.122.1&port={}'.format(sport4))


		if p5 != '0':
			sport5 = c.recv(30)
			print sport5
			l.append('http://192.168.122.1/vnc/?ip=192.168.122.1&port={}'.format(sport5))

		if p6 != '0':
			sport6 = c.recv(30)
			print sport6
			l.append('http://192.168.122.1/vnc/?ip=192.168.122.1&port={}'.format(sport6))
		
		if p7 != '0':
			sport7 = c.recv(30)
			print sport1
			l.append('http://192.168.122.1/vnc/?ip=192.168.122.1&port={}'.format(sport7))
			
		if p8 != '0':
			sport8 = c.recv(30)
			print sport8
			l.append('http://192.168.122.1/vnc/?ip=192.168.122.1&port={}'.format(sport8))
		
		if p9 != '0':
			sport9 = c.recv(30)
			print sport9
			l.append('http://192.168.122.1/vnc/?ip=192.168.122.1&port={}'.format(sport9))
		
		if p10 != '0':
			sport10 = c.recv(30)
			print sport10
			l.append('http://192.168.122.1/vnc/?ip=192.168.122.1&port={}'.format(sport10))


		if p11 != '0':
			sport11 = c.recv(30)
			print sport11
			l.append('http://192.168.122.1/vnc/?ip=192.168.122.1&port={}'.format(sport11))

		if p12 != '0':
			sport12 = c.recv(30)
			print sport12
			l.append('http://192.168.122.1/vnc/?ip=192.168.122.1&port={}'.format(sport12))


		tabs = ''
		length = len(l)
		for i in range(length):
			tabs = tabs + l[i] + ' '	
#running os gallery		
		if length != 0:
			os.system("firefox {}".format(tabs))

		
