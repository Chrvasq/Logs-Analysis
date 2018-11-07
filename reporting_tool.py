#!/usr/bin/env python

import psycopg2

DBNAME = 'news'


def top_three():
    print('\n')
    print('Processing first report...\n')

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    c.execute("select title, count(*) as num from articles join log on log.path like concat('%', articles.slug) group by articles.title order by num desc limit 3")
    results = c.fetchall()
    db.close()

    print('Top three articles of all time: \n')

    for item in results:
        print('\"{}\" - {} views'.format(item[0], item[1]))

    print('\n')


def popular_article_authors():
    print('Processing second report...\n')

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    c.execute("select name, sum(article_views.num) as total_views from authors join (select articles.author as author, title, count(*) as num from articles join log on log.path like concat('%', articles.slug) group by articles.author, articles.title order by num desc) as article_views on authors.id = article_views.author group by authors.name order by total_views desc;")
    results = c.fetchall()
    db.close()

    print('Article authors ranked by views: \n')

    for item in results:
        print('{} - {} views'.format(item[0], item[1]))

    print('\n')


if __name__ == '__main__':
    top_three()
    popular_article_authors()