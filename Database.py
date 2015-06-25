__author__ = 'dimage01'

import MySQLdb

#connect DB

db = MySQLdb.connect("localhost","root","dimage","admage")

cursor = db.cursor()
# execute SQL query using execute() method.
cursor.execute("SELECT * FROM user")


# Fetch a single row using fetchone() method.
data = cursor.fetchall()

#print "Database version : %s " % data

for row in data:
    print "name: ",row[4]
    print "id:"   ,row[5]


# disconnect from server
db.close()


