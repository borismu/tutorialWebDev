sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
cd web 
gunicorn hello:app -c='/home/box/web/etc/hello.py' & 
cd ask
gunicorn ask.wsgi:application -b=0.0.0.0:8000 &

sudo /etc/init.d/mysql start
mysql -u root -e "create database askdata character set utf8"
mysql -u root -e "create user 'askuser' identified by '123'"
mysql -u root -e "GRANT ALL ON askdata.* TO 'askuser'"
python manage.py syncdb