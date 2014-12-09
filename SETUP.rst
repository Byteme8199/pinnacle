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


OpenSSH
~~~~~~

SSH server was already installed on digitalocean (I think) if not carry here it is in case

Since I like to connect to my servers using SSH the first thing I install is openssh-server::

    $ sudo aptitude install openssh-server

ssh should work to your server now (I really really hope you did this before disconnecting)


Python Header Files
~~~~~~~~~~~~~~~~~~

The Python header files are needed in order to compile binding libraries like ``psycopg2``. ::

    $ sudo aptitude install python2.7-dev

PostgreSQL
~~~~~~~~~

Might be up to version 9.3 or higher when you get back to this
::

    $ sudo aptitude install postgresql postgresql-server-dev-9.1

Make your Ubuntu user a PostgreSQL superuser::

    $ sudo su - postgres
    $ createuser --superuser <your username>
    $ exit

Restart PostgreSQL::

    $ sudo service postgresql restart


Nginx And Git
~~~~~~~~~~~

::

    $ sudo aptitude install nginx git



FFMPEG
~~~~~

We use ffmpeg for making thumbnails from the uploaded videos.::

    $ sudo apt-add-repository ppa:jon-severinsson/ffmpeg
    $ sudo apt-get update
    $ sudo apt-get install ffmpeg

There is a full story about this here_. 
The above is the short answer from Guillaume ~3 answers down.

.. _here: http://askubuntu.com/questions/432542/is-ffmpeg-missing-from-the-official-repositories-in-14-04



REDIS*
~~~~

We are not currently using redis for celery / djcelery implementation.
Follow these_ directions but use the most up to date (Stable) version from redis_.

.. _these: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-redis
.. _redis: http://redis.io/download






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

    I use and setup virtualenvwrapper on my servers and local development machines so that I can use ``workon <virtualenv>`` to easily activate a virtualenv. This is why I put all my virtualenvs in ``/usr/local/virtualenvs``.


Make a location for the site::

    $ cd /srv/
    $ sudo mkdir sites
    $ sudo chown deploy:deploy sites
    $ sudo su deploy
    $ cd sites
    $ git clone https://github.com/Byteme8199/pinnacle.git pinnacle
    $ cd pinnacle
    $ exit
    $ sudo chown www-data:www-data /srv/sites/pinnacle/project/static/
    # I think we need to repeat the process for media so that nginx will allow video / picture uploads
    $ sudo chown www-data:www-data /srv/sites/pinnacle/project/media/
    $ sudo su deploy


TL;DR; Update ``/srv/sites/pinnacle/project/settings/local.py`` to reflect the server settings to use.
Create the file ``/srv/sites/pinnacle/project/settings/local.py`` and add the following. Make sure to change the password and then save the file. I usually use a `random string generator <http://clsc.net/tools/random-string-generator.php>`_ to generate a new password for each new Postgresql database and user::

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
            'NAME': 'pinnacle',
            'USER': 'pinnacle',
            'PASSWORD': '<enter a new secure password>',
            'HOST': 'localhost',
        }
    }

Install the sites required python packages::

    $ source /usr/local/virtualenvs/pinnacle/bin/activate
    $ cd /srv/sites/pinnacle/
    $ pip install -r requirements/reboot.txt

Create a PostgreSQL user and database for your site::

    # exit out of the deploy user account
    $ exit
    $ createuser pinnacle -P
    $ Enter password for new role: [enter the same password you used in the local.py file from above]
    $ Enter it again: [enter the password again]
    $ Shall the new role be a superuser? (y/n) n
    $ Shall the new role be allowed to create databases? (y/n) y
    $ Shall the new role be allowed to create more new roles? (y/n) n
    $ createdb pinnacle -O pinnacle


Setup your database for the site::

    # back into deploy
    $ sudo su deploy
    $ cd /srv/sites/pinnacle
    # type the word python less by making manage.py executable
    $ chmod +x manage.py
    # setup the db
    $ ./manage.py syncdb
    # you are using south, right?
    $ ./manage.py migrate --all

If you are itching to test the setup, django's runserver should work now. 
**DO NOT** use runserver for production. (according to the django guys)


Step 4: Daemonize Gunicorn using Ubuntu's Upstart 
-------------------------------------------------

Create your Upstart configuration file::

    $ sudo vi /etc/init/pinnacle.conf

Add the following and save the file::

    description "Pinnacle Dev website"
    start on runlevel [2345]
    stop on runlevel [06]
    respawn
    respawn limit 10 5

    script
        NAME=pinnacle
        PORT=8000
        NUM_WORKERS=2
        TIMEOUT=600
        USER=deploy
        GROUP=deploy
        LOGFILE=/var/log/gunicorn/$NAME.log
        LOGDIR=$(dirname $LOGFILE)
        test -d $LOGDIR || mkdir -p $LOGDIR
        cd /srv/sites/$NAME
        exec /usr/local/virtualenvs/$NAME/bin/gunicorn \
                -w $NUM_WORKERS -t $TIMEOUT \
                --user=$USER --group=$GROUP --log-level=debug \
                --name=$NAME -b 127.0.0.1:$PORT \
                --log-file=$LOGFILE 2>>$LOGFILE \
                project.wsgi:application
    end script


NAME must match the name of your project folder from earlier and PORT must match the nginx port below. 
Update NUM_WORKERS according to the server setup being used. Finally the next to last line is where 
the wsgi.py file is found in the project. 


Add the config as a system service::
    
    $ sudo ln -fs /lib/init/upstart-job /etc/init.d/pinnacle

Make it start at system boot::

    $ sudo update-rc.d pinnacle defaults


Start the site service::

    $ sudo service pinnacle start

Your site should now be running on the port specified above. Nginx setup below handles port forwarding.

Step 5: Daemonize the Celery process
------------------------------------

** still researching this **


Step 6: Setup Nginx to proxy to your new example site
-----------------------------------------------------

Create a new file ``sudo vi /etc/nginx/sites-available/pinnacle.conf`` and add the following to the contents of the file::

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
    $ sudo ln -s ../sites-available/pinnacle.conf

Start nginx::

    $ sudo service nginx restart 

If you followed these directions your server ip or domain name if you have already pointed that at the server 
should show you your site.
