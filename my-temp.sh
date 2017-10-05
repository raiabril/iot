#!/bin/bash
cpu=$(</sys/class/thermal/thermal_zone0/temp)
echo "                                       "
echo "$(hostname)@$(hostname -I)"
echo "$(date)"
echo "---------------------------------------"
echo "GPU $(/opt/vc/bin/vcgencmd measure_temp)"
echo "CPU temp=$((cpu/1000))'C"

