#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","kandula123","nodejs" )
name="eswaar"
last="kandula"
phone="9550621821"
# prepare a cursor object using cursor() method
cursor = db.cursor()
cursor.execute("""INSERT INTO table1 VALUES (%s,%s,%s)""",(name,last,phone))



# disconnect from server
db.close()