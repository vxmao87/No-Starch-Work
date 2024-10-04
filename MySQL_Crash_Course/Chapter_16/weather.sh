#!/bin/bash
cd <FILEPATH>

if [ ! -f weather.csv ]; then
    exit 0
fi

mysql --local_infile=1 -h 127.0.0.1 -D weather -u <USERNAME> -p<PASSWORD> -s \
	< load_weather.sql > load_weather.log

if [ ! -s load_weather.log ]; then
    mysql -h 127.0.0.1 -D weather -u <USERNAME> -p<PASSWORD> -s < copy_weather.sql > copy_weather.log
fi

mv weather.csv weather.csv.$(date +%Y%m%d%H%M%S)