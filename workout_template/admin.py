from django.contrib import admin
from workout_template.models import TemplateWorkoutWeek, WorkoutSheetTemplate
from django.db import models

class TemplateWorkoutWeekInline(admin.TabularInline):
	model = TemplateWorkoutWeek
	fieldsets = [
		('', {'fields': [('group', 'group_order', 'workout_week', 'name')]}),
		('Sets', {'fields': [('set_number', 'reps', 'rest_time', 'tempo')]}),
	]
	extra = 1

class WorkoutSheetTemplateAdmin(admin.ModelAdmin):
	inlines = [TemplateWorkoutWeekInline]
	
	class Media:
                css = {
                        'all': ('admin/css/admin.css',)
                }

	
admin.site.register(WorkoutSheetTemplate, WorkoutSheetTemplateAdmin)
