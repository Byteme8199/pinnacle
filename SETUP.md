# Ubuntu Server Setup Guide for Pinnacle Prospects

These instructions are modified from those found at [epicserve].

[epicserve]: https://epicserve-docs.readthedocs.org/en/latest/django/ubuntu-server-django-guide.html

## Step 1: Install Software


Before you begin it might be a good idea to update your system clock
```shell
$ sudo ntpdate time.nist.gov
```
Download lists of new/upgradable packages
```shell
$ sudo aptitude update
```

### OpenSSH

SSH server was already installed on digitalocean (I think) if not carry here it is in case

Since I like to connect to my servers using SSH the first thing I install is openssh-server
```shell
$ sudo aptitude install openssh-server
```
ssh should work to your server now (I *really* *really* hope you did this before disconnecting)

### Python Header Files

The Python header files are needed in order to compile binding libraries like `psycopg2`.
```shell
$ sudo aptitude install python2.7-dev
```

### PostgreSQL

Might be up to version 9.3 or higher when you get back to this.
```shell
$ sudo aptitude install postgresql postgresql-server-dev-9.1
```
Make your Ubuntu user a PostgreSQL superuser
```shell
$ sudo su - postgres
$ createuser --superuser <your username>
$ exit
```
Restart PostgreSQL
```shell
$ sudo service postgresql restart
```

### Nginx And Git

```shell
$ sudo aptitude install nginx git
```

Note:
> If you are serving video files replace nginx with nginx-extras 
> in order to get the mp4 and flv nginx modules


### FFMPEG

We use ffmpeg for making thumbnails from the uploaded videos.::
```shell
$ sudo apt-add-repository ppa:jon-severinsson/ffmpeg
$ sudo apt-get update
$ sudo apt-get install ffmpeg
```

There is a full story about this [here]. 
The above is the short answer from Guillaume ~3 answers down.

[here]: http://askubuntu.com/questions/432542/is-ffmpeg-missing-from-the-official-repositories-in-14-04


### REDIS

We are not currently using redis for celery / djcelery implementation.
Follow [these] directions but use the most up to date (Stable) version from [redis].

[these]: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-redis
[redis]: http://redis.io/download



## Step 2: Setup a Generic Deploy User

The reason we are setting up a generic deploy user is so that if you have multiple developers who are allowed to do deployments you can easily add the developer's SSH public key to the deploy user's ``/home/deploy/.ssh/authorized_keys`` file in order to allow them to do deployments.

```shell
$ sudo useradd -d /home/deploy -m -s /bin/bash deploy
```

## Step 3: Install Pinnacle Site

#### Setup a virtualenv
```shell
$ sudo apt-get install python-setuptools
$ sudo easy_install pip virtualenv
$ cd /usr/local/
$ sudo mkdir virtualenvs
$ sudo chown deploy:deploy virtualenvs
$ sudo su deploy
$ cd virtualenvs
$ virtualenv --no-site-packages pinnacle
$ exit
```
Note:
> I use and setup [virtualenvwrapper] on my servers and local development machines 
> so that I can use `workon <virtualenv>` to easily activate a virtualenv. 
> This is why I put all my virtualenvs in `/usr/local/virtualenvs`.

[virtualenvwrapper]: https://virtualenvwrapper.readthedocs.org/en/latest/install.html

#### Make a location for the site
```shell
$ cd /srv/
$ sudo mkdir sites
$ sudo chown deploy:deploy sites
$ sudo su deploy
$ cd sites
$ git clone https://github.com/Byteme8199/pinnacle.git pinnacle
$ cd pinnacle
$ exit
$ sudo chown www-data:www-data /srv/sites/pinnacle/project/static/

# I think we need to repeat the process for media 
# so that nginx will allow video / picture uploads
$ sudo chown www-data:www-data /srv/sites/pinnacle/project/media/
$ sudo su deploy
```

#### Update settings/local.py

TL;DR; Update `/srv/sites/pinnacle/project/settings/local.py` to reflect the server settings to use.

Create the file `/srv/sites/pinnacle/project/settings/local.py` and add the following. Make sure to change the password and then save the file. I usually use a [random string generator] to generate a new password for each new Postgresql database and user

[random string generator]: http://clsc.net/tools/random-string-generator.php

```python
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
```

