****
LOST ASSET TRACKING

Theodore Lessman
CIS322 Assignment 3

$/preflight.sh
-handles preparing this for startup including creating tables and putting data into lost

$/src
load_db.sh
-shell script for preflight to run to populate database

app.py
-flask python script to handle web page connections
-currently configured without wsgi

lost.config.json
-raw config file data

config.py
-python script to parse json data in order to use for lost

$/src/templates/*
/login : front page - accepts username and begins session, connects to /filter
/filter : allows user to choose filter by date and/or location, connects to inventory or transit
/inventory : report page for assets at locations
/transit : report page for assets on convoys
/logout : logout page, links back to login

/dev : debug page for handling report testing



