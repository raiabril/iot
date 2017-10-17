#!/bin/bash
export PATH="/usr/local/lib/google-cloud-sdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games"
# Comment added yes
bq load --skip_leading_rows=1 cpb100-173514:gas_stations.Spain $(ls /media/pi/RAI/logs/gasolineras/*.csv | tail -1)
