#!/usr/bin/python2

import os,commands,time,andos,usermenu,uservnc

def iaas(c,username,password):
	os.system("dialog --menu 'OSREMOTE TOOL' 50 70 11 1 'OS GALLERY' 2 'INSTALL OS' 3 'OS in vnc viewer'  4 OS in browser 5 'OS using Qrencode' 6 'Launch os' 7 'Shut OS' 8 'OS migrate' 9 'os in android through vnc viewer' 10 'BAck'  11 'Exit' 2>/tmp/qq.txt")
	f = open("/tmp/qq.txt")
        choice = f.read()
        f.close()

	c.send(choice)


#cancel
	if choice == '':
		usermenu.menu(c,username,password)

#os gallery
	elif choice == '1':
		usergallery.gallery(c,username,password)
	
#install os
	elif choice == '2':		
		useros.oss(c,username,password)

#os in vnc viewer
	elif choice == '3':
		pass

#os in browser
	elif choice == '4':
		pass

#os with qrencode
	elif choice == '5':
		userqren.qr(c,username,password)

#launch os
	elif choice == '6':
		userlist.listt(c,username,password)

#shut os
	elif choice == '7':
		pass

#os migrate
	elif choice == '8':
		usermigrate.migrate(c,username,password)

#os in android
	elif choice == '9':
		andos.andos(c,username,password)

#back
	elif choice == '10':
		usermenu.menu(c,username,password)

#exit
	elif choice == '11':
		os.system("dialog --infobox 'HAVE A Nice DAY !!!! BBYE' 10 40")
