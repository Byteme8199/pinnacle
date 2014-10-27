from django.contrib import admin
from workoutsheet.models import WorkoutWeek, WorkoutSheet
from django.db import models

class WorkoutWeekInline(admin.TabularInline):
	model = WorkoutWeek
	fieldsets = [
		('', {'fields': [('workout_week', 'name')]}),
		('Sets', {'fields': [('set_number', 'reps', 'rest_time', 'tempo')]}),
	]
	extra = 1

class WorkoutSheetAdmin(admin.ModelAdmin):
	inlines = [WorkoutWeekInline]
	
admin.site.register(WorkoutSheet, WorkoutSheetAdmin)