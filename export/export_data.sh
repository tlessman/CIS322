#!/bin/bash

echo $1 #lost
echo $2 #/export/export_data.csv
dbname=$1
output_dir=$2
output_file=./$output_dir/export_data.csv
touch ./export/users.csv ./export/facilities.csv ./export/assets.csv ./export/transfers.csv
python3 ./export/export_data.py $dbname $output_file

