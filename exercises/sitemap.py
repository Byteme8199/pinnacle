from django.contrib.sitemaps import Sitemap
from exercises.models import Exercise
from utils.language import load_item_languages
from config.models import LanguageConfig


class ExercisesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        language_list = load_item_languages(LanguageConfig.SHOW_ITEM_EXERCISES)
        return Exercise.objects.accepted().filter(language__in=language_list)
