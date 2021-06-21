sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install python3-venv -y
python3 -m venv env
source env/bin/activate
ls
pip install django
pip install pillow
git clone https://github.com/deep3324/phoenix.git
ls
cd phoenix/
pip3 install gunicorn
sudo apt-get install nginx -y
gunicorn --bind 0.0.0.0:8000 PhOeniX.wsgi:application
gunicorn --bind 0.0.0.0:8000 PhOeNiX.wsgi:application
cd PhOeNiX/
sudo nano settings.py 
cd ..
gunicorn --bind 0.0.0.0:8000 PhOeNiX.wsgi:application
cd PhOeNiX/
sudo nano settings.py 
cd ..
gunicorn --bind 0.0.0.0:8000 PhOeNiX.wsgi:application
sudo apt-get install -y supervisor
cd /etc/supervisor/conf.d
sudo touch gunicorn.conf
sudo nano gunicorn.conf 
clear
sudo mkdir -p /var/log/gunicorn
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl status
sudo nano /etc/nginx/sites-available/django.conf
sudo ln /etc/nginx/sites-available/django.conf /etc/nginx/sites-enabled/
sudo nginx -t
sudo service nginx restart
cd /etc/nginx/sites-enabled/
source env/bin/activate
cd /etc/nginx/sites-enabled/
sudo nano django.conf
sudo nginx -t
sudo service nginx restart
sudo nano django.conf
sudo nginx -t
sudo service nginx restart
sudo nginx -t
sudo service nginx restart
sudo supervisorctl reload
sudo service nginx restart
sudo nginx -t
cd 
cd phoenix/
cd PhOeNiX/
sudo nano settings.py 
sudo supervisorctl reload
sudo service nginx restart
sudo nginx -t
sudo nano settings.py 
sudo supervisorctl reload
sudo service nginx restart
sudo nginx -t
exit
cd /etc/nginx/sites-enabled/
sudo nano django.conf 
sudo service nginx restart
sudo nginx -t
sudo supervisorctl reload
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python3-certbot-nginx
sudo systemctl reload nginx
sudo ufw allow ssh
sudo ufw enable 
sudo ufw allow 'Nginx Full'
sudo ufw delete allow 'Nginx HTTP'
sudo ufw status
sudo certbot --nginx -d phoenixnsec.in -d www.phoenixnsec.in
sudo certbot renew --dry-run
exit
cd /etc/nginx/sites-enabled/
sudo nano django.conf 
sudo systemctl restart nginx
sudo nano /etc/hosts
sudo nginx -t && sudo systemctl restart nginx
sudo nano django.conf 
systemctl reload nginx
sudo systemctl reload nginx
source phoenix/
source env/bin/activate
cd phoenix/
ls
cd PhoenixApp/
ls
cd migrations/
ls
cd
cd phoenix/
python3 manage.py makemigrations
cd PhoenixApp/
cd migrations/
rm 0001_initial.py 
cd ..
ls
rm db.sqlite3 
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
source env/bin/activate
cd phoenix/PhOeNiX/
cd static/
ls
cd js/
ls
cd ..
cd PhoenixApp/
ls
cd static/
ls
cd ..
cd PhOeNiX/
cd static/
ls
cd
sudo service nginx restart
sudo nginx -t
cd phoenix/
cd PhoenixApp/
cd templates/
ls
sudo nano blogs.html 
sudo nano blog.html 
sudo service nginx restart
sudo supervisorctl reload
sudo nginx-t
sudo nginx -t
source env/bin/activate
python manage.py dumpdata
cd phoenix/
python manage.py dumpdata
python manage.py shell
ls
cd PhoenixApp/
ls
cd templates/
ls
sudo nano events.html 
sudo service nginx restart
sudo supervisorctl reload
sudo nano events.html 
sudo service nginx restart
sudo supervisorctl reload
cs
cd
deactivate
source env/bin/activate
cd phoenix/PhoenixApp/templates/
ls
sudo nano result.html 
sudo service nginx restart
sudo supervisorctl reload
sudo nano result.html 
sudo service nginx restart
sudo supervisorctl reload
sudo service nginx restart
sudo nano result.html 
sudo service nginx restart
sudo supervisorctl reload
cd 
cd phoenix/PhoenixApp/
ls
sudo nano views.py 
pip install django-autoslug
source env/bin/activate
cd phoenix/PhoenixApp/
sudo nano models.py 
cd ..
python manage.py makemigrations
cd PhoenixApp/
sudo nano models.py 
cd ..
python manage.py makemigrations
python manage.py migrate
sudo service nginx restart
sudo service supervisorctl reload
sudo supervisorctl reload
source env/bin/activate
cd phoenix/
cd PhoenixApp/
sudo nano views.py 
cd templates/
sudo nano events.html 
sudo service nginx restart
cd ..
ls
python3 manage.py runserver
python3 manage.py makemigrations
python3 manage.py migrate
sudo service nginx restart
cd PhoenixApp/
sudo nano views.py 
sudo nano urls.py 
sudo supervisorctl reload
cd ..
cd PhOeNiX/
sudo nano settings.py 
sudo supervisorctl reload
sudo service nginx restart
cd ..
cd PhoenixApp/
sudo nano views.py 
sudo nano urls.py 
cd templates/
sudo nano events.html 
sudo nano artcraft.html 
sudo supervisorctl reload
sudo service nginx restart
cd /etc/nginx/
ls
cd conf.d/
ls
cd ..
sudo nano nginx.conf 
/usr/local/nginx/sbin/nginx -s reload
sudo service nginx reload
sudo systemctl reload nginx.service
cd
source phoenix/PhoenixApp/templates/
source env/bin/activate
cd phoenix/PhoenixApp/templates/
sudo nano artcraft.html 
sudo systemctl reload nginx.service
sudo supervisorctl reload
sudo systemctl reload nginx.service
sudo supervisorctl reload
source env/bin/activate
sudo systemctl reload nginx.service
sudo supervisorctl reload
sudo systemctl reload nginx.service
sudo supervisorctl reload
sudo nano phoenix/PhoenixApp/urls.py 
sudo nano phoenix/PhoenixApp/views.py 
source env/bin/activate
cd phoenix/
ls
python3 manage.py makemigrations
python3 manage.py migrate
sudo systemctl nginx reload
sudo service nginx reload
sudo supervisorctl reload
cd PhoenixApp/
cd templates/
nano events.html 
sudo service nginx reload
sudo supervisorctl reload
nano quizomania.html 
sudo service nginx reload
sudo supervisorctl reload
nano quizomania.html 
cd ..
nano views.py 
sudo service nginx reload
sudo supervisorctl reload
nano views.py 
sudo service nginx reload
sudo supervisorctl reload
source env/bin/activate
cd phoenix/PhoenixApp/
cd templates/
nano quizomania.html 
