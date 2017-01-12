#!/bin/bash

echo '||| OSNAP Daemon Tool |||';
echo 'This tool will clone Postgres 2.9.x, then build and install Postgres.';
echo 'It will also download, build and install Apache httpd 2.4.25 with mod_wsgi.';
echo 'Cloning Postgres from GitHub...';
git clone https://github.com/postgres/postgres.git;
echo 'DONE';
echo 'Downloading Apache httpd...';
curl -O https://www-eu.apache.org/dist//httpd/httpd-2.4.25.tar.bz2;
echo 'DONE';
