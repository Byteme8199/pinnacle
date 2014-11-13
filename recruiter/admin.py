from django.contrib import admin
from account.models import Account
from recruiter.models import TargetSchool, Coach
from project.utils import Contact
from django.db import models

class CoachInline(admin.StackedInline):
	model = Coach
	fields = (('fname', 'lname'), 'phone', 'email', 'created_date','note')
	readonly_fields = ['created_date']
	extra = 0	
	
class TargetSchoolInline(admin.StackedInline):
	model = TargetSchool
	fields = ('school','note')
	
class TargetSchoolAdmin(admin.ModelAdmin):
	fields = ('school', 'note')
	inlines = [CoachInline,]
	# eventually images?
	
admin.site.register(TargetSchool, TargetSchoolAdmin)