#### Install the sites required python packages
```shell
$ source /usr/local/virtualenvs/pinnacle/bin/activate
$ cd /srv/sites/pinnacle/
$ pip install -r requirements/reboot.txt
```
> we are using reboot.txt above but make sure to use whatever 
> production requirements you need to use

#### Create a PostgreSQL user and database for your site
```shell
# exit out of the deploy user account
$ exit
$ createuser pinnacle -P
$ Enter password for new role: [enter the same password you used in the local.py file from above]
$ Enter it again: [enter the password again]
$ Shall the new role be a superuser? (y/n) n
$ Shall the new role be allowed to create databases? (y/n) y
$ Shall the new role be allowed to create more new roles? (y/n) n
$ createdb pinnacle -O pinnacle
```

#### Setup your database for the site::
```shell
# back into deploy
$ sudo su deploy
$ cd /srv/sites/pinnacle
# type the word python less by making manage.py executable
$ chmod +x manage.py
# setup the db
$ ./manage.py syncdb
# you are using south, right?
$ ./manage.py migrate --all
```

If you are itching to test the setup, django's runserver should work now. 
**DO NOT** use runserver for production. (according to the django guys)


## Step 4: Daemonize Gunicorn using Ubuntu's Upstart 

Create your Upstart configuration file
```shell
$ sudo vi /etc/init/pinnacle.conf
```

Add the following and save the file

```shell
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
```

`NAME` must match the name of your project folder from earlier and `PORT` must match the nginx port below.
Update `NUM_WORKERS` according to the server setup being used. Finally the next to last line is where the wsgi.py file is found in the project. 

Add the config as a system service
```shell
$ sudo ln -fs /lib/init/upstart-job /etc/init.d/pinnacle
```

Make it start at system boot
```shell
$ sudo update-rc.d pinnacle defaults
```

Start the site service
```shell
$ sudo service pinnacle start
```

Your site should now be running on the port specified above. Nginx setup below handles port forwarding.


## Step 5: Daemonize the Celery process

** still researching this **

Seems like it will be something similar to Daemonizing Gunicorn

* [info](http://stackoverflow.com/questions/14275821/how-to-run-celery-as-a-daemon-in-production/16470913#16470913)
* [more](http://stackoverflow.com/questions/10250682/how-to-write-an-ubuntu-upstart-job-for-celery-django-celery-in-a-virtualenv?rq=1)


try this out

```shell
# iamcelery -runs the celery worker in the virtualenv 
#
#
# This task runs on startup to start the celery server as the env user

description "Celery Backend for long running processes"

start on runlevel [2345]
stop on runlevel [06]

# Try to restart if it ends unexpectedly
respawn
# Try max of 10 times with 5 second timeouts
respawn limit 10 5
# Time to wait between sending TERM and KILL signals
kill timeout 20

script
    NAME=pindev
    USER=deploy
    # NAME should be the name of the virtual environment
    # To make things easier for me I use the name
    # name of the project file
    ENV=/usr/local/virtualenvs/$NAME/bin/celery
    SRV=/srv/sites/$NAME
    exec sudo su -s /bin/sh -c 'cd $SRV; exec "$0" "$@"' \
        $USER -- $ENV \
        --app=project.celery:app worker -l info
end script

```



## Step 6: Setup Nginx to proxy to your new example site

Create a new file `sudo vi /etc/nginx/sites-available/pinnacle.conf` and add the following to the contents of the file.

```nginx
server {

    listen       80;
    server_name  localhost;
    access_log   /var/log/nginx/pinnacle.access.log;
    error_log    /var/log/nginx/pinnacle.error.log;


    location  /static/ {
        root  /srv/sites/pinnacle/project/;
        autoindex off;
        # These 3 work to make video streaming
        # work though max_ranges is probably the only
        # necessary directive more testing is needed
        send_timeout 100m;
        max_ranges 0;
        client_max_body_size 5000M;
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
```

Enable the new site
```shell
$ cd /etc/nginx/sites-enabled
$ sudo rm default
$ sudo ln -s ../sites-available/pinnacle.conf
```

Start nginx
```shell
$ sudo service nginx restart 
```

If you followed these directions your server ip or domain name, if you have already pointed that at the server should show you your site.


Notes on nginx:
*  [directives](http://nginx.org/en/docs/http/ngx_http_core_module.html)


## Maintenance

*TBD*

Database backups by [digitalocean].

[digitalocean]: https://www.digitalocean.com/community/tutorials/how-to-backup-postgresql-databases-on-an-ubuntu-vps
