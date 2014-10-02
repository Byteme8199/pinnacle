from os.path import join as path_join

from django.conf import settings
from django.utils import translation
from django.core.exceptions import ObjectDoesNotExist

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import StyleSheet1
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from core.models import Language

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

    try:
        language = Language.objects.get(short_name=used_language)

    # No luck, load english as our fall-back language
    except ObjectDoesNotExist:
        language = Language.objects.get(short_name="en")

    return language


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
    languages = (language.id,)

    # Only registered users have a profile
    if request.user.is_authenticated():
        profile = request.user.userprofile
        show_english = profile.show_english_ingredients

        # If the user's language is not english and has the preference, add english to the list
        if show_english and language.short_name != 'en':
            languages = (language.id, 2)

    return languages


# register new truetype fonts for reportlab
pdfmetrics.registerFont(TTFont(
    'OpenSans', path_join(settings.SITE_ROOT, 'core/static/fonts/OpenSans-Light.ttf')))
pdfmetrics.registerFont(TTFont(
    'OpenSans-Bold', path_join(settings.SITE_ROOT, 'core/static/fonts/OpenSans-Bold.ttf')))
pdfmetrics.registerFont(TTFont(
    'OpenSans-Regular', path_join(settings.SITE_ROOT, 'core/static/fonts/OpenSans-Regular.ttf')))

styleSheet = StyleSheet1()
styleSheet.add(ParagraphStyle(
               name='Normal',
               fontName='OpenSans',
               fontSize=10,
               leading=12,
               ))
styleSheet.add(ParagraphStyle(
               parent=styleSheet['Normal'],
               fontSize=8,
               name='Small',
               ))
styleSheet.add(ParagraphStyle(
               parent=styleSheet['Normal'],
               name='Bold',
               fontName='OpenSans-Bold',
               ))
