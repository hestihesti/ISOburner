import os
import sys
import time
import subprocess
from termcolor import colored
from images import banner


def check():
	if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
		raise PermissionError(colored('Run "sudo su" To Run This Script', 'red'))

def make():
	banner.img()
	time.sleep(1)
	fdisk = 'fdisk -l'
	os.system(fdisk)
	usb = input(colored('Whats The USB ID (ex. /dev/sdb1):\n> ', 'yellow'))
	umount = 'umount ' + usb
	os.system(umount)
	vfat = 'mkfs.vfat ' + usb
	os.system(vfat)
	fsck = 'fsck ' + usb
	os.system(fsck)
	path = input(colored('/Path/To/ISO/Image.iso:  ', 'yellow'))
	dd = 'dd if=' + path + ' of=/dev/sdx status=progress oflag=sync'
	try:
		os.system(dd)
		print('\n \n \n')
		print(colored('[+] ISO Has Been Successfully Burned To USB!', 'green'))
	except:
		print(colored('There Was An Error', 'red'))

check()
make()
