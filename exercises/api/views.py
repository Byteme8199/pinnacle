from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import link
from rest_framework.decorators import api_view

from easy_thumbnails.alias import aliases
from easy_thumbnails.files import get_thumbnailer

from django.utils.translation import ugettext as _

from config.models import LanguageConfig
from exercises.models import Exercise
from exercises.models import Equipment
from exercises.models import ExerciseCategory
from exercises.models import ExerciseImage
from exercises.models import ExerciseComment
from exercises.models import Muscle
from utils.language import load_item_languages
from utils.language import load_language
from utils.permissions import CreateOnlyPermission


class ExerciseViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for exercise objects
    '''
    model = Exercise
    permission_classes = (IsAuthenticatedOrReadOnly, CreateOnlyPermission)
    ordering_fields = '__all__'
    filter_fields = ('category',
                     'creation_date',
                     'description',
                     'language',
                     'muscles',
                     'muscles_secondary',
                     'status',
                     'name',
                     'equipment',
                     'license',
                     'license_author')

    def pre_save(self, obj):
        '''
        Set language, author and status
        '''
        obj.language = load_language()
        obj.set_author(self.request)


@api_view(['GET'])
def search(request):
    '''
    Searches for exercises.

    This format is currently used by the exercise search autocompleter
    '''
    q = request.GET.get('term', None)
    results = []
    if not q:
        return Response(results)

    languages = load_item_languages(LanguageConfig.SHOW_ITEM_EXERCISES)
    exercises = (Exercise.objects.filter(name__icontains=q)
                                 .filter(language__in=languages)
                                 .filter(status=Exercise.STATUS_ACCEPTED)
                                 .order_by('category__name', 'name')
                                 .distinct())

    for exercise in exercises:
        if exercise.main_image:
            image_obj = exercise.main_image
            image = image_obj.image.url
            t = get_thumbnailer(image_obj.image)
            thumbnail = t.get_thumbnail(aliases.get('micro_cropped')).url
        else:
            image = None
            thumbnail = None

        exercise_json = {'id': exercise.id,
                         'name': exercise.name,
                         'value': exercise.name,
                         'category': _(exercise.category.name),
                         'image': image,
                         'image_thumbnail': thumbnail}

        results.append(exercise_json)

    return Response(results)


class EquipmentViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    API endpoint for equipment objects
    '''
    model = Equipment
    ordering_fields = '__all__'
    filter_fields = ('name',)


class ExerciseCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    API endpoint for exercise categories objects
    '''
    model = ExerciseCategory
    ordering_fields = '__all__'
    filter_fields = ('name',)


class ExerciseImageViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for exercise image objects
    '''
    model = ExerciseImage
    permission_classes = (IsAuthenticatedOrReadOnly, CreateOnlyPermission)
    ordering_fields = '__all__'
    filter_fields = ('is_main',
                     'status',
                     'exercise',
                     'license',
                     'license_author')

    @link()
    def thumbnails(self, request, pk):
        '''
        Return a list of the image's thumbnails
        '''
        image = ExerciseImage.objects.get(pk=pk)
        thumbnails = {}
        for alias in aliases.all():
            t = get_thumbnailer(image.image)
            thumbnails[alias] = {'url': t.get_thumbnail(aliases.get(alias)).url,
                                 'settings': aliases.get(alias)}
        thumbnails['original'] = image.image.url
        return Response(thumbnails)

    def pre_save(self, obj):
        '''
        Set the license data
        '''
        obj.set_author(self.request)


class ExerciseCommentViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    API endpoint for exercise comment objects
    '''
    model = ExerciseComment
    ordering_fields = '__all__'
    filter_fields = ('comment',
                     'exercise')


class MuscleViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    API endpoint for muscle objects
    '''
    model = Muscle
    ordering_fields = '__all__'
    filter_fields = ('name',
                     'is_front')
