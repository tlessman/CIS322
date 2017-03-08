#!/bin/bash

echo $1 #lost
echo $2 #/import/import_data.csv
dbname=$1
input_dir=$2
touch ./import/users.csv ./import/facilities.csv ./import/assets.csv ./import/transfers.csv
python3 ./import/import_data.py $dbname $input_dir

