apachectl start
initdb lost
pg_ctl -D lost -l logfile start
createdb lost
