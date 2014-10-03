from django.db import models
from project.utils import Contact
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.mail import send_mail
from recruiter.models import TargetSchool

def send_email(subject, message, from_email, to_email):
    send_mail(subject, message, from_email, to_email)
	
	
class Account(models.Model):
	user = models.OneToOneField(User, related_name='account')
	created_date = models.DateTimeField(default=timezone.now())
	high_school = models.CharField(max_length=255, null=True, blank=True)
	college = models.CharField(max_length=255, null=True, blank=True)
	grad_year = models.PositiveIntegerField(max_length=4, null=True, blank=True)

	#target_school = models.ManyToManyField(TargetSchool, null=True, blank=True)
	
	def weights(self):
		return Weight.objects.filter(account=self.user)

	def heights(self):
		return Height.objects.filter(account=self.user)

	def positions(self):
		return Position.objects.filter(account=self.user)

	def personals(self):
		return Personal.objects.filter(account=self.user)
	
	def coaches(self):
		return Coach.objects.filter(account=self.user)

	def parents(self):
		return Parent.objects.filter(account=self.user)

	def scores(self):
		return Score.objects.filter(account=self.user)
	
	def target_lists(self):
		return TargetSchoolsList.objects.filter(account=self.user)

	def __unicode__(self):
		return unicode('[' + self.user.username + '] ' + self.user.first_name + ' ' + self.user.last_name)

	class Meta:
		ordering = ['-created_date']
	
	def save(self, *args, **kwargs):
		account = self.user.first_name + ' ' + self.user.last_name
		now = timezone.now()
		
		subject = "Account Update: " + account
		message = account + "'s Account has been updated. <a href='http://pinnacleprospects.net/admin/account/account/" + str(self.id) + "'>Click Here to view the changes</a><br />The update occured at " + str(now)
		from_email = 'ryan@hdvideoandwebdesign.com'
		to_email = ['rgordon@golfweek.com', '']
		
		send_email(subject, message, from_email, to_email)

		super(Account,self).save(*args, **kwargs)

class Position(models.Model):
	account = models.ForeignKey(Account)
	created_date = models.DateTimeField(default=timezone.now())
	position = models.CharField(max_length=255, null=True, blank=True)
	PRIMARY = 'Primary'
	SECONDARY = 'Secondary'
	TERTIARY = 'Tertiary'
	POSITION_CHOICES = ((PRIMARY, 'Primary'),(SECONDARY, 'Secondary'),(TERTIARY, 'Tertiary'))
	position_type = models.CharField(max_length=10, choices=POSITION_CHOICES, default=PRIMARY)
	note = models.TextField(blank=True, null=False)

	class Meta:
		ordering = ['-created_date']

class Personal(Contact):
	account = models.ForeignKey(Account)
	pass
		
class Coach(Contact):
	account = models.ForeignKey(Account)
	pass

class Parent(Contact):
	account = models.ForeignKey(Account)
	pass

class TargetSchoolsList(models.Model):
	account = models.ForeignKey(Account)
	created_date = models.DateTimeField(default=timezone.now())
	target_schools = models.ManyToManyField(TargetSchool, null=True, blank=True)
	chosen_school = models.ForeignKey(TargetSchool, related_name='target_schools')
	note = models.TextField(blank=True, null=False)

class Height(models.Model):
	account = models.ForeignKey(Account)
	created_date = models.DateTimeField(default=timezone.now())
	height_feet = models.PositiveIntegerField()
	height_inches = models.PositiveIntegerField()
	note = models.TextField(blank=True, null=False)
	tot_inches = models.SmallIntegerField(blank=True, null=False, editable=False)
	def __unicode__(self):
		return unicode(str(self.height_feet) + "' " + str(self.height_inches) + '"' )

	def save(self, *args, **kwargs):
		self.tot_inches = (self.height_feet * 12) + self.height_inches
		super(Height,self).save(*args, **kwargs)
		
	class Meta:
		ordering = ['created_date']

class Weight(models.Model):
	account = models.ForeignKey(Account)
	created_date = models.DateTimeField(default=timezone.now())
	weight = models.DecimalField(max_digits=6, decimal_places=2)
	note = models.TextField(blank=True, null=False)

	def __unicode__(self):
		return unicode(self.weight)

	class Meta:
		ordering = ['created_date']

class Score(models.Model):
	account = models.ForeignKey(Account)
	created_date = models.DateTimeField(default=timezone.now())
	score_data = models.DecimalField(max_digits=6, decimal_places=2)
	ACT = 'ACT'
	SAT = 'SAT'
	GPA = 'GPA'
	SCORE_CHOICES = ((ACT, 'ACT'),(SAT, 'SAT'),(GPA, 'GPA'))
	score_type = models.CharField(max_length=10, choices=SCORE_CHOICES, default=GPA)
	note = models.TextField(blank=True, null=False)

	def __unicode__(self):
		return unicode(self.score_data)

	class Meta:
		ordering = ['-created_date']
	
