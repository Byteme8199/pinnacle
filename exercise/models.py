from django.db import models
from django.utils import timezone
from django.db import models

# Create your models here.

class ExerciseName(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True, null=True)
	#video = models.FileField(upload_to='./videos/exercises/', blank=True, null=True)
	file = models.FileField(upload_to='./videos/exercises/', blank=True, null=True)

	def video(self):
		path = ExerciseName.objects.filter(pk=self.id)
		return path[0].file.path.replace("/srv/sites/pindev/project", "")
	
	def __unicode__(self):
		return u"%s" % self.name

	class Meta:
		ordering = ['name']
		verbose_name_plural = "Exercise Videos"	
