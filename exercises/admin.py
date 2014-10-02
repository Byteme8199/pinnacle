from django.contrib import admin

from exercises.models import Exercise
from exercises.models import ExerciseComment
from exercises.models import ExerciseCategory
from exercises.models import Muscle


class ExerciseCommentInline(admin.TabularInline):  # admin.StackedInline
    model = ExerciseComment
    extra = 1


class ExerciseAdmin(admin.ModelAdmin):

    inlines = [ExerciseCommentInline]

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(ExerciseCategory)
admin.site.register(Muscle)
