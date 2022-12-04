#!/usr/bin/python3
""" Filter states by user input """

from sys import argv
import MySQLdb


if __name__ == '__main__':
    user, password, database, state = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=user, passwd=password, db=database)
    db = db.cursor()
    db.execute("""SELECT * FROM states
    WHERE name LIKE BINARY '{}' ORDER BY id"""
               .format(state))
    r = db.fetchall()
    for i in r:
        print(i)
