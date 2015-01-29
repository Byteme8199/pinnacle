from __future__ import absolute_import

from .dev import *


#### EMAIL SETUP ####
DEFAULT_FROM_EMAIL = 'pinnacleprospects@gmail.com'
SERVER_EMAIL = 'pinnacleprospects@gmail.com'

EMAIL_USE_TLS = True
EMAIL_PORT = 587

EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_HOST_USER = 'pinnacleprospects@gmail.com'
EMAIL_KEY = 'ds9iHQ7cpOL4711IUORieQ'


DATABASES = {'default': dj_database_url.config(
    default='sqlite:////' + ROOT_DIR + '/newworkout2.db')}


#DATABASES = {
#        'default': {
#            'ENGINE': 'django.db.backends.postgresql_psycopg2',
#            'NAME': 'pindev',
#            'USER': 'pindev',
#            'PASSWORD': 'whycantwebefriends',
#            'HOST': 'localhost',
#        }
#}





# CELERY REDIS CONFIG #
BROKER_URL = "redis://localhost:6379/0"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

DEVSERVER = True