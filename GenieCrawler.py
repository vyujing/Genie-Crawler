#-*- encoding: utf-8 -*-
import GenieMemberRange as gm
import MySQLdb
import sys

if __name__ == "__main__":
	#ran = gm.getGenieRange()
	try:
		db = MySQLdb.connect("localhost","vyujing","yourpassword","vyujing" )
		
		global cur
		cur = db.cursor()
		#sql = "SELECT ID FROM articles ORDER BY ID DESC LIMIT 10"
		sql = ("INSERT INTO genie VALUES('%s', '%s', '%s', '%s', '%s', '%s', null)") % ('vyujing', 'Queen', 'Muse', 'Metallica', 'zisn', 'jamy')
		cur.execute(sql)
		db.commit()
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)
	db.close()
