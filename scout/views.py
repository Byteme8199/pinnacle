# Create your views here.
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from scout.models import *
from django.utils import timezone


class LoggedInMixin(object):

    @method_decorator(login_required)

    def dispatch(self, *args, **kwargs):
		####  Request the Account ID of the User Account thats logged in
		#self.request.user.account.id = self.request.user.account.id
		
		if self.request.user.is_staff:
			if self.request.user.account.ghost_id == 'None':
				self.request.session['active_user'] = self.request.user.account.id
			else:
				self.request.session['active_user'] = self.request.user.account.ghost_id.id
		else:
			self.request.session['active_user'] = self.request.user.account.id
		
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class ScoutView(LoggedInMixin, ListView):

	model = ScoutSheet
	template_name = 'scout/index.html'

	def get_queryset(self):
		return ScoutSheet.objects.filter(account=self.request.session['active_user'])
	
	def get_context_data(self, **kwargs):
		context = super(ScoutView, self).get_context_data(**kwargs)
		context['rankings'] = ScoutSheet.objects.filter(account=self.request.session['active_user'])
		return context
	
	
class GuestScoutView(LoggedInMixin, ListView):
	model = ScoutSheet
	template_name = 'scout/index.html'

	def get_queryset(self):
		return ScoutSheet.objects.filter(account=self.request.session['active_user'])
		
	def get_context_data(self, **kwargs):
		thisid = self.request.path.split('/')
		context = super(GuestScoutView, self).get_context_data(**kwargs)
		context['rankings'] = ScoutSheet.objects.filter(account=self.request.session['active_user'])
		return context