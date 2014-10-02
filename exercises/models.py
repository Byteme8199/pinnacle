#import six
#import logging

from django.db import models
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify  # django.utils.text.slugify in django 1.5!
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.core.urlresolvers import reverse
from django.core import mail
from django.core.cache import cache
from django.core.validators import MinLengthValidator
from django.db.models.signals import pre_save
from django.db.models.signals import post_delete
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global

from utils.managers import SubmissionManager
from utils.models import AbstractLicenseModel
from utils.models import AbstractSubmissionModel
from utils.constants import EMAIL_FROM
from utils.cache import delete_template_fragment_cache
from utils.cache import reset_workout_canonical_form
from utils.cache import cache_mapper

#logger = logging.getLogger('custom')


class Muscle(models.Model):
    '''
    Muscle an exercise works out
    '''

    name = models.CharField(max_length=50,
                            verbose_name=_('Name'),
                            help_text=_('In latin, e.g. "Pectoralis major"'))

    # Whether to use the front or the back image for background
    is_front = models.BooleanField(default=1)

    # Metaclass to set some other properties
    class Meta:
        ordering = ["name", ]

    def __unicode__(self):
        '''
        Return a more human-readable representation
        '''
        return self.name

    def get_owner_object(self):
        '''
        Muscle has no owner information
        '''
        return False


class Equipment(models.Model):
    '''
    Equipment used or needed by an exercise
    '''

    name = models.CharField(max_length=50,
                            verbose_name=_('Name'))

    class Meta:
        '''
        Set default ordering
        '''
        ordering = ["name", ]

    def __unicode__(self):
        '''
        Return a more human-readable representation
        '''
        return self.name

    def get_owner_object(self):
        '''
        Equipment has no owner information
        '''
        return False


class ExerciseCategory(models.Model):
    '''
    Model for an exercise category
    '''
    name = models.CharField(max_length=100,
                            verbose_name=_('Name'),)

    # Metaclass to set some other properties
    class Meta:
        verbose_name_plural = _("Exercise Categories")
        ordering = ["name", ]

    def __unicode__(self):
        '''
        Return a more human-readable representation
        '''
        return self.name

    def get_owner_object(self):
        '''
        Category has no owner information
        '''
        return False

    def save(self, *args, **kwargs):
        '''
        Reset all cached infos
        '''

        super(ExerciseCategory, self).save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        '''
        Reset all cached infos
        '''

        super(ExerciseCategory, self).delete(*args, **kwargs)


class Exercise(AbstractSubmissionModel, AbstractLicenseModel, models.Model):
    '''
    Model for an exercise
    '''

    objects = SubmissionManager()
    '''Custom manager'''

    category = models.ForeignKey(ExerciseCategory,
                                 verbose_name=_('Category'))
    description = models.TextField(max_length=2000,
                                   verbose_name=_('Description'),
                                   validators=[MinLengthValidator(40)])
    '''Description on how to perform the exercise'''

    name = models.CharField(max_length=200,
                            verbose_name=_('Name'))

    muscles = models.ManyToManyField(Muscle,
                                     verbose_name=_('Primary muscles'),
                                     null=True,
                                     blank=True)
    '''Main muscles trained by the exercise'''

    muscles_secondary = models.ManyToManyField(Muscle,
                                               verbose_name=_('Secondary muscles'),
                                               related_name='secondary_muscles',
                                               null=True,
                                               blank=True)
    '''Secondary muscles trained by the exercise'''

    equipment = models.ManyToManyField(Equipment,
                                       verbose_name=_('Equipment'),
                                       null=True,
                                       blank=True)
    '''Equipment needed by this exercise'''

    creation_date = models.DateField(_('Date'),
                                     auto_now_add=True,
                                     null=True,
                                     blank=True)
    '''The submission date'''
    #
    # Django methods
    #
    class Meta:
        ordering = ["name", ]

    def get_absolute_url(self):
        '''
        Returns the canonical URL to view an exercise
        '''
        return reverse('exercise-view', kwargs={'id': self.id, 'slug': slugify(self.name)})

    def save(self, *args, **kwargs):
        '''
        Reset all cached infos
        '''

        super(Exercise, self).save(*args, **kwargs)

        # Cached objects
        cache.delete(cache_mapper.get_exercise_key(self))
        cache.delete(cache_mapper.get_exercise_muscle_bg_key(self))

        # Cached workouts
        for set in self.set_set.all():
            reset_workout_canonical_form(set.exerciseday.training_id)

    def delete(self, *args, **kwargs):
        '''
        Reset all cached infos
        '''

        # Cached objects
        cache.delete(cache_mapper.get_exercise_key(self))
        cache.delete(cache_mapper.get_exercise_muscle_bg_key(self))

        # Cached workouts
        for set in self.set_set.all():
            reset_workout_canonical_form(set.exerciseday.training.pk)

        super(Exercise, self).delete(*args, **kwargs)

    def __unicode__(self):
        '''
        Return a more human-readable representation
        '''
        return self.name

    #
    # Own methods
    #

    @property
    def main_image(self):
        '''
        Return the main image for the exercise or None if nothing is found
        '''
        return self.exerciseimage_set.accepted().filter(is_main=True).first()

    def get_owner_object(self):
        '''
        Exercise has no owner information
        '''
        return False


