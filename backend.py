#!/usr/bin/python
import MySQLdb

passFile = open("password.txt","r") #opens file

def dbConnect():
    '''
    Connects to root database

    NOTE: Make sure to use db.close() after usage!

    Args: None
    Returns: database link 'db'
       * db.cursor() : returns cursor to point to data
          * cur.execute(<SQL in string here>)

    For complete MySQLdb Python Module Documentation:
         http://www.mikusa.com/python-mysql-docs/index.html
    '''

    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd=passFile.read(),     # your password
                         db="GeorgiaWorks")  # name of the data base
    return db
