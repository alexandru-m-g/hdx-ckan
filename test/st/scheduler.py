#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import schedule

import collect
from collector.utilities.item import item

def wrapper():
  '''Wrapper for main program.'''

  collect.main()


schedule.every(12).hours.do(wrapper)

def main(verbose=True):
  '''
  Wrapper to run all the scheduled tasks.

  '''

  if verbose:
    print('%s Running scheduler.' % item('bullet'))

  try:
    while True:
      schedule.run_pending()
      time.sleep(1)

  except Exception as e:
    print(e)
    return False


if __name__ == '__main__':
  main()
