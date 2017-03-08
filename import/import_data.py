#cur.copy_to(export/export_data.csv, 'users', sep=",")
#cur.copy_from(import/import_data.csv, 'users')

import psycopg2
import csv
import sys

#database connection setup
conn = psycopg2.connect( dbname = sys.argv[1], host = '127.0.0.1', port = 5432)
cur = conn.cursor()

SQL = "COPY users(username, password, role, active) FROM stdin WITH CSV HEADER DELIMITER as ','"
with open('./import/users.csv', 'r') as f:
    cur.copy_expert(sql = SQL,  file = f)
    conn.commit()
    

SQL = "COPY facilities(fcode) FROM stdin WITH CSV HEADER DELIMITER as ','"
with open('./import/facilities.csv', 'r') as f:
    cur.copy_expert(sql = SQL,  file = f)
    conn.commit()
    

SQL = "COPY assets(asset_tag, description, facility, acquired, disposed) FROM stdin WITH CSV HEADER DELIMITER as ','"
with open('./import/assets.csv', 'r') as f:
    cur.copy_expert(sql = SQL,  file = f)
    conn.commit()
    

SQL = "COPY transit,request(asset_tag, requester, request_dt, approve_dt, src, dest, load_dt, unload_dt) FROM stdin WITH CSV HEADER DELIMITER as ','"
with open('./import/transfers.csv', 'r') as f:
    cur.copy_expert(sql = SQL,  file = f)
    conn.commit()
    

#SQL = "COPY * FROM stdin WITH CSV HEADER DELIMITER as ','"
#with open(sys.argv[2], 'w') as f:
#    cur.copy_expert(sql = SQL,  file = f)
#    conn.commit()

cur.close()
