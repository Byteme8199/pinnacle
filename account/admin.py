from django.contrib import admin
from django.contrib.admin import helpers
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.utils import timezone
from account.models import Height, Weight, Score, Account, Position, Coach, Parent, TargetSchoolsList, Personal
from workoutsheet.models import WorkoutSheet, WorkoutWeek
from workout_template.models import WorkoutSheetTemplate, TemplateWorkoutWeek
from project.utils import Contact
from django.db import models
from django import forms

class HeightInline(admin.StackedInline):
	model = Height
	fields = ('height_feet', 'height_inches', 'created_date','note')
	readonly_fields = ['created_date']
	extra = 0

class WeightInline(admin.StackedInline):
	model = Weight
	fields = ('weight', 'created_date','note')
	readonly_fields = ['created_date']
	extra = 0

class ScoreInline(admin.StackedInline):
	model = Score
	fields = ('score_type', 'score_data', 'created_date','note')
	readonly_fields = ['created_date']
	extra = 0

class PositionInline(admin.StackedInline):
	model = Position
	fields = ('position_type', 'position', 'created_date','note')
	readonly_fields = ['created_date']
	extra = 0

class CoachInline(admin.StackedInline):
	model = Coach
	fields = (('fname', 'lname'), 'phone', 'email', 'created_date','note')
	readonly_fields = ['created_date']
	extra = 0

class ParentInline(admin.StackedInline):
	model = Parent
	fields = (('fname', 'lname'), 'phone', 'email', 'created_date','note')
	readonly_fields = ['created_date']
	extra = 0

class PersonalInline(admin.StackedInline):
	model = Personal
	fields = (('fname', 'lname'), 'phone', 'email', 'created_date','note')
	readonly_fields = ['created_date']
	extra = 0

class TargetSchoolsListInline(admin.StackedInline):
	model = TargetSchoolsList
	fields = ('target_schools', 'chosen_school', 'created_date','note')
	readonly_fields = ['created_date']
	extra = 0


class AddWorkoutForm(forms.Form):
        workout_name = forms.CharField(required=True)
        workout = forms.ModelChoiceField(queryset=WorkoutSheetTemplate.objects.all(), required=True)
        description = forms.CharField(required=False)


def add_workout(modeladmin, request, queryset):
        form = None
        print request.POST.get('post')
        if request.POST.get('post'):
            form = AddWorkoutForm(request.POST)
            if form.is_valid():
                workout = form.cleaned_data['workout']
                name = form.cleaned_data['workout_name']
                if request.POST['description']:
                    description = request.POST['description']
                else:
                    description = ""

                for account in queryset:
                    new_workout = WorkoutSheet(account=account, name=name, description=description, created_date=timezone.now(), start_date=timezone.now())
                    new_workout.save()

                    weeks = workout.weeks()

                    for w in weeks:
                        new_week = WorkoutWeek(workout=new_workout, group=w.group, group_order=w.group_order, workout_week=w.workout_week, name=w.name, set_number=w.set_number, reps=w.reps, rest_time=w.rest_time, tempo=w.tempo, weight=w.weight)
                        new_week.save()

                modeladmin.message_user(request, ("Successfully added workout for %d Accounts") % (queryset.count(),))
                return HttpResponseRedirect(request.get_full_path())

        if not form:
            form = AddWorkoutForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})

        return TemplateResponse(request, 'admin/add_workout.html', {'accounts': queryset, 'workout_form': form, 'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME }, current_app=modeladmin.admin_site.name)

add_workout.short_description = "Add Workout to selected Accounts"


class AccountAdmin(admin.ModelAdmin):
	inlines = [WeightInline, HeightInline, ScoreInline, PositionInline, CoachInline, ParentInline, TargetSchoolsListInline]

        actions = [add_workout]


admin.site.register(Account, AccountAdmin)
