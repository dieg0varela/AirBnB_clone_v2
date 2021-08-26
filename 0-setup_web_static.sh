#!/usr/bin/env bash
# Script that configure the deployment of hbnb
apt update -y
apt install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
printf %s "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/server_name _/a \        location /hbnb_static/ {\n      alias /data/web_static/current/;\n      autoindex on;\n }\n" /etc/nginx/sites-available/default
service nginx restart
exit 0
