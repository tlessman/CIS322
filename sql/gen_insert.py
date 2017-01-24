#gen_insert // python script using psychopg to execute sql commands to read, clean and insert data from csv to lost db

#dbname 5432

import psycopg2
import csv
import sys


#database connection setup
#conn = psycopg2.connect(dbname=sys.argv[1], host = '127.0.0.1', port = int(sys.argv[2]))
conn = psycopg2.connect( dbname = 'lost', host = '127.0.0.1', port = 5432)
cur = conn.cursor()

#access file compartments
with open('osnap_legacy/security_compartments.csv', 'r') as f:
    csv_data = csv.reader(f)
    first_row = next(csv_data)
    for rows in csv_data:
        print(rows)
        cur.execute("insert into compartments (abbrv, comment) values (%s, %s);", rows)

#insert into compartments (abbrv, comment) values ($V1, $V2);
conn.commit()

#access file levels 
with open('osnap_legacy/security_levels.csv', 'r') as f:
    csv_data = csv.reader(f)
    first_row = next(csv_data)
    for rows in csv_data:
        print(rows)
        cur.execute("insert into levels (abbrv, comment) values (%s, %s);", rows)

#insert into compartments (abbrv, comment) values ($V1, $V2);
conn.commit()


#access file products 
with open('osnap_legacy/product_list.csv', 'r') as f:
    csv_data = csv.DictReader(f)

    for rows in csv_data:
        t = (rows["vendor"], rows["name"], rows["model"])
 
        cur.execute("insert into products(vendor, description, alt_description) values (%s, %s, %s);", t)

#insert into compartments (abbrv, comment) values ($V1, $V2);
conn.commit()

#access asset files 
with open('osnap_legacy/DC_inventory.csv', 'r') as f:
    csv_data = csv.DictReader(f)
    #v = cur.execute("select product_fk from products where products_pk is not null")
    for rows in csv_data:
        t = (v["product_fk"], rows["asset_tag"], rows["product"])
 
        cur.execute("insert into products(vendor, description, alt_description) values (%s, %s, %s);", t)

#insert into compartments (abbrv, comment) values ($V1, $V2);
conn.commit()
