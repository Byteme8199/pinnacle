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
	
class ExerciseTypeAdmin(admin.ModelAdmin):
	list_filter = ('name',)
	list_display = ('name',)
	
class WorkoutAdmin(admin.ModelAdmin):
	list_filter = ('account', 'exercise_sets')
	search_fields = ['account',]
	raw_id_fields = ('account',)
	inlines = [ExerciseSetInline]

admin.site.register(ExerciseType, ExerciseTypeAdmin)
admin.site.register(Workout, WorkoutAdmin)