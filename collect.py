#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
COLLECTOR:
---------
Script that wraps the complete application logic.
Here we query the WFP API and collect all available
data, storing the results in local CSV files.

'''
import scraperwiki

from collector.parser import parse
from collector.classes.mvam import mVAM
from collector.utilities.item import item
from collector.storage.csv import store_csv
from collector.storage.sqlite import store_sqlite

def main():
    '''
    Program wrapper.

    '''
    tables = ['pblStatsSum', 'pblStatsSum4Maps']
    for t in tables:
        m = mVAM(table=t)

        output = []
        records = m.query()
        for record in records:
            output.append(parse(record))

        store_csv(data=output, path='%s.csv' % t)
        store_sqlite(data=output, table=t)

if __name__ == '__main__':
  try:
    main()
    print('%s Successfully collected mVAM data.' % item('success'))
    scraperwiki.status('ok')

  except Exception as e:
    print('%s Failed to collected mVAM data.' % item('error'))
    print(e)
    scraperwiki.status('error', 'Failed to collect data.')
