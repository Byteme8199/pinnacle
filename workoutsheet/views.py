from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

from workoutsheet.models import WorkoutSheet, WorkoutWeek
from workoutsheet.forms import WorkoutWeekForm
from exercise.models import ExerciseName

from django.utils import timezone
import operator

class LoggedInMixin(object):

    @method_decorator(login_required)

    def dispatch(self, *args, **kwargs):
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class WorkoutVideosView(LoggedInMixin, ListView):
	model = ExerciseName
	template_name = 'workout/videos.html'

	def get_queryset(self):
		return ExerciseName.objects.all()
	
class WorkoutWorkoutsView(LoggedInMixin, ListView):
	model = WorkoutSheet
	template_name = 'workout/workouts.html'

	def get_queryset(self):
		return WorkoutSheet.objects.filter(account=self.request.user.account.id)
	
class WorkoutBaseView(LoggedInMixin, ListView):
	model = WorkoutSheet
	template_name = 'workout/index.html'

	def get_queryset(self):
		return WorkoutSheet.objects.filter(account=self.request.user.account.id)
	
class WorkoutView(LoggedInMixin, UpdateView):
	model = WorkoutSheet
	#form_class = SchoolForm
	template_name = 'workout/workout.html'
	success_url = '/workout/'


class WorkoutWeekView(LoggedInMixin, UpdateView):
	model = WorkoutWeek
	form_class = WorkoutWeekForm
	template_name = 'workout/workout_week.html'
	success_url = '/workout/'
	
	def form_valid(self, form):
		form.save()
		return super(WorkoutWeekView, self).form_valid(form)
