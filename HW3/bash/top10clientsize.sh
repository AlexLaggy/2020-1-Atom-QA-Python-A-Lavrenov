#!/usr/bin/env bash
sort -nrk10 $1 | awk '{if ($9 ~ /^4/) {print $1, substr($6,2), $7, $9, $10}}' | uniq | head
