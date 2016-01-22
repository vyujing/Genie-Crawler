#-*- encoding: utf-8 -*-
import GenieMemberRange as gm
import GenieMemberArtist as ga
import MySQLdb
import sys

if __name__ == "__main__":
	
	ran = gm.getGenieRange()
	try:
		db = MySQLdb.connect("localhost","vyujing","vyujing","vyujing" )
		cur = db.cursor()
		cur.execute("set names utf8");
		#sql = "SELECT ID FROM articles ORDER BY ID DESC LIMIT 10"

		for i in range(int(ran[0]), int(ran[1])):
			res = ga.getArtist(i)
			print(res)
			if(res[0] is True):
				r = [0,0,0,0,0,0]
				for i in range(1,6):
					r[i] = res[i].replace("'", "").replace('"', "").replace('#', '').replace('--', '')
				if r[1] is "" and r[2] is "":
					continue
				print(r)
				sql = "INSERT INTO genie VALUES('%s', '%s', '%s', '%s', '%s', '%s', null)"% (str(i), r[1], r[2], r[3], r[4], r[5])
				print(sql)
				cur.execute(sql)
				db.commit()
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)
	db.close()
