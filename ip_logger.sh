#!/bin/bash

while true; do
    echo "Loggin IP to gdrive [$(date)]"
    ip route > /tmp/current_ip.txt
    rclone copy /tmp/current_ip.txt gdrive:/CaptivePortalIP/
    echo "[$(date)] New IP uploaded to Google Drive."
    sleep 300
done