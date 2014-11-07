from django.contrib import admin
from exercise.models import ExerciseName


class ExerciseNameAdmin(admin.ModelAdmin):
	class Media:
                css = {
                        'all': ('admin/css/admin.css',)
                }


# Register your models here.
admin.site.register(ExerciseName, ExerciseNameAdmin)
