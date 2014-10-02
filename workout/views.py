# Create your views here.
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from workout.models import *
from django.utils import timezone


class LoggedInMixin(object):

    @method_decorator(login_required)

    def dispatch(self, *args, **kwargs):
		####  Request the Account ID of the User Account
		self.request.session['account'] = Account.objects.filter(user=self.request.user)[0].id
		#print self.request.session['account']
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class WorkoutView(LoggedInMixin, ListView):

	model = Workout
	template_name = 'workout/index.html'

	def get_queryset(self):
		return Workout.objects.filter(account=self.request.session['account'])