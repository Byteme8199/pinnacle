from django.db import models
from django.utils import timezone
from account.models import Account

class ExerciseType(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return u"%s" % self.name

class Exercise(models.Model):
	# A workout has many exercises
	movement_name = models.ForeignKey(ExerciseType)
	date = models.DateTimeField(default=timezone.now())
	description = models.CharField(max_length=255)

	def __unicode__(self):
		return u"%s" % self.movement_name

class ExerciseSet(models.Model):
	set_number = models.PositiveSmallIntegerField(max_length=4)
	reps = models.PositiveSmallIntegerField(max_length=4, blank=True, null=True)
	rep_info = models.CharField(max_length=80)
	minutes = models.PositiveSmallIntegerField(max_length=3, blank=True, null=True)
	seconds = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)

	rest_minutes = models.PositiveSmallIntegerField(max_length=3, blank=True, null=True)
	rest_seconds = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)

	tempo = models.CharField(max_length=255)
	result = models.CharField(max_length=255)
	note = models.TextField(blank=True, null=False)
	# may need to implement note functionality here
	exercise = models.ForeignKey(Exercise)
	workout = models.ForeignKey("Workout")

	def __unicode__(self):
		return u"%d" % self.set_number
	
class Workout(models.Model):
	account = models.ForeignKey(Account)
	exercise_sets = models.ManyToManyField(ExerciseSet, related_name="ExerciseSet", editable=False)
	description = models.CharField(max_length=255)
	note = models.TextField(blank=True, null=False)
	def __unicode__(self):
		return u"%d Workout" % self.account 

    

