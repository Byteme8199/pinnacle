from django.forms import ModelForm
from recruiter.models import TargetSchool
from django import forms

		
class TargetSchoolForm(ModelForm):

	class Meta:
		model = TargetSchool