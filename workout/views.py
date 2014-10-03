# Create your views here.
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from workout.models import Routine
from django.utils import timezone


class LoggedInMixin(object):

    @method_decorator(login_required)

    def dispatch(self, *args, **kwargs):
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class WorkoutView(LoggedInMixin, ListView):

	model = Routine
	template_name = 'workout/index.html'

	def get_queryset(self):
		return Routine.objects.filter(account=self.request.user.account.id)