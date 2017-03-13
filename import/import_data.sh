#!/bin/bash

echo $1 #lost
echo $2 #/import/import_data.csv
dbname=$1
input_dir=$2
touch ./$input_dir/users.csv ./$input_dir/facilities.csv ./$input_dir/assets.csv ./$input_dir/transfers.csv
python3 ./$input_dir/import_data.py $dbname
