from django.forms import ModelForm
from workout.models import Routine, Day
from django import forms


class RoutineForm(ModelForm):

	class Meta:
		model = Routine
		exclude = ('account', 'created_date', 'days', 'description')
		
class DayForm(ModelForm):

	class Meta:
		model = Day
		exclude = ('due_date', 'exercise_group', 'routine')