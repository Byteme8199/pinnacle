from django.db import models
from django.utils import timezone
from account.models import Account
from exercise.models import ExerciseName
from workout_template.models import WorkoutSheetTemplate, TemplateWorkoutWeek
from django import template
register = template.Library()

class WorkoutWeek(models.Model):
	name = models.ForeignKey(ExerciseName, verbose_name="Exercise")  #Get ExerciseNames from other database table
	workout = models.ForeignKey('WorkoutSheet')
	set_number = models.PositiveSmallIntegerField(max_length=3, blank=True, null=True, verbose_name="Sets" )
	#result = models.CharField(max_length=255, blank=True, null=True)
	percent_of_max = models.CharField(max_length=255, blank=True, null=True)
	tempo = models.CharField(max_length=255, blank=True, null=True)
	rest_time = models.CharField(max_length=255, blank=True, null=True, verbose_name="Rest")
	reps = models.CharField(max_length=255, blank=True, null=True)
	weight = models.CharField(max_length=255, blank=True, null=True)
	result_array = models.CharField(max_length=255, blank=True, null=True) #comma seperated array for weight results

	WORKOUT_WEEK_NUMBER = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
	)

	WORKOUT_GROUP = (
		('A', 'A'),
		('B', 'B'),
		('C', 'C'),
		('D', 'D'),
		('E', 'E'),
		('F', 'F'),
		('G', 'G'),
		('H', 'H'),
		('I', 'I'),
		('J', 'J'),
		('K', 'K'),
		('L', 'L'),
	)

	WORKOUT_GROUP_ORDER = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
		('6', '6'),
		('7', '7'),
		('8', '8'),
	)

	workout_week = models.CharField(max_length=5, choices=WORKOUT_WEEK_NUMBER, default='1', verbose_name="Week")
	group = models.CharField(max_length=1, choices=WORKOUT_GROUP, default='A', verbose_name="Group")
	group_order = models.CharField(max_length=1, choices=WORKOUT_GROUP_ORDER, default='1', verbose_name="Group Order")


	def __unicode__(self):
		return u"%s: Week #%s" % (self.name.name, self.workout_week)

	class Meta:
		verbose_name = "Exercise"
		verbose_name_plural = "Exercises by Week"





class WorkoutSheet(models.Model):
	account = models.ForeignKey(Account)
	workout_template = models.ForeignKey(WorkoutSheetTemplate, blank=True, null=True)
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True, null=True)

	created_date = models.DateTimeField(default=timezone.now(), editable=False)
	start_date = models.DateTimeField(default=timezone.now(), blank=True, null=True)

	def year(self):
		year = str(self.start_date)
		year = year.split('-')
		return year[0]

	def weeks(self):
		return WorkoutWeek.objects.filter(workout=self.pk)

	def fullsheet(self):
		fullsheet = []
		for week in WorkoutWeek.objects.filter(workout=self.pk).order_by('group', 'group_order', 'workout_week'):
			fullsheet.append(week)
		return fullsheet

	EXERCISE_CATEGORY_CHOICES = (
		('GEN', 'General Workouts'),
		('WARM', 'Warmup Exercises'),
		('PLYO', 'Plyometrics'),
		('CORE', 'Core Excercises'),
	)

	exercise_category = models.CharField(max_length=4, choices=EXERCISE_CATEGORY_CHOICES, default='GEN')

	def save(self, *args, **kwargs):
		if not self.id and self.workout_template:
			if not self.description:
				self.description = self.workout_template.description
			if not self.name:
				self.description = self.workout_template.name
			workout = WorkoutSheet(account=self.account, name=self.name,description=self.description, created_date=timezone.now(), start_date=self.start_date)
			workout.save()

			weeks = self.workout_template.weeks()

			for w in weeks:
				for i in range(4):
					weeknum = i + 1
					new_week = WorkoutWeek(workout=workout, group=w.group, group_order=w.group_order, workout_week=weeknum, name=w.name, set_number=w.set_number, reps=w.reps, rest_time=w.rest_time, tempo=w.tempo, weight=w.weight)
					new_week.save()
		else:
			super(WorkoutSheet, self).save(*args, **kwargs)


	class Meta:
		verbose_name = "Workout"
		verbose_name_plural = "Workouts"
		ordering = ['-start_date']
	def __unicode__(self):
		return u"%s: %s" % (self.exercise_category, self.name)

