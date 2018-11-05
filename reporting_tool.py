#! /usr/bin/env python3

import psycopg2

DBNAME = 'news'


def top_three():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    c.execute("select path, count(*) from log where status = '200 OK' and path != '/' group by log.path;")
    results = c.fetchall()
    db.close()

    for article in results:
        print('{} -  {} views'.format(article[0], article[1]))

top_three()