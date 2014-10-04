from django.db import models
from django.utils import timezone
from account.models import Account

class ExerciseType(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True, null=True)
	hints = models.CharField(max_length=255, blank=True, null=True)

	def __unicode__(self):
		return u"%s" % self.name
	
class ExerciseSet(models.Model):
	instructions = models.CharField(max_length=255, blank=True, null=True)
	set_number = models.PositiveSmallIntegerField(max_length=4, verbose_name="Number of Sets")
	reps = models.PositiveSmallIntegerField(max_length=4, blank=True, null=True)
	rep_info = models.CharField(max_length=120, blank=True, null=False)
	minutes = models.PositiveSmallIntegerField(max_length=3, blank=True, null=True)
	seconds = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
	rest_minutes = models.PositiveSmallIntegerField(max_length=3, blank=True, null=True)
	rest_seconds = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)

	tempo = models.CharField(max_length=255, blank=True, null=False)
	result = models.CharField(max_length=255, blank=True, null=False)
	note = models.TextField(blank=True, null=False)

	exercise = models.ForeignKey(ExerciseType)
	exercise_group = models.ForeignKey("ExerciseSetGroup")

	has_completed = models.BooleanField(default='None', verbose_name="Exercise Completed?")
	
	def __unicode__(self):
		return "[%s] %s x %s" % (self.exercise.name, str(self.set_number), str(self.reps))

class ExerciseSetGroup(models.Model):
	name = models.CharField(max_length=255)
	exercise_sets = models.ManyToManyField(ExerciseSet, related_name="ExerciseSet", editable=False)
	
	def get_exercise_sets(self):
		return ExerciseSet.objects.filter(exercise_group=self.id)
	
	def __unicode__(self):
		exercises = ""
		for exercise_set in ExerciseSet.objects.filter(exercise_group=self.id):
			exercises = exercises + str(exercise_set) + " | "
		return u"%s - %s" % (self.name, exercises)
	
class Day(models.Model):
	due_date = models.DateField(default=timezone.now())
	routine = models.ForeignKey("Routine")
	exercise_group = models.ForeignKey(ExerciseSetGroup)
	has_completed = models.BooleanField(default='None', verbose_name="Day Completed?")
	note = models.TextField(blank=True, null=False)
	
	class Meta:
		ordering = ['due_date']
		verbose_name_plural = "Days Routine"
	
	def __unicode__(self):
		return str(self.due_date)
	
class Routine(models.Model):
	account = models.ForeignKey(Account)
	days = models.ManyToManyField(Day, related_name="Day", editable=False)
	description = models.TextField(blank=True, null=False)
	note = models.TextField(blank=True, null=False)
	created_date = models.DateField(default=timezone.now(), editable=False)
	has_completed = models.BooleanField(default='None', verbose_name="Routine Completed?")
	
	def get_days(self):
		return Day.objects.filter(routine=self.id)
	
	def __unicode__(self):
		return u"Workout Routine - %s" % str(self.created_date)