#gen_insert // python script using psychopg to execute sql commands to read, clean and insert data from csv to lost db

#dbname 5432

import psycopg2
import csv
import sys


#database connection setup
#conn = psycopg2.connect(dbname=sys.argv[1], host = '127.0.0.1', port = int(sys.argv[2]))
conn = psycopg2.connect( dbname = 'lost', host = '127.0.0.1', port = 5432)
cur = conn.cursor()

#access file
csv_data = csv.reader("osnap_legacy/.security_compartments.csv")

rows = csv_data.split('\n')
first_row = next(csv_data)
for row in rows:
    cur.execute(insert into compartments (abbrv, comment);)

cur.commit()


