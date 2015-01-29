import smtplib
from django.conf import settings
from django.db import models
from project.utils import Contact
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.mail import send_mail
from recruiter.models import TargetSchool
from video.tasks import send_the_email
from django.core.urlresolvers import reverse

from datetime import datetime, timedelta


def upload_path_handler(instance, filename):
	return "./profiles/%s/%s" % (instance.user.username, filename)

def upload_path_handler_2(instance, filename):
	return "./profiles/%s/%s" % (instance.account.user.username, filename)

def upload_path_handler_carousel(instance, filename):
	return "./carousel_images/%s" % (filename)

def email(account, area, msg=None):
	now = timezone.now()
	subject = "[Pinnacle Update] for " + account + " in " + area
	if msg is None:
		message = "Name: " + account + "\nUpdate: " + area + " Info Added/Updated \n@: " + str(now)
	else:
		message = msg
	send_the_email.delay(subject, message)



class Account(models.Model):
	user = models.OneToOneField(User, related_name='account')
	created_date = models.DateTimeField(default=timezone.now())
	high_school = models.CharField(max_length=255, null=True, blank=True)
	college = models.CharField(max_length=255, null=True, blank=True)
	club = models.CharField("Club/National Team", max_length=255, null=True, blank=True)
	throws = models.CharField(max_length=5, null=True, blank=True)
	bats = models.CharField(max_length=5, null=True, blank=True)
	grad_year = models.PositiveIntegerField(max_length=10, null=True, blank=True)
	grad_class = models.CharField("Class", max_length=5, null=True, blank=True)
	eligible = models.PositiveIntegerField(max_length=10, null=True, blank=True)
	dob = models.CharField("Date of Birth", max_length=10, null=True, blank=True)
	profile_image = models.FileField(upload_to=upload_path_handler, null=True, blank=True)
	team_image = models.FileField(upload_to=upload_path_handler, null=True, blank=True)
	ghost_id = models.ForeignKey('self', null=True, blank=True)
	
	#target_school = models.ManyToManyField(TargetSchool, null=True, blank=True)

	def photo(self):
		photo = self.profile_image.path
		return photo.replace('/srv/sites/pindev/project/', '/')

	def team_photo(self):
		team = self.team_image.path
		return team.replace('/srv/sites/pindev/project/', '/')

	def weights(self):
		return Weight.objects.filter(account=self.id)

	def heights(self):
		return Height.objects.filter(account=self.id)

	def positions(self):
		return Position.objects.filter(account=self.id)

	def personals(self):
		return Personal.objects.filter(account=self.id)

	def coaches(self):
		return Coach.objects.filter(account=self.id)

	def parents(self):
		return Parent.objects.filter(account=self.id)

	def scores(self):
		return Score.objects.filter(account=self.id)

	def carousel_images(self):
		return CarouselImage.objects.filter(account=self.id).order_by('-created_date')
	
	def memos(self):
		return UserMemo.objects.filter(account=self.id).order_by('-created_date')

	def memos_count(self):
		return UserMemo.objects.filter(account=self.id, is_new=1).order_by('-created_date')

	def see_memos(self):
		UserMemo.objects.filter(account=self.id).update(is_new=0)
		pass

	def target_lists(self):
		return TargetSchoolsList.objects.filter(account=self.id)

	def __unicode__(self):
		return unicode(self.user.first_name + ' ' + self.user.last_name)

	class Meta:
		ordering = ['-created_date']

	def save(self, *args, **kwargs):
		msg = "General Account Info Updated"
		email(self.user.first_name + ' ' + self.user.last_name, 'Account', msg)
		super(Account,self).save(*args, **kwargs)
	
	def get_absolute_url(self):
		return reverse('guest_account', kwargs={'pk': self.pk})

