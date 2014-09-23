from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from account.models import Account

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
	criterion = models.ForeignKey(Criterion)
	scoutsheet = models.ForeignKey("ScoutSheet")
	account = models.ForeignKey(Account)
	
	def __unicode__(self):
		return unicode('[' + self.criterion.name + '] ' + str(self.rank) )
	
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
