echo $1
echo " "
echo '||| OSNAP Daemon Tool |||'
echo " "

# this tool will download, configure, and install Postgres 2.9.x and Apache httpd 2.4.25

echo 'Tool is downloading assets...'
echo 'DOWNLOADING Postgres'
git clone https://github.com/postgres/postgres.git
git branch -r
git checkout -b REL9_5_STABLE origin/REL9_5_STABLE
echo 'DONE'

echo 'Tool will configure and install PostgreSQL...'
echo 'CONFIGURING...'
cd postgres
./configure --prefix=$1
echo 'Preparing...'
make
echo 'Installing'
make install
cd ..
echo 'DONE'
echo ' '



echo 'DOWNLOADING Apache httpd'
curl -# -O https://www-eu.apache.org/dist//httpd/httpd-2.4.25.tar.bz2
echo 'UNPACKING...'
tar -xjf httpd-2.4.25.tar.bz2
echo 'DONE'
echo ' '

echo 'Tool will configure and install Apache...'
echo 'CONFIGURING...'
cd httpd-2.4.25
./configure --prefix=$1
echo 'Preparing...'
make
echo 'Installing'
make install
echo 'DONE'

