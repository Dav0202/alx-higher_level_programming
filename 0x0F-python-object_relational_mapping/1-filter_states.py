#!/usr/bin/python3
""" Filter states """

from sys import argv
import MySQLdb


if __name__ == '__main__':
    user, password, database = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=password, db=database)
    db = db.cursor()
    db.execute("""SELECT * FROM states
    WHERE REGEXP_LIKE(name, '^N', 'c') ORDER BY id""")
    r = db.fetchall()
    for i in r:
        print(i)
