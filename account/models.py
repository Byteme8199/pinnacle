import smtplib
from django.conf import settings
from django.db import models
from project.utils import Contact
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.mail import send_mail
from recruiter.models import TargetSchool
from video.tasks import send_the_email

def upload_path_handler(instance, filename):
	return "./profiles/%s/%s" % (instance.user.username, filename)

def upload_path_handler_2(instance, filename):
	return "./profiles/%s/%s" % (instance.account.user.username, filename)

def upload_path_handler_carousel(instance, filename):
	return "./carousel_images/%s" % (filename)

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
		return CarouselImage.objects.all()

	def memos(self):
		return UserMemo.objects.filter(account=self.id)

	def target_lists(self):
		return TargetSchoolsList.objects.filter(account=self.id)

	def __unicode__(self):
		return unicode(self.user.first_name + ' ' + self.user.last_name)

	class Meta:
		ordering = ['-created_date']

	def save(self, *args, **kwargs):
		account = self.user.first_name + ' ' + self.user.last_name
		now = timezone.now()

		subject = "Account Update: " + account
		message = account + "'s Account has been updated. <a href='http://pinnacleprospects.net/admin/account/account/" + str(self.id) + "'>Click Here to view the changes</a><br />The update occured at " + str(now)
                from_email = 'pinnacleprospects@gmail.com'
		to_email = ['ryan@hdvideoandwebdesign.com', '']

		send_the_email.delay(subject, message, from_email, to_email)

		super(Account,self).save(*args, **kwargs)

class CarouselImage(models.Model):
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

	class Meta:
		ordering = ['-created_date']

class Personal(Contact):
	account = models.ForeignKey(Account)
	pass

class Coach(Contact):
	account = models.ForeignKey(Account)
	#pass

	class Meta:
		verbose_name_plural = "Coaches"

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

