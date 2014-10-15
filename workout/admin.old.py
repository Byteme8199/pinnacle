from django.contrib import admin
from workout.models import *
from django.db import models

class ExerciseSetInline(admin.StackedInline):
	model = ExerciseSet
	inline_classes = ('grp-collapse grp-open',)
	#fields = ('set_number', 'reps', 'rep_info', 'minutes', 'seconds', 'rest_minutes', 'rest_seconds', 'tempo', 'result', 'note')
	fieldsets = [
		('', {'fields': [('exercise', 'instructions')]}),
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
	list_display = ('account', 'description', 'note', 'created_date', 'has_completed')
	search_fields = ['account',]
	raw_id_fields = ('account',)
	inlines = [DayInline]

admin.site.register(ExerciseType, ExerciseTypeAdmin)
admin.site.register(ExerciseSet, ExerciseSetAdmin)
admin.site.register(ExerciseSetGroup, ExerciseSetGroupAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Routine, RoutineAdmin)