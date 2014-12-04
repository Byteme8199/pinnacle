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
	scout = models.CharField("Scout", max_length=255, blank=True, null=True)
	note = models.TextField("Physical Description", blank=True, null=True)
	note2 = models.TextField("Abilities", blank=True, null=True)	
	note3 = models.TextField("Weaknesses", blank=True, null=True)	
	note4 = models.TextField("Signability and Player Summation", blank=True, null=True)
	dates_seen = models.TextField("Dates Seen", blank=True, null=True)	
	ab_seen = models.CharField("At Bats Seen", max_length=255, blank=True, null=True)
 	games_seen = models.CharField("Games Seen", max_length=255, blank=True, null=True)
	report_count = models.CharField("Report Count", max_length=255, blank=True, null=True)
	date_completed = models.DateTimeField("Date completed", default=timezone.now())
	makeup = models.CharField("Makeup", max_length=255, blank=True, null=True)
	role = models.CharField("Role:", max_length=255, blank=True, null=True)
	ofp = models.CharField("OFP", max_length=255, blank=True, null=True)
	
	def ranks(self):
		return CriterionRank.objects.filter(scoutsheet=self.id)
	
	def __unicode__(self):
		return unicode('[' + self.account.user.last_name + '] ' + self.note)
	
	class Meta:
		ordering = ['-created_date']
		verbose_name_plural = "Scout Sheets"
