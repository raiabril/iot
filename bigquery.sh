#!/bin/bash

bq load --skip_leading_rows=1 cpb100-173514:gas_stations.Spain $(ls /home/pi/logs/gasolineras/*.csv | tail -1)
