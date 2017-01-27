This directory contains files required for LOST asset tracking database. After downloading and unpacking legacy data, starting webserver and initializing and creating database, run create_tables.sql. Then run import_data.sh with the db name and port as paramenters.



Files:
___create_tables.sql___
generates tables for db based on model in LOST documentation
use: psql [dbname] -f create_tables.sql

___import_data.sh___
runs gen_insert.py script to migrate data, and cleans up directory after migration is complete
use: bash import_data.sh [dbname] [port]

___gen_insert.py___
python script to migrate data. takes db name and port given in terminal to read, clean and migrate data from csv files following LOST model provided in documentation.

___README.txt___
thank you for reading me



Notes:

