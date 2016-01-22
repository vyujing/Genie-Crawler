#-*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
import MySQLdb
import sys
import requests as rs
import bs4
import time
import re
import pdb

def getAlgoInfo(pid,uid):
	global d
	d = False
	try:
		judge_url = "https://www.acmicpc.net/status/?problem_id="+pid+"&user_id="+uid+"&language_id=-1&result_id=-1&from_problem=1"
		response = rs.get(judge_url)
		html_content = response.text.encode(response.encoding)
		navigator = bs4.BeautifulSoup(html_content, "html5lib")
		realRankTag = navigator.find_all("td", class_="result")
		for r in realRankTag:
			result = r.find_all("span")
			result = result[0].string.strip()
			d = True
			# print(result)
			if result.encode('utf-8') == "맞았습니다!!":
				return 1
	except Exception as e:
		print(str(e))
		return False
	if d is True:
		return -1
	return 0

if __name__ == "__main__":
	try:
		db = MySQLdb.connect("localhost","vyujing","","vyujing" )
		usql = "SELECT ID,NAME FROM MEM ORDER BY NAME"
		psql = "SELECT NO FROM PROBLEM ORDER BY IDX"
		userCur = db.cursor()
		probCur = db.cursor()

		userCur.execute("set names utf8");
		probCur.execute("set names utf8");

		userCur.execute(usql)
		
		userRow = userCur.fetchone()
		probCur = db.cursor()
		probCur.execute(psql)
		probRow = probCur.fetchone()
		print("<table border=1>")
		print("<tr>")
		print("<th>이름</th>")
		while probRow is not None:
			print("<th width=100><a href=\"https://www.acmicpc.net/problem/%s\">%s</a></th>" % (probRow[0], probRow[0]))
			probRow = probCur.fetchone()
		print("</tr>")
		print()
		while userRow is not None:
			probCur = db.cursor()
			probCur.execute(psql)
			probRow = probCur.fetchone()
			print("<tr>")
			print("<td>%s</td>" % (userRow[1]))
			while probRow is not None:
				res = getAlgoInfo(probRow[0], userRow[0])
				# print("%s는 %s를 풀었나 : %r" % (userRow[0], probRow[0], res))
				if res is 1:
					print("<td style=\"color:blue;font-weight:bold\">◉</td>")
				elif res is 0:
					print("<td>✕</td>")
				else:
					print("<td style=\"color:blue;font-weight:bold\">▲</td>")
				probRow = probCur.fetchone()
			print("</tr>")
			userRow = userCur.fetchone()
		print("</table>")

	except MySQLdb.Error, e: 
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)
	db.close()
