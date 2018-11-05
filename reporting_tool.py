#! /usr/bin/env python3

import psycopg2

DBNAME = 'news'

db = psycopg2.connect(database=DBNAME)

