#!/bin/bash

DB_USER='root';
DB_PASSWD='ADDPASS';

DB_NAME='mydb';
TABLE='gas';

INPUT_FILE="/media/pi/RAI/logs/gasolineras/gasolineras_2017-09-20_21-06.csv";

SQL="USE $DB_NAME; LOAD LOCAL DATA INFILE '$INPUT_FILE' INTO TABLE `$TABLE` COLUMNS TERMINATED BY ',' LINES TERMINATED BY '\n' CHARACTER SET utf8;"
mysql --user=$DB_USER --password=$DB_PASSWD --local-infile --default_character_set utf8 $DB_NAME --execute="$SQL"
