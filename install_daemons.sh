echo " "
echo '||| OSNAP Daemon Tool |||'
echo " "
# this tool will download, configure, and install Postgres 2.9.x and Apache httpd 2.4.25
echo 'Tool is downloading assets...'
echo 'DOWNLOADING Postgres'
git clone https://github.com/postgres/postgres.git
echo 'DONE'
echo 'DOWNLOADING Apache httpd'
curl -# -O https://www-eu.apache.org/dist//httpd/httpd-2.4.25.tar.bz2
echo 'DONE'
ls -l