def exercise_image_upload_dir(instance, filename):
    '''
    Returns the upload target for exercise images
    '''
    return "exercise-images/{0}/{1}".format(instance.exercise.id, filename)


class ExerciseImage(AbstractSubmissionModel, AbstractLicenseModel, models.Model):
    '''
    Model for an exercise image
    '''

    objects = SubmissionManager()
    '''Custom manager'''

    exercise = models.ForeignKey(Exercise,
                                 verbose_name=_('Exercise'))
    '''The exercise the image belongs to'''

    image = models.ImageField(verbose_name=_('Image'),
                              help_text=_('Only PNG and JPEG formats are supported'),
                              upload_to=exercise_image_upload_dir)
    '''Uploaded image'''

    is_main = models.BooleanField(verbose_name=_('Is main picture'),
                                  default=False,
                                  help_text=_("Tick the box if you want to set this image as the "
                                              "main one for the exercise (will be shown e.g. in "
                                              "the search). The first image is automatically "
                                              "marked by the system."))
    '''A flag indicating whether the image is the exercise's main image'''

    class Meta:
        '''
        Set default ordering
        '''
        ordering = ['-is_main', 'id']

    def save(self, *args, **kwargs):
        '''
        Only one image can be marked as main picture at a time
        '''
        if self.is_main:
            ExerciseImage.objects.filter(exercise=self.exercise).update(is_main=False)
            self.is_main = True
        else:
            if ExerciseImage.objects.accepted().filter(exercise=self.exercise).count() == 0 \
               or not ExerciseImage.objects.accepted() \
                            .filter(exercise=self.exercise, is_main=True)\
                            .count():
                self.is_main = True


        # And go on
        super(ExerciseImage, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        '''
        Reset all cached infos
        '''
        super(ExerciseImage, self).delete(*args, **kwargs)

        # Make sure there is always a main image
        if not ExerciseImage.objects.accepted() \
                .filter(exercise=self.exercise, is_main=True).count() \
           and ExerciseImage.objects.accepted() \
                .filter(exercise=self.exercise) \
                .filter(is_main=False) \
                .count():

                image = ExerciseImage.objects.accepted() \
                    .filter(exercise=self.exercise, is_main=False)[0]
                image.is_main = True
                image.save()

    def get_owner_object(self):
        '''
        Image has no owner information
        '''
        return False


def delete_exercise_image_on_delete(sender, instance, **kwargs):
    '''
    Delete the image, along with its thumbnails, from the disk
    '''

    thumbnailer = get_thumbnailer(instance.image)
    thumbnailer.delete_thumbnails()
    instance.image.delete(save=False)


post_delete.connect(delete_exercise_image_on_delete, sender=ExerciseImage)


def delete_exercise_image_on_update(sender, instance, **kwargs):
    '''
    Delete the corresponding image from the filesystem when the an ExerciseImage
    object was changed
    '''
    if not instance.pk:
        return False

    try:
        old_file = ExerciseImage.objects.get(pk=instance.pk).image
    except ExerciseImage.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        thumbnailer = get_thumbnailer(instance.image)
        thumbnailer.delete_thumbnails()
        instance.image.delete(save=False)


pre_save.connect(delete_exercise_image_on_update, sender=ExerciseImage)


# Generate all thumbnails when uploading a new image
saved_file.connect(generate_aliases_global)


class ExerciseComment(models.Model):
    '''
    Model for an exercise comment
    '''
    exercise = models.ForeignKey(Exercise,
                                 verbose_name=_('Exercise'),
                                 editable=False)
    comment = models.CharField(max_length=200,
                               verbose_name=_('Comment'),
                               help_text=_('A comment about how to correctly do this exercise.'))

    def __unicode__(self):
        '''
        Return a more human-readable representation
        '''
        return self.comment

    def save(self, *args, **kwargs):
        '''
        Reset cached workouts
        '''
        for set in self.exercise.set_set.all():
            reset_workout_canonical_form(set.exerciseday.training_id)

        super(ExerciseComment, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        '''
        Reset cached workouts
        '''
        for set in self.exercise.set_set.all():
            reset_workout_canonical_form(set.exerciseday.training.pk)

        super(ExerciseComment, self).delete(*args, **kwargs)

    def get_owner_object(self):
        '''
        Comment has no owner information
        '''
        return False
