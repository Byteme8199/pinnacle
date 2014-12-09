from django.db import models
from django.utils import timezone

class Contact(models.Model):
	fname = models.CharField('first name', max_length=50)
	lname = models.CharField('last name', max_length=50)
	company = models.CharField(max_length=255, blank=True, null=True)
	street = models.CharField(max_length=255, blank=True, null=True)
	city = models.CharField(max_length=255, blank=True, null=True)
	state = models.CharField(max_length=2, blank=True, null=True) # change this to a dropdown ie ENUM type
	zipcode = models.PositiveIntegerField("Zip Code", max_length=5, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	email = models.EmailField(max_length=250, blank=True, null=True)
	facebook = models.CharField(max_length=255, blank=True, null=True)
	twitter = models.CharField(max_length=255, blank=True, null=True)
	instagram = models.CharField(max_length=255, blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now())
	note = models.TextField(blank=True, null=False)

	def __unicode__(self):
		return unicode(self.fname + ' ' + self.lname)

	class Meta:
		abstract = True





