#!/usr/bin/env bash

ip_addr=$(ip -o address show dev wlan0 \
   | grep -v inet6 \
   | awk '{print $4}' \
   | cut -d / -f 1)

cd gpio_rest_controller

gunicorn --bind $ip_addr:8000 wsgi
