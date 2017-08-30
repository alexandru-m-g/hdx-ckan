#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
PARSER:
--------

Parses specific fields in the WFP dataset,
converting them to the correct format.

'''
def _to_int(value):
    '''
    Converts value to integer.

    '''
    if value is not None:
        return int(value)

def parse(record):
    '''
    Parses certain data types into the
    expected ones.

    '''
    to_float = ['ADM0_CODE', 'ADM1_CODE', 'ADM2_CODE', 'ADM3_CODE']
    output = { k:(_to_int(v) if k in to_float else v) for k,v in record.items() }

    return output
