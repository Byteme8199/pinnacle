from django.forms import ModelForm
from account.models import Weight, Height, Position, Score, Parent, Coach, Personal, TargetSchoolsList, Account
from django import forms


class WeightForm(ModelForm):

	class Meta:
		model = Weight
		exclude = ('account', 'created_date')
		
class HeightForm(ModelForm):

	class Meta:
		model = Height
		exclude = ('account', 'created_date')
		
class PositionForm(ModelForm):

	class Meta:
		model = Position
		exclude = ('account', 'created_date')
		
class ScoreForm(ModelForm):

	class Meta:
		model = Score
		exclude = ('account', 'created_date')
		
class CoachForm(ModelForm):

	class Meta:
		model = Coach
		exclude = ('account', 'created_date', 'facebook', 'twitter', 'instagram')

class PhotoForm(ModelForm):

	class Meta:
		model = Account
		exclude = ('account', 'user', 'high_school', 'college', 'grad_year',  'created_date', 'club', 'throws', 'bats', 'grad_class', 'eligible', 'dob', 'team_image', 'ghost_id')
		
class TeamPhotoForm(ModelForm):

	class Meta:
		model = Account
		exclude = ('account', 'user', 'high_school', 'college', 'grad_year',  'created_date', 'club', 'throws', 'bats', 'grad_class', 'eligible', 'dob', 'profile_image', 'ghost_id')
		
		
class SchoolForm(ModelForm):

	class Meta:
		model = Account
		exclude = ('account', 'user', 'profile_image', 'team_image', 'created_date', 'ghost_id')
		
class GhostForm(ModelForm):

	class Meta:
		model = Account
		exclude = ('account', 'user', 'high_school', 'college', 'grad_year',  'created_date', 'club', 'throws', 'bats', 'grad_class', 'eligible', 'dob', 'team_image', 'profile_image')
		
class PersonalForm(ModelForm):

	class Meta:
		model = Personal
		exclude = ('account', 'created_date', 'fname', 'lname', 'company', 'note')
		
class ParentForm(ModelForm):

	class Meta:
		model = Parent
		exclude = ('account', 'created_date', 'facebook', 'twitter', 'instagram')
		
class TargetSchoolsListForm(ModelForm):

	class Meta:
		model = TargetSchoolsList
		exclude = ('account', 'created_date', 'ghost_id')
		target_schools = forms.SelectMultiple