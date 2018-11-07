#! /usr/bin/env python3

import psycopg2

DBNAME = 'news'


def top_three():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    c.execute("select title, count(*) as num from articles join log on log.path like concat('%', articles.slug) group by articles.title order by num desc limit 3")
    results = c.fetchall()
    db.close()

    for item in results:
        print('\"{item[0]}\" - {item[1]} views'.format(item[0],item[1]))

if __name__ == '__main__':
    top_three()