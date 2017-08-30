#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
REGISTER:
--------

Creates a DataStore in HDX based on specific
-- hard-coded -- id and schema.

'''
import os
import csv
import ckanapi

API_KEY = os.getenv('HDX_KEY', None)

resources = [
    {
        'resource_id': '91c78d24-eab3-40b5-ba91-6b29bcda7178',
        'path': 'pblStatsSum.csv',
        'schema': {
            "fields": [
              { 'id': 'ADM0_NAME', 'type': 'text' },
              { 'id': 'SvyMonthNum', 'type': 'text' },
              { 'id': 'RowNum', 'type': 'text' },
              { 'id': 'ADM2_NAME', 'type': 'text' },
              { 'id': 'IndpVars', 'type': 'text' },
              { 'id': 'AdminStrata', 'type': 'text' },
              { 'id': 'SvyMonth', 'type': 'text' },
              { 'id': 'SvyID', 'type': 'text' },
              { 'id': 'Mean', 'type': 'text' },
              { 'id': 'Demographic', 'type': 'text' },
              { 'id': 'HLAvg', 'type': 'text' },
              { 'id': 'Pctl5', 'type': 'text' },
              { 'id': 'CnfIntvLo', 'type': 'text' },
              { 'id': 'ADM1_NAME', 'type': 'text' },
              { 'id': 'NumObs', 'type': 'text' },
              { 'id': 'ADM0_CODE', 'type': 'int' },
              { 'id': 'PnlID', 'type': 'text' },
              { 'id': 'ID', 'type': 'text' },
              { 'id': 'StDev', 'type': 'text' },
              { 'id': 'SvyYear', 'type': 'text' },
              { 'id': 'Variable', 'type': 'text' },
              { 'id': 'Pctl25', 'type': 'text' },
              { 'id': 'Pctl75', 'type': 'text' },
              { 'id': 'Pctl95', 'type': 'text' },
              { 'id': 'Median', 'type': 'text' },
              { 'id': 'SvyDate', 'type': 'text' },
              { 'id': 'CnfIntvHi', 'type': 'text' }
            ]
        },
        'indexes': []
    },
    {
        'resource_id': '748b40dd-7bd3-40a3-941b-e76f0bfbe0eb',
        'path': 'pblStatsSum4Maps.csv',
        'schema': {
            "fields": [
              {'id': 'ADM0_NAME', 'type': 'text' },
              {'id': 'Mean', 'type': 'float8' },
              {'id': 'RowNum', 'type': 'text' },
              {'id': 'ADM3_NAME', 'type': 'text' },
              {'id': 'ADM2_NAME', 'type': 'text' },
              {'id': 'IndpVars', 'type': 'text' },
              {'id': 'AdminStrata', 'type': 'text' },
              {'id': 'SvyMonth', 'type': 'text' },
              {'id': 'SvyID', 'type': 'text' },
              {'id': 'SvyMonthNum', 'type': 'int' },
              {'id': 'Demographic', 'type': 'text' },
              {'id': 'HLAvg', 'type': 'float8' },
              {'id': 'Pctl5', 'type': 'text' },
              {'id': 'CnfIntvLo', 'type': 'float8' },
              {'id': 'SvyYear', 'type': 'int' },
              {'id': 'Median', 'type': 'float8' },
              {'id': 'NumObs', 'type': 'text' },
              {'id': 'ADM0_CODE', 'type': 'text' },
              {'id': 'PnlID', 'type': 'text' },
              {'id': 'ID', 'type': 'text' },
              {'id': 'ADM1_NAME', 'type': 'text' },
              {'id': 'Variable', 'type': 'text' },
              {'id': 'Pctl25', 'type': 'float8' },
              {'id': 'Pctl75', 'type': 'float8' },
              {'id': 'Pctl95', 'type': 'float8' },
              {'id': 'ADM1_CODE', 'type': 'text' },
              {'id': 'StDev', 'type': 'float8' },
              {'id': 'ADM3_CODE', 'type': 'text' },
              {'id': 'ADM2_CODE', 'type': 'text' },
              {'id': 'SvyDate', 'type': 'text' },
              {'id': 'CnfIntvHi', 'type': 'float8' }
            ]
        },
        'indexes': ['ADM0_CODE', 'ADM1_CODE', 'ADM2_CODE', 'ADM3_CODE', 'SvyYear', 'SvyMonthNum']
    }
]

def upload_data_to_datastore(ckan_resource_id, resource, apikey):
    if apikey is None:
      raise ValueError('No API key provided.')

    ckan = ckanapi.RemoteCKAN('http://data.hdx.rwlabs.org', apikey=API_KEY)

    try:
        ckan.action.datastore_delete(resource_id=ckan_resource_id, force=True, apikey=apikey)
    except:
        pass

    ckan.action.datastore_create(
            apikey=apikey,
            resource_id=ckan_resource_id,
            force=True,
            fields=resource['schema'].get('fields'),
            primary_key=resource['schema'].get('primary_key'),
            indexes=resource['indexes'])

    reader = csv.DictReader(open(resource['path']))
    #rows = [ row for row in reader ]
    rows = []
    for row in reader:
        new_elem = {key:value for key,value in row.items() if value != '' }
        rows.append(new_elem)
    chunksize = 5000
    offset = 0
    print('Uploading data for file: %s' % resource['path'])
    while offset < len(rows):
        rowset = rows[offset:offset+chunksize]
        ckan.action.datastore_upsert(
                resource_id=ckan_resource_id,
                force=True,
                method='insert',
                records=rowset)
        offset += chunksize
        complete = str(float(offset)/len(rows) * 100)[:3] + "%"
        print('Update successful: %s completed' % complete)


def main():
    print('-------------------------------------')

    for i in range(0,len(resources)):
        resource = resources[i]
        resource_id = resource['resource_id']
        print("Reading resource id: %s" % resource_id)
        upload_data_to_datastore(resource_id, resource, API_KEY)

    print('-------------------------------------')
    print('Done.')
    print('-------------------------------------')
