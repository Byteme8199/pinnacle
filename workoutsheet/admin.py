from django.contrib import admin
from workoutsheet.models import WorkoutWeek, WorkoutSheet
from django.db import models

class WorkoutWeekInline(admin.StackedInline):
	model = WorkoutWeek
	fieldsets = [
		('', {'fields': [('group', 'group_order', 'workout_week', 'name')]}),
		('Sets', {'fields': [('set_number', 'reps', 'rest_time', 'tempo', 'result_array')]}),
	]
	extra = 1

class WorkoutSheetAdmin(admin.ModelAdmin):
	inlines = [WorkoutWeekInline]

	date_hierarchy = 'created_date'
	list_filter = ('exercise_category', 'account', 'created_date', 'start_date')
	list_display = ('exercise_category', 'name', 'account', 'created_date', 'start_date')


admin.site.register(WorkoutSheet, WorkoutSheetAdmin)
