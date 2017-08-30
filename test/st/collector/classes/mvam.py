#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
MVAM CLASS:
---------------

Defines mVAM class as a representation of the
mVAM public API.

'''
import requests
import datetime

from collector.utilities.item import item

class mVAM:
    '''
    mVAM class; represents the organization's public API.

    '''
    def __init__(self, table='pblStatsSum', page_limit = 10*4):
        self.tables = ['pblStatsSum', 'pblStatsSum4Maps']
        if table not in self.tables:
            raise ValueError('Table %s does not exist.')

        self.table = table
        self.page_limit = page_limit
        self.metadata = {
            'url': 'http://vam.wfp.org/mvam_monitoring/api.aspx',
            'time': datetime.datetime.now().isoformat(),
            'table': table,
            'records': 0
        }

    def query(self, statement=None):
        '''
        Makes a query to the mVAM API.

        '''
        if statement is None:
            print('%s No statement provided. Fetching all available records.' % item('warn'))

        results = []
        if statement:
            for page in range(0, self.page_limit):
                print('%s Collecting %s page %s' % (item('bullet'), self.table, page) )
                r = requests.post(self.metadata['url'], data = {'table': self.table, 'where': statement, 'page': page })
                if len(r.json()) == 0:
                    break
                else:
                    results += r.json()

        else:
            for page in range(0, self.page_limit):
                print('%s Collecting %s page %s' % (item('bullet'), self.table, page) )
                r = requests.post(self.metadata['url'], data = {'table': self.table, 'page': page })
                if len(r.json()) == 0:
                    break
                else:
                    results += r.json()

        self.metadata['records'] = len(results)
        return(results)
