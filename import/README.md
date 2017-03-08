LOST
Import Data

In this directory:
* import_data.sh
	Shell script that takes csv from given file and inserts it into corresponding tables in database.
	USAGE: bash $REPO/import/import_data.sh [dbname] [output_dir]
* import_data.py
	Needed for export_data.sh. Uses psycopg2 to copy data to database tables from separate .csv files, initially grouped in export_data.csv.

Needed before transfer:
* import_data.csv (or another .csv)
* database with the following tables:
	-assets
	-facilities
	-transfers(transit, request)
	-users

Created by this script:
* assets.csv
* facilities.csv
* tranfers.csv
* users.csv
 
	


