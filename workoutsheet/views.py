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
	
#	def get(self, request, **kwargs):
#		return super(WorkoutWeekView, self).get(request, **kwargs)
#		
#	def post(self, request, **kwargs):
#		sorted_dict = sorted(request.POST.items(), key=operator.itemgetter(0))
#		print sorted_dict
#		week = WorkoutWeek.objects.get(pk=kwargs['pk'])
#		form = WorkoutWeek(result_array=week.result_array)
#		form.save(update_fields=['result_array'])
#		print form
#		return HttpResponseRedirect('/workout/')
	
#	def form_valid(self, form):
#        # This method is called when valid form data has been POSTed.
#        # It should return an HttpResponse.
#		form = WorkoutWeek(result_array=form.cleaned_data['result_array'])
#		form.save()
#		return super(WorkoutWeekView, self).form_valid(form)
	
#		
#		request.POST = request.POST.copy()
#		
#		print request
#		
#		
#		form = self.form_class(request.POST)
#		if form.is_valid():
#        	return HttpResponseRedirect('/success/')
#			return render(request, self.template_name, {'form': form})
#
#		return super(WorkoutWeekView, self).post(request, **kwargs)
