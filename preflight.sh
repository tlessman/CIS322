#!/bin/bash

echo $1 #lost
dbname=$1

if [ "$#" -ne 1 ]; then
	echo "Usage: ./preflight.sh [DBNAME]"
	exit;
fi

psql $dbname -f ./sql/create_tables.sql
cp -R src/* $HOME/wsgi


