#!/usr/bin/env bash
sort -nrk10 $1 | awk '{print $1, $4, $5, substr($6,2), $7, $10}' | uniq | head
