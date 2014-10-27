from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from workoutsheet.models import WorkoutSheet, WorkoutWeek
from exercise.models import ExerciseName

from django.utils import timezone


class LoggedInMixin(object):

    @method_decorator(login_required)

    def dispatch(self, *args, **kwargs):
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)


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

	def form_valid(self, form):
		form.save()
		return super(WorkoutView, self).form_valid(form)