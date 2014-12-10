from __future__ import absolute_import

from .dev import *

EMAIL_HOST_USER = 'pinnacleprospects@gmail.com'
EMAIL_HOST_PASSWORD = '*0S@U*9yU!!e'

DATABASES = {'default': dj_database_url.config(
    default='sqlite:////' + ROOT_DIR + '/newworkout2.db')}



##### OLD (pre 12/10) CELERY SETUP ######

#CELERY_IMPORTS = ('project',)
#CELERY_RESULT_BACKEND = "amqp"

#BROKER_URL = "amqp://guest:guest@localhost//"
#BROKER_URL = "django://project"
#INSTALLED_APPS += ('kombu.transport.django',)

#CELERY_TASK_RESULT_EXPIRES = 300
#CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
#CELERY_BEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# CELERY REDIS CONFIG #
BROKER_URL = "redis://localhost:6379/0"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

