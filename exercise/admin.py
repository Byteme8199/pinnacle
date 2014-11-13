from django.contrib import admin
from exercise.models import ExerciseName


class ExerciseNameAdmin(admin.ModelAdmin):
	pass

# Register your models here.
admin.site.register(ExerciseName, ExerciseNameAdmin)
