#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
STORE CSV:
----------

Defines mVAM class as a representation of the
mVAM public API.

'''
import csv

def store_csv(data=None, path=None):
    '''
    Stores a list of dictionaries as a CSV file.

    '''
    if data is None:
        raise ValueError('No data provided.')

    if path is None:
        raise ValueError('Please provide path.')

    with open(path, 'w') as csvfile:
        field_names = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=field_names)

        writer.writeheader()
        for row in data:
            writer.writerow(row)

    return True
