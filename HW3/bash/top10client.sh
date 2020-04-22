#!/usr/bin/env bash
awk '{if ($9 ~ /^4/) {a[$1,substr($6,2),$7,$9] = a[$1,substr($6,2),$7,$9] + 1}}
END{for(comb in a) {split(comb,sep,SUBSEP); print sep[1], sep[2], sep[3], sep[4], a[sep[1],sep[2],sep[3],sep[4]]}}' $1 | sort -nrk5 | head
