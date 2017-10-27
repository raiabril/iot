#!/bin/bash

for f in *;
do echo $f;
mysql -e "load data local infile '"$f"' into table customs fields TERMINATED BY ',' LINES TERMINATED BY '\n' ignore 1 LINES"  -u pi --password=ADDPASS --local-infile;
done
