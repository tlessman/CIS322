LOST
Export Data

In this directory:
* export_data.sh
	Shell script that takes data from LOST database, then puts it into a csv format.
	USAGE: bash $REPO/export/export_data.sh [dbname] [output_dir]
* export_data.py
	Needed for export_data.sh. Uses psycopg2 to copy data from database tables into separate .csv files, then groups each file into export_data.csv.

Created by this script:
* assets.csv
* facilities.csv
* tranfers.csv
* users.csv
* export_data.csv
	A collection of individual table .csv files in single document.


