# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from workout.models import Workout, Exercise, WorkoutSet, ExerciseName
#from workout.forms import RoutineForm, DayForm

from django.utils import timezone


class LoggedInMixin(object):

    @method_decorator(login_required)

    def dispatch(self, *args, **kwargs):
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)



class WorkoutView(LoggedInMixin, ListView):
	model = Workout 


#	def get_queryset(self):
#		return Routine.objects.filter(account=self.request.user.account.id)
	
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
	
	
