#!/usr/bin/python3

"""
script that takes four arguments and
all values where name matches the 4th argument
"""
import sys
import MySQLdb

def main(argv):
    """display values that matches the 4th argument"""
    db = MySQLdb.connect(host="localhost",port=3306, user=argv[1], 
                          password=argv[2], db=argv[3],searched=argv[4])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}%'\ 
                ORDER BY id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) == 5:
        main(sys.argv)
