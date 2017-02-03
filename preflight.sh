
createdb lost
psql lost -f ./sql/create_tables.sql
#python3 ./sql/gen_insert.py
#lost 5432
psql lost -f ./src/load_db.sql



