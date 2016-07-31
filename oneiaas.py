#!/usr/bin/python2


import os,commands,time,onemenu,onevnc,onegallery,oneinstall,onebrowser,onelaunch,andos,oneshut,onevnc,oneqren,oneossnap
def iaas(c,username,password):
	choice = c.recv(30)

#cancel button
	if choice == '':
		onemenu.menu(c,username,password)
#gallery
	elif choice == '1':
		onegallery.gallery(c,username,password)
	
#install
	elif choice == '2':
		oneinstall.install(c,username,password)

#vnc
	elif choice == '3':
		onevnc.onevnc(c,username,password)

#os in browser
	elif choice == '4':
		onebrowser.onebrowser(c,username,password)

#qr code
	elif choice == '5':
		#qrencode collection
		#qrenco.qren(c,username,password)
		oneqren.qren(c,username,password)

#launch os
	elif choice == '6':
		onelaunch.launch(c,username,password)	

#shut os
	elif choice == '7':
		oneshut.shut(c,username,password)

#os snapshot
	elif choice == '8':
		oneossnap.ossnap(c,username,password)

#os in android
	elif choice == '9':
		andos.andos(c,username,password)

#back
	elif choice == '10':
		onemenu.menu(c,username,password)

#exit
	elif choice == '11':
		c.close()



	#migrate
	"""
		os.system("virt-install --name {0} --import --hvm --ram {1} --disk path=/var/lib/libvirt/images/oja.qcow2 --vcpus {2} --os-type linux --graphics vnc,port=5999,listen = 0.0.0.0".format(username,ram,cpu))

                os.system("setenforce 0")
                os.system("iptables -F")
                fh =open("/etc/exports",'a')
                fh.write("/var/lib/libvirt/images/oja.qcow2 *(rw)\n")
                fh.close()

                os.system("systemctl restart nfs-server")
                os.system("chmod 777 /var/lib/libvirt/images/*")
        #get ip of client in ip ip[1][0]        
                os.system("virsh migrate --live {} qemu+ssh://{}/system".format(username,ip))

	"""  

