# Create your views here.
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from scout.models import *
from django.utils import timezone


class LoggedInMixin(object):

    @method_decorator(login_required)

    def dispatch(self, *args, **kwargs):
		#print self.request.session['account']
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class ScoutView(LoggedInMixin, ListView):

	model = ScoutSheet
	template_name = 'scout/index.html'

	def get_queryset(self):
		return ScoutSheet.objects.filter(account=self.request.user.account.id)
	
	def get_context_data(self, **kwargs):
		context = super(ScoutView, self).get_context_data(**kwargs)
		context['rankings'] = ScoutSheet.objects.filter(account=self.request.user.account.id)
		return context
	
	
class GuestScoutView(LoggedInMixin, ListView):
	model = ScoutSheet
	template_name = 'scout/index.html'

	def get_queryset(self):
		if self.request.user.is_staff:
			thisid = self.request.path.split('/')
			return ScoutSheet.objects.filter(account=thisid[2])
		else:
			return ScoutSheet.objects.filter(account=self.request.user.account.id)
		
	def get_context_data(self, **kwargs):
		thisid = self.request.path.split('/')
		context = super(GuestScoutView, self).get_context_data(**kwargs)
		if self.request.user.is_staff:
			context['rankings'] = ScoutSheet.objects.filter(account=thisid[2])
		else:
			context['rankings'] = ScoutSheet.objects.filter(account=self.request.user.account.id)
		return context