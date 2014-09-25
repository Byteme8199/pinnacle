from django.contrib import admin
from workout.models import *
from django.db import models


#class ExerciseType(models.Model):
#	name = models.CharField(max_length=255)
#
#	def __unicode__(self):
#		return u"%s" % self.name
#
#class Exercise(models.Model):
#	# A workout has many exercises
#	movement_name = models.ForeignKey(ExerciseType)
#	date = models.DateTimeField(default=timezone.now())
#	description = models.CharField(max_length=255)
#
#	def __unicode__(self):
#		return u"%s" % self.movement_name
#
#class ExerciseSet(models.Model):
#	set_number = models.PositiveSmallIntegerField(max_length=4)
#	reps = models.PositiveSmallIntegerField(max_length=4, blank=True, null=True)
#	rep_info = models.CharField(max_length=80)
#	minutes = models.PositiveSmallIntegerField(max_length=3, blank=True, null=True)
#	seconds = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
#
#	rest_minutes = models.PositiveSmallIntegerField(max_length=3, blank=True, null=True)
#	rest_seconds = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
#
#	tempo = models.CharField(max_length=255)
#	result = models.CharField(max_length=255)
#	note = models.TextField(blank=True, null=False)
#	# may need to implement note functionality here
#	exercise = models.ForeignKey(Exercise)
#
#	def __unicode__(self):
#		return u"%d" % self.set_number
#	
#class Workout(models.Model):
#	account = models.ForeignKey(Account)
#	exercise_sets = models.ManyToManyField(ExerciseSet)
#	description = models.CharField(max_length=255)
#	note = models.TextField(blank=True, null=False)
#	def __unicode__(self):
#		return u"%d Workout" % self.account 

	

class ExerciseSetInline(admin.StackedInline):
	model = ExerciseSet
	inline_classes = ('grp-collapse grp-open',)
	#fields = ('set_number', 'reps', 'rep_info', 'minutes', 'seconds', 'rest_minutes', 'rest_seconds', 'tempo', 'result', 'note')
	fieldsets = [
		('', {'fields': ['exercise']}),
		('Sets', {'fields': [('set_number', 'reps', 'rep_info')]}),
		('Set Time', {'fields': [('minutes', 'seconds')], 'classes': ('grp-collapse grp-closed',)}),
		('Rest', {'fields': [('rest_minutes', 'rest_seconds', 'tempo')], 'classes': ('grp-collapse grp-closed',)}),
		('Results', {'fields': [('result', 'note')], 'classes': ('grp-collapse grp-closed',)}),
	]
	raw_id_fields = ('exercise',)
	extra = 1
	
class ExerciseTypeAdmin(admin.ModelAdmin):
	list_filter = ('name',)
	list_display = ('name',)
	
class WorkoutAdmin(admin.ModelAdmin):
	list_filter = ('account', 'exercise_sets')
	#list_display = ('title', 'thumbnail', 'video_type', 'created_date')
	search_fields = ['account',]
	raw_id_fields = ('account',)
	inlines = [ExerciseSetInline]

admin.site.register(ExerciseType, ExerciseTypeAdmin)
admin.site.register(Workout, WorkoutAdmin)