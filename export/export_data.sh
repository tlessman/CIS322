#!/bin/bash

echo $1 #lost
echo $2 #/export/export_data.csv
dbname=$1
output_dir=$2
python3 /export/export_data.py dbname output_dir
#cp /export/export_data.csv /import/import_data.csv
