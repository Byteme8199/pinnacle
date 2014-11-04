from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

from workoutsheet.models import WorkoutSheet, WorkoutWeek
from workoutsheet.forms import WorkoutWeekForm
from exercise.models import ExerciseName

from django.shortcuts import render_to_response


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
	cat_type = 'GEN'
	
	def get(self, request, *args, **kwargs):
		context = locals()
		context['cat_type'] = 'GEN'
		context['years'] = ["2018,GEN","2017,GEN","2016,GEN","2015,GEN","2014,GEN","2013,GEN","2012,GEN"]
		return render_to_response(self.template_name, context)

class WorkoutPlyometricView(LoggedInMixin, ListView):
	model = WorkoutSheet
	template_name = 'workout/workouts.html'
	
	def get(self, request, *args, **kwargs):
		context = locals()
		context['cat_type'] = 'PLYO'
		context['years'] = ["2018,PLYO","2017,PLYO","2016,PLYO","2015,PLYO","2014,PLYO","2013,PLYO","2012,PLYO"]
		return render_to_response(self.template_name, context)

class WorkoutWarmupView(LoggedInMixin, ListView):
	model = WorkoutSheet
	template_name = 'workout/workouts.html'

	def get(self, request, *args, **kwargs):
		context = locals()
		context['cat_type'] = 'WARM'
		context['years'] = ["2018,WARM","2017,WARM","2016,WARM","2015,WARM","2014,WARM","2013,WARM","2012,WARM"]
		return render_to_response(self.template_name, context)

class WorkoutCoreView(LoggedInMixin, ListView):
	model = WorkoutSheet
	template_name = 'workout/workouts.html'
	
	def get(self, request, *args, **kwargs):
		context = locals()
		context['cat_type'] = 'CORE'
		context['years'] = ["2018,CORE","2017,CORE","2016,CORE","2015,CORE","2014,CORE","2013,CORE","2012,CORE"]
		return render_to_response(self.template_name, context)
	
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
