sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
cd web 
gunicorn hello:app -c='/home/box/web/etc/hello.py' 
cd ask
gunicorn ask.wsgi:application -b=0.0.0.0:8000