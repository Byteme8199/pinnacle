from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

from workoutsheet.models import WorkoutSheet, WorkoutWeek
from workoutsheet.forms import WorkoutWeekForm
from exercise.models import ExerciseName
from account.models import Account

from django.shortcuts import render_to_response
from easy_pdf.views import PDFTemplateView

from django.utils import timezone
import operator
import collections

class LoggedInMixin(object):

    @method_decorator(login_required)

    def dispatch(self, *args, **kwargs):
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class WorkoutVideosView(LoggedInMixin, ListView):
	model = ExerciseName
	template_name = 'workout/videos.html'

	def get_queryset(self):
		return ExerciseName.objects.all()
	
class WorkoutVideosByIDView(LoggedInMixin, ListView):
	model = ExerciseName
	template_name = 'workout/videos.html'

	def get_queryset(self):
		thisid = self.request.path.split('/')
		return ExerciseName.objects.filter(id=thisid[3])
	
class WorkoutWorkoutsView(LoggedInMixin, ListView):
	model = WorkoutSheet
	template_name = 'workout/workouts.html'
	cat_type = 'GEN'
	
	def get(self, request, *args, **kwargs):
		context = locals()
		workouts = collections.OrderedDict()
		years = [2018 , 2017, 2016, 2015, 2014, 2013, 2012]
		cat_type = 'GEN'
		for year in years:
			yearstart = str(year) + "-01-01"
			yearend = str(year) + "-12-31"
			objs = WorkoutSheet.objects.filter(start_date__year=year, exercise_category=cat_type, account=request.user.account.id)
			if len(objs) > 0:
				workouts[year] = objs
		context['workouts'] = workouts
		context['cat_type'] = cat_type
		return render_to_response(self.template_name, context)

class WorkoutPlyometricView(LoggedInMixin, ListView):
	model = WorkoutSheet
	template_name = 'workout/workouts.html'
	
	def get(self, request, *args, **kwargs):
		context = locals()
		workouts = collections.OrderedDict()
		years = [2018 , 2017, 2016, 2015, 2014, 2013, 2012]
		cat_type = 'PLYO'
		for year in years:
			yearstart = str(year) + "-01-01"
			yearend = str(year) + "-12-31"
			objs = WorkoutSheet.objects.filter(start_date__year=year, exercise_category=cat_type, account=request.user.account.id)
			if len(objs) > 0:
				workouts[year] = objs
		context['workouts'] = workouts
		context['cat_type'] = cat_type
		return render_to_response(self.template_name, context)

class WorkoutWarmupView(LoggedInMixin, ListView):
	model = WorkoutSheet
	template_name = 'workout/workouts.html'

	def get(self, request, *args, **kwargs):
		context = locals()
		workouts = collections.OrderedDict()
		years = [2018 , 2017, 2016, 2015, 2014, 2013, 2012]
		cat_type = 'WARM'
		for year in years:
			yearstart = str(year) + "-01-01"
			yearend = str(year) + "-12-31"
			objs = WorkoutSheet.objects.filter(start_date__year=year, exercise_category=cat_type, account=request.user.account.id)
			if len(objs) > 0:
				workouts[year] = objs
		context['workouts'] = workouts
		context['cat_type'] = cat_type
		return render_to_response(self.template_name, context)

class WorkoutCoreView(LoggedInMixin, ListView):
	model = WorkoutSheet
	template_name = 'workout/workouts.html'
	
	def get(self, request, *args, **kwargs):
		context = locals()
		workouts = collections.OrderedDict()
		years = [2018 , 2017, 2016, 2015, 2014, 2013, 2012]
		cat_type = 'CORE'
		for year in years:
			yearstart = str(year) + "-01-01"
			yearend = str(year) + "-12-31"
			objs = WorkoutSheet.objects.filter(start_date__year=year, exercise_category=cat_type, account=request.user.account.id)
			if len(objs) > 0:
				workouts[year] = objs
		context['workouts'] = workouts
		context['cat_type'] = cat_type
		return render_to_response(self.template_name, context)
	
class WorkoutBaseView(LoggedInMixin, ListView):
	model = WorkoutSheet
	template_name = 'workout/index.html'

	def get(self, request, *args, **kwargs):
		context = locals()
		cats = ['CORE', 'GEN', 'WARM', 'PLYO']
		categories = {}
		for cat in cats:
			objs = WorkoutSheet.objects.filter(exercise_category=cat, account=request.user.account.id)
			categories[cat] = len(objs)
		context['cats'] = categories
		return render_to_response(self.template_name, context)
	
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


class WorkoutPDF(PDFTemplateView):
	
	model = WorkoutSheet
	template_name = 'workout/pdf.html'

	def get_context_data(self, workout_id, **kwargs):
		context = super(WorkoutPDF, self).get_context_data(**kwargs)
		context['object'] = WorkoutSheet.objects.get(pk=workout_id)
		context['weeks'] = WorkoutWeek.objects.filter(workout=workout_id)
		return context
