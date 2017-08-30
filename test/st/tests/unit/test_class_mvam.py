#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for the mVAM class.

'''
import unittest

from collector.classes.mvam import mVAM

class TestClassmVAM(unittest.TestCase):
    '''
    Perform tests on the mVAM class.

    '''
    def test_mvam_metadata_is_dictionary(self):
        '''
        mVAM().metadata is a dictionary.

        '''
        result = mVAM().metadata
        self.assertIs(type(result), dict)

    def test_mvam_query_returns_a_list(self):
        '''
        mVAM().query() returns a list of results.

        '''
        result = mVAM().query()
        self.assertIs(type(result), list)

        result = mVAM().query(statement="ADM0_NAME='Yemen' AND VARIABLE='FCS' AND MEAN < 40")
        self.assertIs(type(result), list)

    def test_mvam_raises_error_if_wrong_table_provided(self):
        '''
        mVAM().query() raises error if incorrect table requested.

        '''
        with self.assertRaises(ValueError):
            mVAM(table='foo').query()

