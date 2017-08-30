#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for storage functions.

'''
import unittest

from collector.storage.csv import store_csv

class TestStorageCSV(unittest.TestCase):
    '''
    Perform tests on the CSV storage functions.

    '''
    def test_csv_raises_errors_if_no_data_provided(self):
        '''
        store_csv() raises errors if no data or path are provided.

        '''
        with self.assertRaises(ValueError):
            store_csv(data=None)
            store_csv(path=None)
