### HDX mVAM Collector
Collector for [WFP mVAM's API](http://vam.wfp.org/mvam_monitoring/mvamapi.aspx). This collector queries both available tables (`pblStatsSum` and `pblStatsSum4Maps`), paginates through all the available results, stores data in a local CSV file and SQLite database, and pushes those data into their respective resources on the [Humanitarian Data Exchange](https://data.hdx.rwlabs.org/dataset/mvam-food-security-monitoring-databank) platform.

[![Build Status](https://travis-ci.org/luiscape/hdxscraper-wfp-mvam.svg?branch=master)](https://travis-ci.org/luiscape/hdxscraper-wfp-mvam)


#### Usage
Clone this repository and navigate to its folder. Then the `Makefile` instructions:

```
$ make setup && make test
$ make collect && make register
```
The above should collect all available data and register the results on HDX. The environment variable `HDX_KEY` will need to be setup -- and the key will need access to the respective resources on HDX (`91c78d24-eab3-40b5-ba91-6b29bcda7178` and `748b40dd-7bd3-40a3-941b-e76f0bfbe0eb`).
