#!/bin/bash

rm -rf /tmp/usr/local/share/skyline

mkdir -p /tmp/usr/local/share/skyline

cp -r . /tmp/usr/local/share/skyline/

fpm -n skyline -t deb -s dir -v $1 -C /tmp usr/local/share/skyline
