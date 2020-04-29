#!/usr/bin/env bash
FILEPATH="${1:-..}"
FILE=$FILEPATH/"${2:-access.log}"
LOGFILE="${3:-result.txt}"
if [[ -f "$LOGFILE" ]]; then
    rm $LOGFILE
fi
touch $LOGFILE
if [[ -f "$FILE" ]]; then
    #echo "Total count:"
    ./request_count.sh $FILE >> $LOGFILE
    #echo ""
    #echo "Count by types:"
    ./type_count.sh $FILE >> $LOGFILE
    #echo ""
    #echo "Top 10 by size:"
    ./top10size.sh $FILE >> $LOGFILE
    #echo ""
    #echo "Top 10 with client error:"
    ./top10client.sh $FILE >> $LOGFILE
    #echo ""
    #echo "Top 10 with server error:"
    ./top10clientsize.sh $FILE >> $LOGFILE
else
    echo "Can't access to such file!"
    exit 1
fi
