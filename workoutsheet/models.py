from django.db import models
from django.utils import timezone
from account.models import Account
from exercise.models import ExerciseName

class WorkoutWeek(models.Model):
	name = models.ForeignKey(ExerciseName, verbose_name="Exercise")  #Get ExerciseNames from other database table
	workout = models.ForeignKey('WorkoutSheet')
	set_number = models.PositiveSmallIntegerField(max_length=3, blank=True, null=True, verbose_name="Sets" )
	#result = models.CharField(max_length=255, blank=True, null=True)
	percent_of_max = models.CharField(max_length=255, blank=True, null=True)
	tempo = models.CharField(max_length=255, blank=True, null=True)
	rest_time = models.CharField(max_length=255, blank=True, null=True, verbose_name="Rest")
	reps = models.PositiveSmallIntegerField(max_length=4, blank=True, null=True)
	weight = models.PositiveSmallIntegerField(max_length=4, blank=True, null=True)
	result_array = models.CharField(max_length=255, blank=True, null=True) #comma seperated array for weight results

	WORKOUT_WEEK_NUMBER = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
	)
	
	workout_week = models.CharField(max_length=5, choices=WORKOUT_WEEK_NUMBER, default='1', verbose_name="Week")
	
	def __unicode__(self):
		return u"%s: Week #%s" % (self.name.name, self.workout_week)

	class Meta:
		verbose_name_plural = "Weeks"	

class WorkoutSheet(models.Model):
	account = models.ForeignKey(Account)
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now(), editable=False)
	
	def weeks(self):
		f = WorkoutWeek.objects.filter(workout=self.pk)
		print f
		return f

	
	EXERCISE_CATEGORY_CHOICES = (
		('GEN', 'General Workouts'),
		('WARM', 'Warmup Exercises'),
		('PLYO', 'Plyometrics'),
		('CORE', 'Core Excercises'),
	)

	exercise_category = models.CharField(max_length=4, choices=EXERCISE_CATEGORY_CHOICES, default='GEN')
	
	def __unicode__(self):
		return u"%s: %s" % (self.exercise_category, self.name)

