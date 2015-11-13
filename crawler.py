#-*- encoding: utf-8 -*-
#Genie Web Crawler
import requests as rs
import bs4
import time

def getTopRank():
	naver_url = "http://www.naver.com"
	response = rs.get(naver_url)

	html_content = response.text.encode(response.encoding)

	navigator = bs4.BeautifulSoup(html_content, "html5lib")

	realRankTag = navigator.find_all(id='realrank')
	resultList = realRankTag[0].find_all('a')

	keywords = [item['title'] for item in resultList]

	for index, keyword in enumerate(keywords):
		resultText = '[%d위] %s' % (index, keyword.encode('utf-8'))
		print resultText

if __name__ == '__main__':
	while(True):
		getTopRank()
		time.sleep(5)
