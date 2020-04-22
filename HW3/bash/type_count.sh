#!/usr/bin/env bash
awk '{a[substr($6,2)] = a[substr($6,2)] + 1}END{for(key in a)print key, a[key]}' $1
