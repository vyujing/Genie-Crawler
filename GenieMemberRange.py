#-*- encoding: utf-8 -*-
#Genie Web Crawler
import threading
import requests as rs
import bs4
import time
import re
import pdb

def getUser(mid):
	try:
		mid = str(mid)
		genie_url = "http://www.genie.co.kr/MyAlbum/f_main.asp?bgsq=" + mid
		response = rs.get(genie_url)
		html_content = response.text.encode(response.encoding)
		navigator = bs4.BeautifulSoup(html_content, "html5lib")
		realRankTag = navigator.find_all("span", class_="user")
		#pdb.set_trace()
		resultList = realRankTag[0].find_all('a')
		print(resultList)
		return True
	except Exception as e:
		print ("-------Exception has Accoured-------")
		print (str(e))
		return False

def getUserValue(begin, end, t):
	global maxV
	global minV
	mid = 0
	if t:
		ans = 0
	else:
		ans = 987654321
	while(begin <= end):
		mid = (begin + end) / 2
		print ("-------------processing %dth user---------------") % mid
		if getUser(mid) == True:
			if t:
				begin = mid + 1
				if ans < mid:
					ans = mid
			else:
				end = mid - 1
				if ans > mid:
					ans = mid
				
			print ("True")
		else:
			if t:
				end = mid - 1
			else:
				begin = mid + 1
			print ("False")
		print ("begin: %d\nend: %d") % (begin, end)
		time.sleep(0.1)
	if t:
		maxV = ans
	else:
		minV = ans

def getGenieRange():
	# valid range check(binary search)
	thread1 = threading.Thread(target=getUserValue, args=(306610167, 310000000, True,))
	thread2 = threading.Thread(target=getUserValue, args=(304000000, 306610167, False,))

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()
	print("maxUserNo: %d") % (maxV)
	print("minUserNo: %d") % (minV)
	return (minV, maxV)
