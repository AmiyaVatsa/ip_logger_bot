#!/bin/bash

while true; do
    if ! ping -c 1 8.8.8.8 > /dev/null 2>&1; then
        echo "[$(date)] Internet is down. Attempting login..."
        sleep 5
        nmcli connection down "Guest@IISERB"
        sleep 3
        nmcli connection up "Guest@IISERB"
        sleep 5
        python3 ./login.py
        sleep 5
        if ping -c 1 8.8.8.8 > /dev/null 2>&1; then
            ip route > /tmp/current_ip.txt
            echo "Login Successful. [$(date)]" > ./login_success.log
            rclone copy /tmp/current_ip.txt gdrive:/CaptivePortalIP/
            echo "[$(date)] New IP uploaded to Google Drive."
        else
            echo "[$(date)] Login attempt failed. Still no internet."
        fi
    else
        echo "[$(date)] Internet is fine."
    fi
    sleep 300
done
