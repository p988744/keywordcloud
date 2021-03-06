#!/usr/bin/env python
#-*- coding: utf8 -*-
import MySQLdb
import sys


def main(argumenst):
    conn = MySQLdb.connect(host="127.0.0.1", user="keywordcloud", passwd="keywordcloud", db="keywordcloud")
    conn.set_character_set('UTF8')
    c = conn.cursor()
    c.execute('SET NAMES UTF8;')
    c.execute('SET CHARACTER SET utf8;')
    c.execute('SET character_set_connection=utf8;')

    sql = "SELECT * FROM news_news WHERE pub_time < NOW() - INTERVAL 8 DAY ORDER BY pub_time;"
    c.execute(sql)
    for row in c.fetchall():
        print "deleting news topic 「%s」(%s)" % (row[1], row[5])

    conn.commit()

    sql = "DELETE FROM news_news WHERE pub_time < NOW() - INTERVAL 8 DAY;"
    c.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main(sys.argv[1:])
