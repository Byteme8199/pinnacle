#import logging
import hashlib

from django.core.cache import cache
from django.utils.encoding import force_bytes


#logger = logging.getLogger('custom')


def get_template_cache_name(fragment_name='', *args):
    '''
    Logic to calculate the cache key name when using django's template cache.
    Code taken from django/templatetags/cache.py
    '''
    key = u':'.join([str(arg) for arg in args])
    key_name = hashlib.md5(force_bytes(key)).hexdigest()
    return 'template.cache.{0}.{1}'.format(fragment_name, key_name)


def delete_template_fragment_cache(fragment_name='', *args):
    '''
    Deletes a cache key created on the template with django's cache tag
    '''
    cache.delete(get_template_cache_name(fragment_name, *args))


def reset_workout_canonical_form(workout_id):
    cache.delete(cache_mapper.get_workout_canonical(workout_id))


class CacheKeyMapper(object):
    '''
    Simple class for mapping the cache keys of different objects
    '''

    # Keys used by the cache
    LANGUAGE_CACHE_KEY = 'language-{0}'
    LANGUAGE_CONFIG_CACHE_KEY = 'language-config-{0}-{1}'
    EXERCISE_CACHE_KEY = 'exercise-{0}'
    EXERCISE_CACHE_KEY_MUSCLE_BG = 'exercise-muscle-bg-{0}'
    INGREDIENT_CACHE_KEY = 'ingredient-{0}'
    WORKOUT_CANONICAL_REPRESENTATION = 'workout-canonical-representation-{0}'

    def get_exercise_key(self, param):
        '''
        Return the exercise cache key
        '''
        try:
            pk = param.pk
        except AttributeError:
            pk = param

        return self.EXERCISE_CACHE_KEY.format(pk)

    def get_exercise_muscle_bg_key(self, param):
        '''
        Return the exercise muscle background cache key
        '''
        try:
            pk = param.pk
        except AttributeError:
            pk = param

        return self.EXERCISE_CACHE_KEY_MUSCLE_BG.format(pk)

    def get_language_key(self, param):
        '''
        Return the language cache key
        '''
        try:
            pk = param.pk
        except AttributeError:
            pk = param

        return self.LANGUAGE_CACHE_KEY.format(pk)

    def get_language_config_key(self, param, item):
        '''
        Return the language cache key
        '''
        try:
            pk = param.pk
        except AttributeError:
            pk = param

        return self.LANGUAGE_CONFIG_CACHE_KEY.format(pk, item)

    def get_ingredient_key(self, param):
        '''
        Return the ingredient cache key
        '''
        try:
            pk = param.pk
        except AttributeError:
            pk = param

        return self.INGREDIENT_CACHE_KEY.format(pk)

    def get_workout_canonical(self, param):
        '''
        Return the workout canonical representation
        '''
        try:
            pk = param.pk
        except AttributeError:
            pk = param

        return self.WORKOUT_CANONICAL_REPRESENTATION.format(pk)

cache_mapper = CacheKeyMapper()
