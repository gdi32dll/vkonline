# -*- coding: utf-8 -*-
import urllib2
import sys
import re
import datetime
import time
import sqlite3

UserOnline = 1
UserOffline = 0
		
def findString(string,source):
	m = re.search(string,source)
	if (m != None):
		return UserOnline
	return UserOffline

def isOnlineVK(id):
	adress = "http://vk.com/" + id
	for line in urllib2.urlopen(adress):
		if (findString('pp_last_activity">Online',line)):
			return UserOnline
	return UserOffline
	
def GetStatus(id):	
	isOnline = isOnlineVK(id)
	now_time = datetime.datetime.now()
	if (isOnline):
		return (id, now_time.strftime( "%d.%m.%Y %I:%M %p"), UserOnline)
	else:
		return 0 #(id, now_time.strftime( "%d.%m.%Y %I:%M %p"), UserOffline)

		time.sleep(WaitTime)
		
