#!/usr/bin/env python

import psycopg2
from datetime import datetime

DBNAME = 'news'


def open_conn():
    global db, c

    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        return [db, c]
    except:
        print('Unable to connect to database.')


def close_conn():
    db.close()
    print('End of report.\n')


def top_three():
    print('\nProcessing first report...\n')

    c.execute(
        "select title, count(*) as num from articles join log on"
        " log.path like concat('%', articles.slug) group by"
        " articles.title order by num desc limit 3"
        )
    results = c.fetchall()

    print('Top three articles of all time: \n')

    for item in results:
        print('\"{}\" - {} views'.format(item[0], item[1]))


def popular_article_authors():
    print('\nProcessing second report...\n')

    c.execute(
        "select name, sum(article_views.num) as total_views from authors join"
        "(select articles.author as author, title, count(*) as num from"
        " articles join log on log.path like concat('%', articles.slug) group"
        " by articles.author, articles.title) as article_views on authors.id ="
        " article_views.author group by authors.name order by total_views"
        " desc;"
        )
    results = c.fetchall()

    print('Article authors ranked by views: \n')

    for item in results:
        print('{} - {} views'.format(item[0], item[1]))


def error_report():
    print('\nProcessing third report...\n')

    c.execute(
        "select t3.time::date, t3.error_percentage from (select t1.time::date,"
        " (t1.total / t2.total) * 100 as error_percentage from (select"
        " a.time::date, sum(a.num) as total from (select status, time::date,"
        " count(*) as num from log where status != '200 OK' group by"
        " log.status, log.time::date) as a group by a.time::date) as t1"
        ", (select b.time::date, sum(b.num) as total from (select status"
        ", time::date, count(*) as num from log group by log.status"
        ", log.time::date) as b group by b.time::date) as t2 where"
        " t1.time = t2.time) as t3 where error_percentage > 1;"
        )
    results = c.fetchall()

    date = results[0][0]
    percent = round(results[0][1], 2)

    print('Failed Requests > 1%: \n')

    print(date.strftime('%B %d, %Y - ') + str(percent) + '% ' + 'errors\n')


if __name__ == '__main__':
    open_conn()
    top_three()
    popular_article_authors()
    error_report()
    close_conn()
