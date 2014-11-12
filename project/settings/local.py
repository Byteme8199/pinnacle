from __future__ import absolute_import

from .dev import *

EMAIL_HOST_USER = 'pinnacleprospects@gmail.com'
EMAIL_HOST_PASSWORD = '*0S@U*9yU!!e'

DATABASES = {'default': dj_database_url.config(
    default='sqlite:////' + ROOT_DIR + '/newworkout2.db')}

CELERY_IMPORTS = ('project',)
CELERY_RESULT_BACKEND = "amqp"
BROKER_URL = "amqp://guest:guest@localhost//"
CELERY_TASK_RESULT_EXPIRES = 300
CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
CELERY_BEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
#CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
#CELERY_RESULT_BACKEND='djcelery.backends.cache:CacheBackend'
