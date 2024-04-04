#!/usr/bin/env bash
# install nginx and add new server block to the configuration

# check and install if nginx does not exist
if ! command -v nginx &> /dev/null; then
    echo "NGINX not installed. Installing now.."

    # installation of nginx
    apt-get -y update
    apt-get -y install nginx
    ufw allow 'Nginx HTTP'
    echo 'Hello World!' > /var/www/html/index.nginx-debian.html
    service nginx start

    echo "NGINX installation successfull"
else
    echo "NGINX already installed"
fi

test_dir="/data/web_static/releases/test/"
# check if directory exists otherwise create
if [ ! -d "$1" ]; then
    mkdir -p "$test_dir"
else
    echo "Directory '$1' already exists"
fi

# put simple text into index.html for testing
echo "\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# create symbolic link to folder /data/web_static/releases/test/
#+ if it doesn't exist
sym_link="/data/web_static/current"
linked_dir="/data/web_static/releases/test/"
if [ -d "$sym_link" ]; then
    rm -rf "$sym_link"
fi
ln -s "$linked_dir" "$sym_link"
echo "symbolic link created"

# give recursive ownership of /data/ to ubuntu and group
chown -R ubuntu:ubuntu /data/

sudo sed -i '/server_name _;/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-available/default

service nginx restart
