echo $1
echo " "
echo '||| OSNAP Daemon Tool |||'
echo " "

# this tool will download, configure, and install Postgres 2.9.x and Apache httpd 2.4.25

echo 'Tool will download, configure and install PostgreSQL 9.5.x and Apache httpd 2.4.25'

echo 'Downloading Postgres'
git clone https://github.com/postgres/postgres.git

echo 'DONE'

echo 'Configuring Postgres'
cd postgres
./configure --prefix=$1

echo 'Preparing Postgres'
make

echo 'Installing Postgres'
make install

echo 'Switching to 9.5.x'

git branch -r

git checkout -b REL9_5_STABLE origin/REL9_5_STABLE

echo 'Configuring 9.5.x'
cd postgres
./configure --prefix=$1

echo 'Preparing 9.5.x'
make

echo 'Installing 9.5.x'
make install

cd ..
echo 'DONE'



echo 'Downloading Apache httpd'
curl -# -O https://www-eu.apache.org/dist//httpd/httpd-2.4.25.tar.bz2

echo 'Unpacking Apache...'
tar -xjf httpd-2.4.25.tar.bz2

echo 'DONE'

echo 'Configuring Apache...'
cd httpd-2.4.25
./configure --prefix=$1

echo 'Preparing Apache...'
make

echo 'Installing Apache'
make install

echo 'DONE'
echo ' '
echo '||| OSNAP Daemon Tool Complete |||'
