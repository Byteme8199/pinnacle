from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from account.models import Account, Weight, Height, Position, Score, Parent, Coach, TargetSchoolsList, Personal
from account.forms import HeightForm, WeightForm, PositionForm, ScoreForm, ParentForm, CoachForm, PersonalForm, TargetSchoolsListForm, PhotoForm, TeamPhotoForm, SchoolForm, GhostForm

from django.views.generic.edit import FormView, UpdateView
from django.utils import timezone
from easy_pdf.views import PDFTemplateView

from django.core.urlresolvers import reverse

		
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

class AccountView(LoggedInMixin, ListView):
    model = Account
    template_name = 'account/index.html'

    def get_queryset(self):
		return [Account.objects.get(pk=self.request.session['active_user'])]
	
class AddPhotoView(LoggedInMixin, UpdateView):
	model = Account
	form_class = PhotoForm
	template_name = 'account/add_pic.html'
	success_url = '/account/'

	def form_valid(self, form):
		form.save()
		return super(AddPhotoView, self).form_valid(form)
	
class AddTeamPhotoView(LoggedInMixin, UpdateView):
	model = Account
	form_class = TeamPhotoForm
	template_name = 'account/add_team_pic.html'
	success_url = '/account/'

	def form_valid(self, form):
		form.save()
		return super(AddTeamPhotoView, self).form_valid(form)
	
class AddSchoolView(LoggedInMixin, UpdateView):
	model = Account
	form_class = SchoolForm
	template_name = 'account/add_school.html'
	success_url = '/account/'

	def form_valid(self, form):
		form.save()
		return super(AddSchoolView, self).form_valid(form)

class AddWeightView(LoggedInMixin, FormView):

	model = Weight
	template_name = 'account/add_weight.html'
	form_class = WeightForm
	success_url = '/account/'

	def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
		account_id = Account.objects.get(pk=self.request.session['active_user'])
		form = Weight(account=account_id, created_date=timezone.now(), weight=form.cleaned_data['weight'], note=form.cleaned_data['note'])
		form.save()
		return super(AddWeightView, self).form_valid(form)

class AddHeightView(LoggedInMixin, FormView):

	model = Height
	template_name = 'account/add_height.html'
	form_class = HeightForm
	success_url = '/account/'

	def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
		account_id = Account.objects.get(pk=self.request.session['active_user'])
		form = Height(account=account_id, created_date=timezone.now(), height_feet=form.cleaned_data['height_feet'], height_inches=form.cleaned_data['height_inches'], note=form.cleaned_data['note'])
		form.save()
		return super(AddHeightView, self).form_valid(form)

class AddScoreView(LoggedInMixin, FormView):

	model = Score
	template_name = 'account/add_score.html'
	form_class = ScoreForm
	success_url = '/account/'

	def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
		account_id = Account.objects.get(pk=self.request.session['active_user'])
		form = Score(account=account_id, created_date=timezone.now(), score_data=form.cleaned_data['score_data'], score_type=form.cleaned_data['score_type'], note=form.cleaned_data['note'])
		form.save()
		return super(AddScoreView, self).form_valid(form)	
	
class AddPositionView(LoggedInMixin, FormView):

	model = Position
	template_name = 'account/add_position.html'
	form_class = PositionForm
	success_url = '/account/'

	def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
		account_id = Account.objects.get(pk=self.request.session['active_user'])
		form = Position(account=account_id, created_date=timezone.now(), position=form.cleaned_data['position'], position_type=form.cleaned_data['position_type'], note=form.cleaned_data['note'])
		form.save()
		return super(AddPositionView, self).form_valid(form)

	
	
class AddPersonalView(LoggedInMixin, FormView):

	model = Personal
	template_name = 'account/add_personal.html'
	form_class = PersonalForm
	success_url = '/account/'

	def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
		account_id = Account.objects.get(pk=self.request.session['active_user'])
		form = Personal(account=account_id, created_date=timezone.now(), fname=self.request.user.first_name, lname=self.request.user.last_name, street=form.cleaned_data['street'], city=form.cleaned_data['city'], state=form.cleaned_data['state'], zipcode=form.cleaned_data['zipcode'], phone=form.cleaned_data['phone'], phone_carrier=form.cleaned_data['phone_carrier'], email=form.cleaned_data['email'], note="")
		form.save()
		return super(AddPersonalView, self).form_valid(form)


class EditPersonalView(LoggedInMixin, UpdateView):
	model = Personal
	form_class = PersonalForm
	template_name = 'account/edit_personal.html'
	success_url = '/account/'

	def form_valid(self, form):
		form.save()
		return super(EditPersonalView, self).form_valid(form)

class GhostView(LoggedInMixin, UpdateView):
	model = Account
	form_class = GhostForm
	template_name = 'account/ghost.html'
	success_url = '/account/'

	def form_valid(self, form):
		form.save()
		return super(GhostView, self).form_valid(form)	
	
	
class AddParentView(LoggedInMixin, FormView):

	model = Parent
	template_name = 'account/add_parent.html'
	form_class = ParentForm
	success_url = '/account/'

	def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
		account_id = Account.objects.get(pk=self.request.session['active_user'])
		form = Parent(account=account_id, created_date=timezone.now(), fname=form.cleaned_data['fname'], lname=form.cleaned_data['lname'], street=form.cleaned_data['street'], city=form.cleaned_data['city'], state=form.cleaned_data['state'], zipcode=form.cleaned_data['zipcode'], phone=form.cleaned_data['phone'], email=form.cleaned_data['email'], note=form.cleaned_data['note'])
		form.save()
		return super(AddParentView, self).form_valid(form)
	
	
class AddCoachView(LoggedInMixin, FormView):

	model = Coach
	template_name = 'account/add_coach.html'
	form_class = CoachForm
	success_url = '/account/'

	def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
		account_id = Account.objects.get(pk=self.request.session['active_user'])
		form = Coach(account=account_id, created_date=timezone.now(), fname=form.cleaned_data['fname'], lname=form.cleaned_data['lname'], street=form.cleaned_data['street'], city=form.cleaned_data['city'], state=form.cleaned_data['state'],  zipcode=form.cleaned_data['zipcode'], phone=form.cleaned_data['phone'], email=form.cleaned_data['email'], note=form.cleaned_data['note'])
		form.save()
		return super(AddCoachView, self).form_valid(form)	

	
class AddTargetListView(LoggedInMixin, FormView):

	model = TargetSchoolsList
	template_name = 'account/add_targetlist.html'
	form_class = TargetSchoolsListForm
	success_url = '/account/'

	def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
		account_id = Account.objects.get(pk=self.request.session['active_user'])
		form = TargetSchoolsList(account=account_id, created_date=timezone.now(),  target_schools=form.cleaned_data.get('target_schools'), chosen_school=form.cleaned_data['chosen_school'], note=form.cleaned_data['note'])
		form.save()
		return super(AddTargetListView, self).form_valid(form)	
		
	
class AccountPDF(PDFTemplateView):

	model = Account
	template_name = 'account/pdf.html'

	def get_context_data(self, **kwargs):
		account = Account.objects.get(pk=self.request.session['active_user'])
		kwargs['weights'] = account.weights()
		kwargs['heights'] = account.heights()
		kwargs['account'] = account.__dict__
		return super(AccountPDF, self).get_context_data(**kwargs)
