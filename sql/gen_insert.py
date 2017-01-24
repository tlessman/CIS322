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

with open ("osnap_legacy/convoys.csv", "r") as f:
    reader = csv.reader(f)
    columns = next(reader)
    query = 'insert into convoys({0}) values ({1})'
    query = query.format(','.join(columns), ','.join('?' * len(columns)))
    for data in reader:
        cursor.execute(query, data)
    cursor.commit()
