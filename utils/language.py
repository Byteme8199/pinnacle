#import logging

from django.utils import translation
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache
from core.models import Language

from config.models import LanguageConfig
from utils.cache import cache_mapper


#logger = logging.getLogger('custom')


# ************************
# Language functions
# ************************


def load_language():
    '''
    Returns the currently used language, e.g. to load appropriate exercises
    '''

    # TODO: perhaps store a language preference in the user's profile?

    # Read the first part of a composite language, e.g. 'de-at'
    used_language = translation.get_language().split('-')[0]

    language = cache.get(cache_mapper.get_language_key(used_language))
    if language:
        return language

    try:
        language = Language.objects.get(short_name=used_language)
    except ObjectDoesNotExist:
        # No luck, load english as our fall-back language
        language = Language.objects.get(short_name="en")

    cache.set(cache_mapper.get_language_key(language), language)
    return language


def load_item_languages(item):
    '''
    Returns the languages for a data type (exercises, ingredients)
    '''

    language = load_language()
    languages = cache.get(cache_mapper.get_language_config_key(language, item))

    # Load the configurations we are interested in and return the languages
    if not languages:
        languages = []

        config = LanguageConfig.objects.filter(language=language, item=item, show=True)
        if not config:
            languages.append(Language.objects.get(short_name="en"))
            return languages

        for i in config:
            languages.append(i.language_target)

        cache.set(cache_mapper.get_language_config_key(language, item), languages)

    return languages


def load_ingredient_languages(request):
    '''
    Filter the ingredients the user will see by its language.

    Additionally, if the user has selected on his preference page that he wishes
    to also see the ingredients in English (from the US Department of Agriculture),
    show those too.

    This only makes sense if the user's language isn't English, as he will be
    presented those in that case anyway, so also do a check for this.
    '''

    language = load_language()
    languages = load_item_languages(LanguageConfig.SHOW_ITEM_INGREDIENTS)

    # Only registered users have a profile
    if request.user.is_authenticated():
        profile = request.user.userprofile
        show_english = profile.show_english_ingredients

        # If the user's language is not english and has the preference, add english to the list
        if show_english and language.short_name != 'en':
            languages = list(set(languages + [Language.objects.get(pk=2)]))

    return languages
