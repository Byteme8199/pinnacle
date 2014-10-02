#import logging
import decimal
import json
import datetime

from functools import wraps
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


#logger = logging.getLogger('custom')


class DecimalJsonEncoder(json.JSONEncoder):
    '''
    Custom JSON encoder.

    This class is needed because we store some data as a decimal (e.g. the
    individual weight entries in the workout log) and they need to be
    processed, json.dumps() doesn't work on them
    '''
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


def disable_for_loaddata(signal_handler):
    '''
    Decorator to prevent clashes when loading data with loaddata and
    post_connect signals. See also:
    http://stackoverflow.com/questions/3499791/how-do-i-prevent-fixtures-from-conflicting
    '''
    @wraps(signal_handler)
    def wrapper(*args, **kwargs):
        if kwargs['raw']:
            # print "Skipping signal for {0} {1}".format(args, kwargs)
            return
        signal_handler(*args, **kwargs)
    return wrapper


def next_weekday(date, weekday):
    '''
    Helper function to find the next weekday after a given date,
    e.g. the first Monday after the 2013-12-05

    See link for more details:
    * http://stackoverflow.com/questions/6558535/python-find-the-date-for-the-first-monday-after-a

    :param date: the start date
    :param weekday: weekday (0, Monday, 1 Tuesday, 2 Wednesday)
    :type date: datetime.date
    :type weekday int
    :return: datetime.date
    '''
    days_ahead = weekday - date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return date + datetime.timedelta(days_ahead)


def make_token(user):
    '''
    Convenience function that generates the UID and token for a user

    :param user: a user object
    :return: the uid and the token
    '''
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    return uid, token


def check_token(uidb64, token):
    '''
    Checks that the user token is correct.

    :param uidb:
    :param token:
    :return: True on success, False in all other situations
    '''
    if uidb64 is not None and token is not None:
        uid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=uid)

        if user is not None and default_token_generator.check_token(user, token):
            return True

    return False
