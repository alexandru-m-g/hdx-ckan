#!/bin/bash

#
# Run tests with coverage.
#
source venv/bin/activate
nosetests --with-cov \
          --rednose \
          --no-byte-compile \
          --nologcapture \
          -v
