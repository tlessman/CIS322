#gen_insert // python script using psychopg to execute sql commands to read, clean and insert data from csv to lost db

dbname 5432

import psycopg2
import csv
import sys

ifile open("osnap_legacy/convoys.csv", "rb")
reader = csv.reader(ifile)


