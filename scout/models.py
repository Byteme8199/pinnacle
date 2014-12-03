from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from account.models import Account

class CriterionScaleRow(models.Model):
	rank = models.CharField(max_length=255, blank=False, null=False)
	column_one = models.CharField(max_length=255, blank=False, null=False)
	column_two = models.CharField(max_length=255, blank=True, null=True)
	scale = models.ForeignKey("CriterionScale")
	
	class Meta:
		ordering = ['rank']
		verbose_name_plural = "Grade"
	
class CriterionScale(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False)
	column_one_name = models.CharField(max_length=255, blank=False, null=False)
	column_two_name = models.CharField(max_length=255, blank=True, null=True)
	
	class Meta:
		verbose_name_plural = "Grading Scales"
		
	def __unicode__(self):
		return unicode(self.name)

class Criterion(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False)
	
	def __unicode__(self):
		return unicode(self.name)
		
	class Meta:
		ordering = ['name']
		verbose_name_plural = "criteria"
		
class CriterionRank(models.Model):
	rank = models.PositiveIntegerField()
	created_date = models.DateTimeField(default=timezone.now())
	#criterion = models.ForeignKey(CriterionScale)
	scoutsheet = models.ForeignKey("ScoutSheet")
	scale = models.ForeignKey("CriterionScale")
	#account = models.ForeignKey(Account)
	
	def __unicode__(self):
		return unicode('[' + self.scale.name + '] - ' + str(self.rank) )
	
	class Meta:
		ordering = ['-created_date']
		verbose_name_plural = "Rankings"
	
class ScoutSheet(models.Model):
	account = models.ForeignKey(Account)
	created_date = models.DateTimeField(default=timezone.now())
	note = models.TextField(blank=True, null=False)	
	
	def ranks(self):
		return CriterionRank.objects.filter(scoutsheet=self.id)
	
	def __unicode__(self):
		return unicode('[' + self.account.user.last_name + '] ' + self.note)
	
	class Meta:
		ordering = ['-created_date']
		verbose_name_plural = "Scout Sheets"
