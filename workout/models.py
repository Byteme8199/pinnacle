from django.db import models
from django.utils import timezone
from account.models import Account

class ExerciseType(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return u"%s" % self.name

class ExerciseSet(models.Model):
	set_number = models.PositiveSmallIntegerField(max_length=4)
	reps = models.PositiveSmallIntegerField(max_length=4, blank=True, null=True)
	rep_info = models.CharField(max_length=80, blank=True, null=False)
	minutes = models.PositiveSmallIntegerField(max_length=3, blank=True, null=True)
	seconds = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
	rest_minutes = models.PositiveSmallIntegerField(max_length=3, blank=True, null=True)
	rest_seconds = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)

	tempo = models.CharField(max_length=255, blank=True, null=False)
	result = models.CharField(max_length=255, blank=True, null=False)
	note = models.TextField(blank=True, null=False)
	# may need to implement note functionality here
	exercise = models.ForeignKey(ExerciseType)
	workout = models.ForeignKey("Workout")

	def __unicode__(self):
		return u"%d" % self.set_number
	
class Workout(models.Model):
	account = models.ForeignKey(Account)
	#workout_date = models.DateField(default=timezone.now())
	start = models.DateField(default=timezone.now())
	end = models.DateField(default=timezone.now())
	exercise_sets = models.ManyToManyField(ExerciseSet, related_name="ExerciseSet", editable=False)
	description = models.CharField(max_length=255)
	note = models.TextField(blank=True, null=False)
	def __unicode__(self):
		return u"%s Workout" % str(self.account)

    

