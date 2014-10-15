from django.forms import ModelForm
from workout.models import Workout, WorkoutSet, Exercise, ExerciseName 
from django import forms


class ManageWorkoutForm(ModelForm):
	
	class Meta:
		model = Workout
		exclued = ('account')



#class RoutineForm(ModelForm):

#	class Meta:
#		model = Routine
#		exclude = ('account', 'created_date', 'days', 'description')
		
#class DayForm(ModelForm):

#	class Meta:
#		model = Day
#		exclude = ('due_date', 'exercise_group', 'routine')
