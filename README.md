# CalipsoPlus Backend

The aim of this project is to provide a backend RESTful service for  CalipsoPlus JRA2 Demonstrator project.

### Contents

*  [Architecture](#Architecture)
    *  [Additional components](#Additional-components)
        *  [Guacamole](#Guacamole)
        *  [Umbrella](#Umbrella)
    *  [Versions and major dependencies](#Versions-and-major-dependencies)
*  [Requirements](#Requirements)
*  [Build & Development](#Build-&-Development)
    *  [Database configuration](#Database-configuration)
    *  [Migrate](#Migrate)
    *  [Run](#Run)
*  [Testing](#Testing)
*  [Deploy](#Deploy)
    *  [Configure uswgi](#Configure-uswgi)
    *  [Restart the service](#Restart-the-service)
*  [API](#API)

## Architecture

This backend is built using the [Django](https://www.djangoproject.com/) and [Django REST](https://www.django-rest-framework.org/) frameworks, running over Python 3.6 (Python 3.7 and higher should also be supported). You can refer to the documentation of the respective frameworks for more information.

Additionally, this application is configured to use a MySQL database (versions 5.6 and higher are supported). Other database backends are also supported by the Django framework (PostgreSQL, Oracle, SQLite), but require changes in the settings of the application. Check the relevant [Django documentation](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#database-setup) for further details.

### Additional components
#### Guacamole
To connect with the resources (Docker containers, virtual machines...) requisitioned by the application users, this application interfaces with an [Apache Guacamole](https://guacamole.apache.org/) service, which provides VNC or RDP connections through HTTP.

#### Umbrella

In addition to local authentication schemes implemented in each facility, this application is also designed to provide access via the [Umbrella](https://umbrellaid.org/) federated authentication service.

(TODO: Shibboleth)

### Versions and major dependencies

(TODO: do it or skip it? They can check the requirements.txt, maybe link to it? -> [requirements.txt](requirements.txt))

## Requirements

(TODO: detail specs, maybe use a table?)

For a minimal deployment of the backend segment of this application, the following resources are required:

*  An application server to host the Django backend (may also host the frontend application).
*  A database server.
*  A server running the Shibboleth identity provider (required to support the Umbrella federated authentication system).
*  A server running Guacamole (TODO: depending on usage, may share the application server? To check)
*  A server to use as host to the docker containers the users may requisition.

## Build & Development

The project has been developed in Python using Django Framework and the source code can be found in [CELLS' Git repository](https://git.cells.es/mis/calipsoplus-backend).

The user will need to install Python 3+, python-pip and python-virtualenv. Some other packages could be required.

```bash
mkdir calipsoplus & cd calipsoplus
mkdir logs
virtualenv ~/.virtualenvs/calipsoenv/bin/activate
git clone git@git.cells.es:mis/calipsoplus-backend.git -b develop backend
env/bin/pip install -r calipsoplus/requirements.txt
```

### Database configuration

By default, the application settings are configured to use MySQL database server, and we need a new schema to manage app's data, with the necessary user and host credentials to manage it. This document will follow default configuration settings.

```sql
CREATE DATABASE `calipsoplus`;
```

```bash
cd calipsoplus
mkdir config & cd config
mkdir database & cd database
vi guacamole.cnf #guacamole db
vi default.cnf #calipso db
```

Add the following content to the **default.cnf** file
```bash
[client]
database = calipsoplus
host = localhost
port = 3306
user = *****
password = *****
default-character-set = utf8
```
Add the following content to the **guacamole.cnf** file
```bash
[client]
database = guacamoledb
host = localhost
port = 3306
user = *****
password = *****
default-character-set = utf8
```

Set **default.cnf** and **guacamole.cnf** files as read only

```bash
chmod 555 default.cnf
chmod 555 guacamole.cnf
```

### Migrate
```
env/bin/python backend/manage.py migrate --settings=calipsoplus.settings_[local|test|demo|prod]
```

### Run

Once the environment and the database are configured...

```bash
./manage.py runserver 127.0.0.1:8000 settings=calipsoplus.settings_local
```

The service should be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Testing

The application has its own unit testing settings, which will create a mock database using SQLite and will store it in local memory. This way the testing is faster than using MySQL.

```bash
cd calipsoplus
source ~/.virtualenvs/calipsoenv/bin/activate
./manage.py test --settings=calipsoplus.settings_unittests
```

## Deploy

Follow the same steps as in the **Build & Development** section except the **Run** subsection

### Configure uswgi

Go to uwsgi's directory which contains the apps-available and apps-enabled directories. We will name it UWSGI_DIR.

First of all, review the calipsoplus-backend.ini file to be sure every property is set correctly.

After that, we need to edit the configuration file with correct environment configuration in terms of project location, Django's environment settings and database configuration.

### Configure Apache

Go to Apache's directory which contains the apps-available and apps-enabled directories. We will name it APACHE_DIR.

```bash
cd APACHE_DIR/apps-available
cp SOURCE_DIR/settings/config/apache/calipsoplus-backend.conf .
cd ../apps-enabled
ln -s ../apps-available/calipsoplus-backend.conf XX-calipsoplus-backend.conf
```

### Restart the service

```bash
sudo service apache2 restart
```


## API

(TODO: Link to external file? -> [API.md](API.md)) 