#!/bin/bash

echo $1 #lost
#echo $2 #5432
dbname=$1
#port=$2

dropdb $dbname
createdb $dbname
psql $dbname -f ./sql/create_tables.sql
cp -R src/* $HOME/wsgi


