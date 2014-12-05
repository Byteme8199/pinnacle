Ubuntu Server Setup Guide for Pinnacle Prospects
================================================

These instructions are modified from those found at epicserve_.

.. _epicserve: https://epicserve-docs.readthedocs.org/en/latest/django/ubuntu-server-django-guide.html

Step 1: Install Software
------------------------

Before you begin it might be a good idea to update your system clock::

    $ sudo ntpdate time.nist.gov

Download lists of new/upgradable packages::

    $ sudo aptitude update

SSH server was already installed on digitalocean (I think) otherwise

OpenSSH
~~~~~~

Since I like to connect to my servers using SSH the first thing I install is openssh-server::

    $ sudo aptitude install openssh-server

ssh should work to your server now (I really really hope you did this before disconnecting)


Python Header Files
~~~~~~~~~~~~~~~~~~

The Python header files are needed in order to compile binding libraries like ``psycopg2``. ::

    $ sudo aptitude install python2.7-dev

PostgreSQL
~~~~~~~~~

::
Might be up to version 9.3 or higher when you get back to this

    $ sudo aptitude install postgresql postgresql-server-dev-9.1

Make your Ubuntu user a PostgreSQL superuser::

    $ sudo su - postgres
    $ createuser --superuser <your username>
    $ exit

Restart PostgreSQL::

Old School
    $ sudo /etc/init.d/postgresql restart
New School
    $ sudo service postgresql restart


Nginx And Git
~~~~~~~~~~~

::

    $ sudo aptitude install nginx git



Step 2: Setup a Generic Deploy User
-----------------------------------

The reason we are setting up a generic deploy user is so that if you have multiple developers who are allowed to do deployments you can easily add the developer's SSH public key to the deploy user's ``/home/deploy/.ssh/authorized_keys`` file in order to allow them to do deployments.

::

    $ sudo useradd -d /home/deploy -m -s /bin/bash deploy


Step 3: Install Pinnacle Site
-------------------------------

Setup a virtualenv::

    $ sudo apt-get install python-setuptools
    $ sudo easy_install pip virtualenv
    $ cd /usr/local/
    $ sudo mkdir virtualenvs
    $ sudo chown deploy:deploy virtualenvs
    $ sudo su deploy
    $ cd virtualenvs
    $ virtualenv --no-site-packages pinnacle
    $ exit

.. note::

    I personally use and setup virtualenvwrapper on all my servers and local development machines so that I can use ``workon <virtualenv>`` to easily activate a virtualenv. This is why I put all my virtualenvs in ``/usr/local/virtualenvs``.


Make a location for the example site::

    $ cd /srv/
    $ sudo mkdir sites
    $ sudo chown deploy:deploy sites
    $ sudo su deploy
    $ cd sites
    $ git clone https://github.com/Byteme8199/pinnacle.git pinnacle
    $ cd pinnacle
    $ exit
    $ sudo chown www-data:www-data /srv/sites/pinnacle/project/static/
    .. note:: I think we need to repeat the process for media so that nginx will allow video / picture uploads
    $ sudo chown www-data:www-data /srv/sites/pinnacle/project/media/
    $ sudo su deploy

Create the file ``/srv/sites/example-site/config/settings/local.py`` and add the following. Make sure to change the password and then save the file. I usually use a `random string generator <http://clsc.net/tools/random-string-generator.php>`_ to generate a new password for each new Postgresql database and user::

    from base import *

    LOCAL_SETTINGS_LOADED = True

    DEBUG = True

    INTERNAL_IPS = ('127.0.0.1', )

    ADMINS = (
        ('Your Name', 'username@example.com'),
    )

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'example_site',
            'USER': 'example_site',
            'PASSWORD': '<enter a new secure password>',
            'HOST': 'localhost',
        }
    }

Install the sites required python packages::

    $ source /usr/local/virtualenvs/example-site/bin/activate
    $ cd /srv/sites/example-site/
    $ pip install -r config/requirements/production.txt

Create a PostgreSQL user and database for your example-site::

    # exit out of the deploy user account
    $ exit
    $ createuser example_site -P
    $ Enter password for new role: [enter the same password you used in the local.py file from above]
    $ Enter it again: [enter the password again]
    $ Shall the new role be a superuser? (y/n) n
    $ Shall the new role be allowed to create databases? (y/n) y
    $ Shall the new role be allowed to create more new roles? (y/n) n
    $ createdb example_site -O example_site





Step 4: Daemonize Gunicorn using Ubuntu's Upstart* 
--------------------------------------------------

********* This didn't work last I tried I will update with a working version here *********


Create your Upstart configuration file::

    $ sudo vi /etc/init/gunicorn_example-site.conf

Add the following and save the file::

    description "upstart configuration for gunicorn example-site"

    start on net-device-up
    stop on shutdown

    respawn

    exec /usr/local/virtualenvs/example-site/bin/gunicorn_django -u www-data -c /srv/sites/example-site/config/gunicorn/example-site.py /srv/sites/example-site/config/settings/__init__.py

Start the gunicorn site::

    $ sudo start gunicorn_example-site


Step 5: Setup Nginx to proxy to your new example site
-----------------------------------------------------

Create a new file ``sudo vi /etc/nginx/sites-available/example-site.conf`` and add the following to the contents of the file::

    server {

        listen       80;
        server_name  localhost;
        access_log   /var/log/nginx/pinnacle.access.log;
        error_log    /var/log/nginx/pinnacle.error.log;


        location  /static/ {
            root  /srv/sites/pinnacle/project/;
        }

        location  /media/ {
            root  /srv/sites/pinnacle/project/;
        }


        location  / {
            proxy_pass            http://127.0.0.1:8000/;
            proxy_redirect        off;
            proxy_set_header      Host             $host;
            proxy_set_header      X-Real-IP        $remote_addr;
            proxy_set_header      X-Forwarded-For  $proxy_add_x_forwarded_for;
            client_max_body_size  5000m;
        }

    }

Enable the new site::

    $ cd /etc/nginx/sites-enabled
    $ sudo rm default
    $ sudo ln -s ../sites-available/example-site.conf

Start nginx::

Old School
    $ sudo /etc/init.d/nginx start
New School
    $ sudo service nginx restart 
