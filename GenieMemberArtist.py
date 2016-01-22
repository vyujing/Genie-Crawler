#-*- encoding: utf-8 -*-
#Genie Web Crawler
import threading
import requests as rs
import bs4
import time
import re
import pdb

def getArtist(V):
	try:
		V = str(V)
		# mid = 301448745
		genie_url = "http://www.genie.co.kr/MyAlbum/f_main.asp?bgsq=" + str(V)
		response = rs.get(genie_url)
		html_content = response.text.encode(response.encoding)
		navigator = bs4.BeautifulSoup(html_content, "html5lib")
		navigator = navigator.find_all("div", class_="most-artist")
		#pdb.set_trace()
		#print(navigator)
		#		navigator = navigator.find_all("div", class_="most-artist")
		resultList = navigator[0].find_all('a')
		try:
			t1 = (resultList[2].contents[0])
			t1 = t1.encode('utf-8')
		except Exception as e:
			t1 = ""
		try:
			t2 = (resultList[4].contents[0])
			t2 = t2.encode('utf-8')
		except Exception as e:
			t2 = ""
		try:
			t3 = (resultList[6].contents[0])
			t3 = t3.encode('utf-8')
		except Exception as e:
			t3 = ""
		try:
			t4 = (resultList[8].contents[0])
			t4 = t4.encode('utf-8')
		except Exception as e:
			t4 = ""
		try:
			t5 = (resultList[10].contents[0])
			t5 = t5.encode('utf-8')
		except Exception as e:
			t5 = ""
		return (True, t1, t2, t3, t4, t5)
	except Exception as e:
		print ("-------Exception has Accoured-------")
		print (str(e))
		return (False,)
