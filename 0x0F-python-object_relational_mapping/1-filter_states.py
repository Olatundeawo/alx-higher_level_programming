#!/usr/bin/python3

"""
accepts 3 arguments
and lists all states with a name N as the beginning
"""

import sys
import MySQLdb


def main(argv):
    """list states with name starting with N"""
    db = MySQLdb.connect(host="locahost", port=3306, user=argv[1], password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute = ("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    pass
    cur.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        main(sys.argv)

