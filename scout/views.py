# Create your views here.
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from scout.models import *
from django.utils import timezone


class LoggedInMixin(object):

    @method_decorator(login_required)

    def dispatch(self, *args, **kwargs):
		####  Request the Account ID of the User Account
		self.request.session['account'] = Account.objects.filter(user=self.request.user)[0].id
		print self.request.session['account']
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class ScoutView(LoggedInMixin, ListView):

	model = ScoutSheet
	template_name = 'scout/index.html'

	def get_queryset(self):
		return ScoutSheet.objects.filter(account=self.request.session['account'])
	
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(ScoutView, self).get_context_data(**kwargs)
		# Add in the publisher
		context['rankings'] = CriterionRank.objects.filter(account=self.request.session['account']).order_by('criterion', '-created_date')
		return context