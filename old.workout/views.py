from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from workout.models import Workout, Exercise, WorkoutWeek
from workout.forms import WorkoutForm, WorkoutWeekFormSet, ExerciseFormSet, ExerciseForm
from exercise.models import ExerciseName

from django.utils import timezone


class LoggedInMixin(object):

    @method_decorator(login_required)

    def dispatch(self, *args, **kwargs):
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class CreateWorkout(LoggedInMixin, CreateView):
	model = Workout 
	template_name = 'workout/create_workout.html'
	success_url = '/workout/exercise/create/'
	
	def form_valid(self, form):
		workout = Workout(account=form.cleaned_data['account'], name=form.cleaned_data['name'], description=form.cleaned_data['description'] )
		workout.save()		
		self.success_url = self.success_url + str(workout.id)
		return super(CreateWorkout, self).form_valid(form)
	

class AddExercisesToWorkout(LoggedInMixin, CreateView):
	model = Exercise 
	form_class = ExerciseForm
	template_name = 'workout/create_exercise.html'
	success_url = '/workout/set/create/'
	
	def get(self, request, *args, **kwargs):
		self.object = None
		workout = Workout.objects.get(pk=kwargs['workout_id'])
	
		exercises = ExerciseName.objects.all()
		form_class = self.get_form_class()
		form = self.get_form(form_class)
				
		return self.render_to_response(self.get_context_data(form=form, workout=workout, exercises=exercises))
	
	def form_valid(self, form):

		ex1 = Exercise(workout=form.cleaned_data['id_workout'], name=form.cleaned_data['id_exercise_0'], description=form.cleaned_data['id_description_0'])
		ex1.save()
		# make object from form arrays
		# parse this over and over per item in array
		#for thing in things:
			#exercise = Exercise(account=form.cleaned_data['account'], name=form.cleaned_data['name'], description=form.cleaned_data['description'] )
			#exercise.save()		
		self.success_url = self.success_url + str(form.cleaned_data['id_workout'])
		return super(AddExercisesToWorkout, self).form_valid(form)
		

class AddExerciseSetsToExercise(LoggedInMixin, CreateView):
	model = WorkoutWeek
	template_name = 'workout/create_set.html'
	success_url = '/workout/'
	
	def get(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		exerciselist = Exercise.objects.filter(workout=kwargs['workout_id'])
		return self.render_to_response(self.get_context_data(form=form, workout=kwargs['workout_id'], exercises=exerciselist))

		# return super(AddExerciseSetsToExercise, self).form_valid(form)
	
class CreateSet(LoggedInMixin, CreateView):
	model = WorkoutWeek
	

class WorkoutView(LoggedInMixin, ListView):
	model = Workout 
	template_name = 'workout/index.html'

	def get_queryset(self):
		return Workout.objects.filter(account=self.request.user.account.id)
	
class EditRoutineView(LoggedInMixin, UpdateView):

#	model = Routine
	template_name = 'workout/edit_routine.html'
#	form_class = RoutineForm
	success_url = '/workout/'

	def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
		
		#form = Routine(has_completed=form.cleaned_data['has_completed'])
		form.save()
		return super(EditRoutineView, self).form_valid(form)

class EditDayView(LoggedInMixin, UpdateView):

#	model = Day
	template_name = 'workout/edit_day.html'
#	form_class = RoutineForm
	success_url = '/workout/'

	def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

		form.save()
		return super(EditDayView, self).form_valid(form)
	
	
