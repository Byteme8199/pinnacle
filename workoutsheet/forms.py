from django.forms import ModelForm
from workoutsheet.models import WorkoutWeek
from django import forms

class WorkoutWeekForm(ModelForm):

	class Meta:
		model = WorkoutWeek
		#exclude = ('name', 'workout', 'set_number', 'percent_of_max', 'tempo', 'rest_time', 'reps', 'weight', 'workout_week')
