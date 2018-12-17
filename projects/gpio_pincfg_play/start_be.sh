#!/usr/bin/env bash

ip_addr=$(ip -o address show dev wlan0 \
   | grep -v inet6 \
   | awk '{print $4}' \
   | cut -d / -f 1)

gunicorn --bind $ip_addr:8000 be.wsgi
