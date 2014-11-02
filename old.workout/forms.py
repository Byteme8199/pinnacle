from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from workout.models import Workout, WorkoutWeek, Exercise


class WorkoutForm(ModelForm):
	class Meta:
		model = Workout




WorkoutWeekFormSet = inlineformset_factory(Workout, WorkoutWeek)
ExerciseFormSet = inlineformset_factory(Workout, Exercise)


class ExerciseForm(ModelForm):
	class Meta:
		model = Exercise
		exclude = [ 'workout' ]