class CarouselImage(models.Model):
	account = models.ForeignKey(Account)
	caption = models.TextField(blank=True, null=False)
	carousel_image = models.FileField(upload_to=upload_path_handler_carousel, null=True, blank=True)
	created_date = models.DateTimeField(default=timezone.now())

	def image(self):
		image_path = self.carousel_image.path
		return image_path.replace('/srv/sites/pindev/project/', '/')

	def __unicode__(self):
		return unicode(self.caption)

	class Meta:
		ordering = ['-created_date']

class UserMemo(models.Model):
	account = models.ForeignKey(Account)
	note = models.TextField(blank=True, null=False)
	note_image = models.FileField(upload_to=upload_path_handler_2, null=True, blank=True)
	created_date = models.DateTimeField(default=timezone.now())
	is_new = models.BooleanField(default=1)

	def memo_image(self):
		note = self.note_image.path
		return note.replace('/srv/sites/pindev/project/', '/')

	def __unicode__(self):
		return unicode(self.account.user.username + ': ' + self.note)

	class Meta:
		ordering = ['-created_date']

class Position(models.Model):
	account = models.ForeignKey(Account)
	created_date = models.DateTimeField(default=timezone.now())
	position = models.CharField(max_length=255, null=True, blank=True)
	PRIMARY = 'Primary'
	SECONDARY = 'Secondary'
	POSITION_CHOICES = ((PRIMARY, 'Primary'),(SECONDARY, 'Secondary'))
	position_type = models.CharField(max_length=10, choices=POSITION_CHOICES, default=PRIMARY)
	note = models.TextField(blank=True, null=False)

	def save(self, *args, **kwargs):
		msg = "Position updated to " + self.position + " as " + self.position_type
		email(self.account.user.first_name + ' ' + self.account.user.last_name, 'Position')
		super(Position,self).save(*args, **kwargs)
			
	class Meta:
		ordering = ['-created_date']

class Personal(Contact):
	account = models.ForeignKey(Account)
	
	def save(self, *args, **kwargs):
		email(self.account.user.first_name + ' ' + self.account.user.last_name, 'Personal')
		super(Personal,self).save(*args, **kwargs)

class Coach(Contact):
	account = models.ForeignKey(Account)
	
	def save(self, *args, **kwargs):
		msg = "New Coach Added / Updated"
		email(self.account.user.first_name + ' ' + self.account.user.last_name, 'Coach', msg)
		super(Coach,self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = "Coaches"

class Parent(Contact):
	account = models.ForeignKey(Account)
	
	def save(self, *args, **kwargs):
		email(self.account.user.first_name + ' ' + self.account.user.last_name, 'Parent')
		super(Parent,self).save(*args, **kwargs)

class TargetSchoolsList(models.Model):
	account = models.ForeignKey(Account)
	created_date = models.DateTimeField(default=timezone.now())
	target_schools = models.ManyToManyField(TargetSchool, null=True, blank=True)
	chosen_school = models.ForeignKey(TargetSchool, related_name='target_schools')
	note = models.TextField(blank=True, null=False)

	def save(self, *args, **kwargs):
		msg = self.chosen_school + " Added to Target Schools"
		email(self.account.user.first_name + ' ' + self.account.user.last_name, 'Target Schools', msg)	
		super(TargetSchoolsList,self).save(*args, **kwargs)

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
		msg = self.height_feet + "' " + self.height_inches + "\" Height Added"
		email(self.account.user.first_name + ' ' + self.account.user.last_name, 'Height', msg)
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
	
	def save(self, *args, **kwargs):
		msg = str(self.weight) + " lbs Added to Weights"
		email(self.account.user.first_name + ' ' + self.account.user.last_name, 'Weight', msg)
		super(Weight,self).save(*args, **kwargs)

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
	
	def save(self, *args, **kwargs):
		msg = self.score_data + " " + self.score_type + " Score Added"
		email(self.account.user.first_name + ' ' + self.account.user.last_name, 'Grade', msg)
		super(Score,self).save(*args, **kwargs)

	class Meta:
		ordering = ['-created_date']

