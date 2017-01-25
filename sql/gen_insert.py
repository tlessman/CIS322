#gen_insert // python script using psychopg to execute sql commands to read, clean and insert data from csv to lost db

#dbname 5432

import psycopg2
import csv
import sys


#database connection setup
#conn = psycopg2.connect(dbname=sys.argv[1], host = '127.0.0.1', port = int(sys.argv[2]))
conn = psycopg2.connect( dbname = 'lost', host = '127.0.0.1', port = 5432)
cur = conn.cursor()

"""SECURITY TABLES"""

#migrate security compartments 
with open('osnap_legacy/security_compartments.csv', 'r') as f:
    csv_data = csv.reader(f)
    first_row = next(csv_data)
    for rows in csv_data:

        cur.execute("insert into compartments (abbrv, comment) values (%s, %s);", rows)


#migrate security levels 
with open('osnap_legacy/security_levels.csv', 'r') as f:
    csv_data = csv.reader(f)
    first_row = next(csv_data)
    for rows in csv_data:

        cur.execute("insert into levels (abbrv, comment) values (%s, %s);", rows)

#generate security tags





"""ASSET TABLES"""

#access file products 
with open('osnap_legacy/product_list.csv', 'r') as f:
    csv_data = csv.DictReader(f)

    for rows in csv_data:
        t = (rows["vendor"], rows["name"], rows["model"])
 
        cur.execute("insert into products(vendor, description, alt_description) values (%s, %s, %s);", t)


#access files assets 
with open('osnap_legacy/DC_inventory.csv', 'r') as fa:
    with open('osnap_legacy/HQ_inventory.csv', 'r') as fb:
        with open('osnap_legacy/MB005_inventory.csv', 'r') as fc:
            with open('osnap_legacy/NC_inventory.csv', 'r') as fd:
                with open('osnap_legacy/SPNV_inventory.csv', 'r') as fe: 
                    csv_data = csv.DictReader(fe)
                    #v = cur.execute("select product_fk from products where products_pk is not null")
                    for rows in csv_data:
                        t = (rows["asset tag"], rows["product"])
                        cur.execute("insert into assets(asset_tag, description) values (%s, %s);", t)
                csv_data = csv.DictReader(fd)
                #v = cur.execute("select product_fk from products where products_pk is not null")
                for rows in csv_data:
                    t = (rows["asset tag"], rows["product"])
                    cur.execute("insert into assets(asset_tag, description) values (%s, %s);", t)
            csv_data = csv.DictReader(fc)
            #v = cur.execute("select product_fk from products where products_pk is not null")
            for rows in csv_data:
                t = (rows["asset tag"], rows["product"])
                cur.execute("insert into assets(asset_tag, description) values (%s, %s);", t)
        csv_data = csv.DictReader(fb)
        #v = cur.execute("select product_fk from products where products_pk is not null")
        for rows in csv_data:
            t = (rows["asset tag"], rows["product"])
            cur.execute("insert into assets(asset_tag, description) values (%s, %s);", t)
    csv_data = csv.DictReader(fa)
    #v = cur.execute("select product_fk from products where products_pk is not null")
    for rows in csv_data:
        t = (rows["asset tag"], rows["product"])
        cur.execute("insert into assets(asset_tag, description) values (%s, %s);", t)

#facilities
with open('osnap_legacy/'



#select product_pk from products 



"""USER TABLES"""




conn.commit()
