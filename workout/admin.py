from django.contrib import admin
from workout.models import *
from django.db import models

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
	extra = 1

class DayInline(admin.StackedInline):
	model = Day
	inline_classes = ('grp-collapse grp-open',)
	raw_id_fields = ('exercise_group',)
	extra = 0
	
class ExerciseSetAdmin(admin.ModelAdmin):
	list_filter = ('set_number',)

class ExerciseSetGroupAdmin(admin.ModelAdmin):
	inlines = [ExerciseSetInline]
	
class ExerciseTypeAdmin(admin.ModelAdmin):
	list_filter = ('name',)
	list_display = ('name',)

class DayAdmin(admin.ModelAdmin):
	list_filter = ('due_date', 'exercise_group')
	search_fields = ['due_date',]
	
class RoutineAdmin(admin.ModelAdmin):
	list_filter = ('account', 'days')
	search_fields = ['account',]
	raw_id_fields = ('account',)
	inlines = [DayInline]

admin.site.register(ExerciseType, ExerciseTypeAdmin)
admin.site.register(ExerciseSet, ExerciseSetAdmin)
admin.site.register(ExerciseSetGroup, ExerciseSetGroupAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Routine, RoutineAdmin)





#from django.db import models
#from django.utils import timezone
#from account.models import Account
#
#class ExerciseType(models.Model):
#	name = models.CharField(max_length=255)
#
#	def __unicode__(self):
#		return u"%s" % self.name
#
#class ExerciseSet(models.Model):
#	set_number = models.PositiveSmallIntegerField(max_length=4)
#	reps = models.PositiveSmallIntegerField(max_length=4, blank=True, null=True)
#	rep_info = models.CharField(max_length=80, blank=True, null=False)
#	minutes = models.PositiveSmallIntegerField(max_length=3, blank=True, null=True)
#	seconds = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
#	rest_minutes = models.PositiveSmallIntegerField(max_length=3, blank=True, null=True)
#	rest_seconds = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
#
#	tempo = models.CharField(max_length=255, blank=True, null=False)
#	result = models.CharField(max_length=255, blank=True, null=False)
#	note = models.TextField(blank=True, null=False)
#
#	exercise = models.ForeignKey(ExerciseType)
#	day = models.ForeignKey("Day")
#
#	def __unicode__(self):
#		return u"%d" % self.set_number
#	
#class Day(models.Model):
#	exercise_sets = models.ManyToManyField(ExerciseSet, related_name="ExerciseSet", editable=False)
#	due_date = models.DateField(default=timezone.now())
#	
#	def __unicode__(self):
#		return self.due_date
#	
#class Routine(models.Model):
#	account = models.ForeignKey(Account)
#	days = models.ManyToManyField(Day, related_name="Day", editable=False)
#	note = models.TextField(blank=True, null=False)
#	
#	def __unicode__(self):
#		return u"%s Workout Routine" % str(self.account)