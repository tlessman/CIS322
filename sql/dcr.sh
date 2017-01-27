
dropdb lost
createdb lost
psql lost -f create_tables.sql
bash import_data.sh lost 5432
