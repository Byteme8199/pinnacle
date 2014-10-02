from django.conf import settings

#from wger import get_version
from utils import constants
from utils.language import load_language


def processor(request):

    language = load_language()
    full_path = request.get_full_path()
    i18n_path = {}
    for lang in settings.LANGUAGES:
        i18n_path[lang[0]] = '/{0}{1}'.format(lang[0], full_path[3:])

    context = {
        # Application version
        'version': get_version(),

        # User language
        'language': language,

        # Available application languages
        'languages': settings.LANGUAGES,

        # The current path
        'request_full_path': full_path,

        # Translation links
        'i18n_path': i18n_path,

        # Translation links
        'datepicker_i18n_path': 'js/bootstrap-datepicker/locales/bootstrap-datepicker.{0}.js'.
        format(language.short_name),

        # Flag for guest users
        'has_demo_data': request.session.get('has_demo_data', False),

        # Don't show messages on AJAX requests (they are deleted if shown)
        'no_messages': request.META.get('HTTP_X_WGER_NO_MESSAGES', False),

        # Default cache time for template fragment caching
        'cache_timeout': settings.CACHES['default']['TIMEOUT']
    }

    # Pseudo-intelligent navigation here
    if '/software/' in request.get_full_path() \
       or '/contact' in request.get_full_path() \
       or '/api/v2' in request.get_full_path():
            context['active_tab'] = constants.SOFTWARE_TAB

    elif '/exercise/' in request.get_full_path():
        context['active_tab'] = constants.EXERCISE_TAB

    elif '/nutrition/' in request.get_full_path():
        context['active_tab'] = constants.NUTRITION_TAB

    elif '/weight/' in request.get_full_path():
        context['active_tab'] = constants.WEIGHT_TAB

    elif '/workout/' in request.get_full_path():
        context['active_tab'] = constants.WORKOUT_TAB

    else:
        context['active_tab'] = constants.USER_TAB

    return context
