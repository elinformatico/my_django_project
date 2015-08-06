virtualenv env -p python3

sudo pip install virtualenvwrapper

Agregar en el archivo ~/.bashrc y agregar lo siguiente al final
Ejecutar:
source ~/.bashrc

mkvirtualenv --version

workon test         <---- Activate a enviroment
mkvirtualenv test   <---- Create a enviroment
rmvirtualenv test   <---- Remove a enviroment

pip install -r requirements.txt

START PYTHON PROJECT
-------------------------------
django-admin startproject fifa
cd fifa
python manage.py startapp soccer
In the file: setting.py add in INSTALLED_APPS the soccer APP
edit file: soccer/models.py

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

workon fifa

API Documentation
http://www.django-rest-framework.org/api-guide/settings/


Python SHELL
from soccer.models import Player, Team


Execute Queries:
https://docs.djangoproject.com/en/1.8/topics/db/queries/

