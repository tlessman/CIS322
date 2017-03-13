#cur.copy_to(export/export_data.csv, 'users', sep=",")
#cur.copy_from(import/import_data.csv, 'users')

import psycopg2
import csv
import sys

#database connection setup
conn = psycopg2.connect( dbname = sys.argv[1], host = '127.0.0.1', port = 5432)
cur = conn.cursor()

#cur.execute("CREATE TABLE asset_report (asset_tag varchar(16), description varchar(64), facility_fk integer, acquired_dt timestamp, disposed boolean, disposed_dt timestamp);")
#conn.commit()

cur.execute("SELECT asset_tag, description, facility_fk, acquired_dt, disposed, disposed_dt INTO asset_report FROM assets JOIN asset_at ON assets.asset_pk = asset_at.asset_fk;")
conn.commit()

#cur.execute("CREATE TABLE transfers (asset_tag varchar(16), req_user_fk integer, request_dt timestamp, app_user_fk integer, approved_dt timestamp, src_fk integer, dest_fk integer, load_dt timestamp, unload_dt timestamp);")
#conn.commit()

cur.execute("SELECT asset_tag, req_user_fk, request_dt, app_user_fk, approved_dt, src_fk, dest_fk INTO transfers FROM request JOIN assets ON assets.asset_pk = request.asset_fk JOIN transit ON transit.src_fk = request.src_fk;")
conn.commit()

SQL = "COPY users(username, password, role, active) TO stdout WITH CSV HEADER DELIMITER as ','"
with open('./export/users.csv', 'w') as f:
    cur.copy_expert(sql = SQL,  file = f)
    conn.commit()

SQL = "COPY facilities(fcode) TO stdout WITH CSV HEADER DELIMITER as ','"
with open('./export/facilities.csv', 'w') as f:
    cur.copy_expert(sql = SQL,  file = f)
    conn.commit()

SQL = "COPY asset_status(asset_tag, description, facility, acquired_dt, disposed, disposed_dt) TO stdout WITH CSV HEADER DELIMITER as ','"
with open('./export/assets.csv', 'w') as f:
    cur.copy_expert(sql = SQL,  file = f)
    conn.commit()   

SQL = "COPY transfers(asset_tag, requester, request_dt, approve_dt, src, dest, load_dt, unload_dt) TO stdout WITH CSV HEADER DELIMITER as ','"
with open('./export/transfers.csv', 'w') as f:
    cur.copy_expert(sql = SQL,  file = f)
    conn.commit()
    

#SQL = "COPY * TO stdout WITH CSV HEADER DELIMITER as ','"
#with open(sys.argv[2], 'w') as f:
#    cur.copy_expert(sql = SQL,  file = f)
#    conn.commit()

cur.close()
