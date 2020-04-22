#!/usr/bin/env bash
FILEPATH="${1:-..}"
FILE=$FILEPATH/"${2:-access.log}"
if [[ -f "$FILE" ]]; then
    echo "Total count:"
    ./request_count.sh $FILE
    echo ""
    echo "Count by types:"
    ./type_count.sh $FILE
    echo ""
    echo "Top 10 by size:"
    ./top10size.sh $FILE
    echo ""
    echo "Top 10 with client error:"
    ./top10client.sh $FILE
    echo ""
    echo "Top 10 with server error:"
    ./top10server.sh $FILE
else
    echo "Can't access to such file!"
    exit 1
fi
