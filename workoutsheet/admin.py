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

	class Media:
                css = {
                        'all': ('http://www.hdvideoandwebdesign.com/pinnacle/admin-css/admin.css',)
                }

	
admin.site.register(WorkoutSheet, WorkoutSheetAdmin)
