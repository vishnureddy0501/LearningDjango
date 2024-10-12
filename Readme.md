start the mongodb service:
---------------------------
sudo systemctl start mongod  # For Ubuntu and other Linux systems

check the status of mongodb service:
-------------------------------------
sudo systemctl status mongod

Run the server:
---------------
# make sure mongodb is started and running
python3 manage.py runserver


install python 3.8.10

pip installation:
----------------
sudo apt-get install python3-pip

pymongo installation:
---------------------
sudo apt-get install python3-pymongo

checking pip version:
----------------------
python3 -m pip --version

Django installation:
-------------------
sudo apt update (updating ubuntu packages)
sudo apt install python3-django -y (installing django)
django-admin --version (checking django version)


(or)

pip3 install django

for creating a app
-------------------
python3 manage.py startapp deals (deals is a separate module. we can keep all the code related to deals separately)


for resolving atlas errors:
---------------------------
pip3 install dnspython


for resolving unapplied migration(s):
------------------------------------
python manage.py migrate

creating a django app: (we can have so many apps in django project)
-------------------------------------------------------------------
django-admin startproject project_name

check django version:
--------------------
python3 -m django --version

check python version:
--------------------
python3 --version
