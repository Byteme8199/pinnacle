from django.db import models
from project.utils import Contact
from django.utils import timezone

class TargetSchool(models.Model):
	school = models.CharField(max_length=255, null=False, blank=False)
	note = models.TextField(blank=True, null=False)
	
	def __unicode__(self):
		return unicode(self.school)
		
class Coach(Contact):
	target_school = models.ForeignKey(TargetSchool)
	pass
