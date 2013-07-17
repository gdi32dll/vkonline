import urllib2
import sys
import re
import datetime
import time
import sqlite3
import vkonline
from multiprocessing import Process

UserIDs = []


def run( WaitTime = 300):
	UserIDs = []
	fl = open("UserIDs.txt","r")
	for l in fl:
		UserIDs.append(l.replace('\n',''))
	while 1:
		db_connector = sqlite3.connect('sqlite/vk_status.db')
		cursor = db_connector.cursor()
		for line in UserIDs:
			Status = vkonline.GetStatus(line)
			if (Status == vkonline.UserOffline):
				pass
			else:	
				cursor.execute("INSERT INTO users VALUES (?, ?, ?)", Status)
			
		db_connector.commit()
		cursor.close()
		db_connector.close()
		
		time.sleep(WaitTime)

run(300)
