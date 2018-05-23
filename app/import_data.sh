#!/usr/bin/env bash

mongoimport --host mongodb_database --port 27017 -d test -c crimes --type csv --file /tmp/Chicago_Crimes_2001_to_2004.csv --headerline
rm /tmp/crimes.zip