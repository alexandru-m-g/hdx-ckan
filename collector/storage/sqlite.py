#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
SQLITE:
-------

Stores Python dictionaries as SQLite
records.

'''
import scraperwiki

from collector.utilities.item import item

def store_sqlite(data, table):
  '''
  Store records in a SQLite database.

  '''
  print('{bullet} Storing {n} records in database.'.format(bullet=item('bullet'), n=len(data)))

  # for record in data:
  scraperwiki.sqlite.save(data[0].keys(), data, table_name=table)
