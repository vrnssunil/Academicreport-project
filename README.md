# Academicreport-project
Academicreport on django
# Academicreport
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

# Prerequisites
 ### The following installations are required  for django      
   #### To install pip
        ** **cmd:sudo apt-get insatll python-pip
   #### To install python-dev , libmysqlclient-dev,mysqlserver
        ** **cmd:sudo apt install  python-dev libmysqlclient-dev mysqlserver
   #### To install virtualenv
        ** **cmd:sudo pip install virtualenv 
   #### Now we have to create virtualenv in our directory
        ** **cmd:virtualenv -p python venv
   #### we have to activate virtualenv by
        ** **cmd:source venv/bin/activate
   #### To import data from the github to  Aws
       ** ** cmd : git clone "https://github.com/bhanuchander008/Academicreport.git"
   #### Changing into curent directory
       ** **cmd:cd directoryname
  #### Installation packages to setup djangoproject in textfile
      ** **cmd:pip install -r requirements.txt
  
# DATABASE
   #### To enter into mysql prompt
        ** ** cmd:mysql -u root -p
   #### To create database
     ** ** cmd: create database databasename;
     ** ** cmd:use database; # To enter into our database
     ** ** cmd:show tables;  # To show tables in database
     ** ** cmd:select * from table tablename;# To see data in tables
  
   #### To create tables in database:
     ** **  cmd :python manage.py mkaemigrations
     ** **  cmd:python manage.py migrtae
 
 #### To push the data into database:
     ** **  cmd:python pythonfilename.py(python db.py)
     
  #### To check in the webserver
     ** ** cmd:python manage.py runserver

