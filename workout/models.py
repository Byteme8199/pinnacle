from django.db import models
from django.utils import timezone
from account.models import Account
from exercise.models import ExerciseName

#class ExerciseName(models.Model):
#	name = models.CharField(max_length=255)
#	description = models.CharField(max_length=255, blank=True, null=True)
#	video = models.FileField(upload_to='./videos/exercises/', blank=True, null=True)
#
#	EXERCISE_CATEGORY_CHOICES = (
#		('GEN', 'General Workouts'),
#		('WARM', 'Warmup Exercises'),
#		('PLYO', 'Plyometrics'),
#		('CORE', 'Core Excercises'),
#	)
#
#	exercise_category = models.CharField(max_length=4, choices=EXERCISE_CATEGORY_CHOICES, default='GEN')
#
#	def __unicode__(self):
#		return u"%s" % self.name
#
#	class Meta:
#		ordering = ['name']
#		verbose_name_plural = "exercise Descriptions"	


class WorkoutSet(models.Model):
	workout_week = models.ForeignKey('WorkoutWeek')
	set_info = models.CharField(max_length=255, blank=True, null=True)
	set_parent = models.PositiveSmallIntegerField(max_length=4, blank=True, null=True)
	

class WorkoutWeek(models.Model):
	set_number = models.PositiveSmallIntegerField(max_length=3, blank=True, null=True)
	#result = models.CharField(max_length=255, blank=True, null=True)
	percent_of_max = models.CharField(max_length=255, blank=True, null=True)
	tempo = models.CharField(max_length=255, blank=True, null=True)
	rest_time = models.CharField(max_length=255, blank=True, null=True)
	reps = models.PositiveSmallIntegerField(max_length=4, blank=True, null=True)
	weight = models.PositiveSmallIntegerField(max_length=4, blank=True, null=True)

	WORKOUT_WEEK_NUMBER = (
		('1', 'One'),
		('2', 'Two'),
		('3', 'Three'),
		('4', 'Four'),
	)
	
	workout_week = models.CharField(max_length=5, choices=WORKOUT_WEEK_NUMBER, default='1')
	exercise = models.ForeignKey('Exercise')
	workout = models.ForeignKey('Workout')

	def __unicode__(self):
		return u"%s : Set #%s" % (self.exercise.name.name, self.set_number)

	class Meta:
		verbose_name_plural = "Weeks"	


class Exercise(models.Model):
	name = models.ForeignKey(ExerciseName)
	workout = models.ForeignKey('Workout')
	description = models.CharField(max_length=255, blank=True, null=True)

	def __unicode__(self):
		return u"%s" % self.name.name

class Workout(models.Model):
	account = models.ForeignKey(Account)
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now(), editable=False)
	
	EXERCISE_CATEGORY_CHOICES = (
		('GEN', 'General Workouts'),
		('WARM', 'Warmup Exercises'),
		('PLYO', 'Plyometrics'),
		('CORE', 'Core Excercises'),
	)

	exercise_category = models.CharField(max_length=4, choices=EXERCISE_CATEGORY_CHOICES, default='GEN')

	
	def __unicode__(self):
		return u"%s" % self.name

