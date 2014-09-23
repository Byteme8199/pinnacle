from django.contrib import admin
from account.models import Height, Weight, Score, Account, Position, Coach, Parent, TargetSchoolsList
from project.utils import Contact
from django.db import models

class HeightInline(admin.TabularInline):
	model = Height
	fields = ('height_feet', 'height_inches', 'created_date','note')
	readonly_fields = ['created_date']
	extra = 0
	
class WeightInline(admin.TabularInline):
	model = Weight
	fields = ('weight', 'created_date','note')
	readonly_fields = ['created_date']
	extra = 0
	
class ScoreInline(admin.TabularInline):
	model = Score
	fields = ('score_type', 'score_data', 'created_date','note')
	readonly_fields = ['created_date']
	extra = 0
	
class PositionInline(admin.TabularInline):
	model = Position
	fields = ('position_type', 'position', 'created_date','note')
	readonly_fields = ['created_date']
	extra = 0
	
class CoachInline(admin.StackedInline):
	model = Coach
	fields = (('fname', 'lname'), 'phone', 'email', 'created_date','note')
	readonly_fields = ['created_date']
	extra = 0
	
class ParentInline(admin.StackedInline):
	model = Parent
	fields = (('fname', 'lname'), 'phone', 'email', 'created_date','note')
	readonly_fields = ['created_date']
	extra = 0

class TargetSchoolsListInline(admin.StackedInline):
	model = TargetSchoolsList
	fields = ('target_schools', 'chosen_school', 'created_date','note')
	readonly_fields = ['created_date']
	extra = 0

class AccountAdmin(admin.ModelAdmin):
	inlines = [WeightInline, HeightInline, ScoreInline, PositionInline, CoachInline, ParentInline, TargetSchoolsListInline]
	
admin.site.register(Account, AccountAdmin)