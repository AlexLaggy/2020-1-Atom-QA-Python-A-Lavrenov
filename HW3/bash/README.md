# Tutorial for bash block

## General
To start all scripts run ./all_scripts.sh.
This script has a default params, such as a directory and a filename, but u can give it as bash params.
1st param is a directory, 2d param is a filename.

## Total count
For doing this task run ./request_count.sh.
In this task i used `wc -l`.

## Count by type
For doing this task run ./type_count.sh.
In this task i used multidimensional arrays of command `awk`. This script collects keys(`HEAD`, `GET`, `POST`, etc.) and increments it's values in the 2d dimension.

## Top 10 the biggest requests by size
For doing this task run ./top10size.sh.
In this task i used `awk` for printing result and `sort` with keys `-nkr10` to sort data by 10th column.

## Top 10 requests with client error
For doing this task run ./top10client.sh.
In this task i used multidimensional arrays of command `awk` for collect requests group by `ip`, `method`, `url`, `status code` and `number of iterations`. Also this script sorts status codes which starts with `4`.

## Top 10 requests with server error
For doing this task run ./top10server.sh.
Script looks like the previous, but it sorts status codes which starts with `5`.