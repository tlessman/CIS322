#cur.copy_to(export/export_data.csv, 'users', sep=",")
#cur.copy_from(import/import_data.csv, 'users')

import psycopg2
import csv
import sys

#database connection setup
conn = psycopg2.connect( dbname = sys.argv[1], host = '127.0.0.1', port = 5432)
cur = conn.cursor()

SQL = "COPY users TO stdout WITH CSV HEADER DELIMITER as ','"
with open(sys.argv[2], 'w') as f:
    cur.copy_expert(sql = SQL,  file = f)
    conn.commit()
    cur.close()
