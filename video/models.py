from django.db import models
from project.utils import Contact
from account.models import Account
from django.utils import timezone
from django.core.mail import send_mail
from subprocess import check_output
from video.tasks import send_the_email

class VideoType(models.Model):
	name = models.CharField(max_length=100, blank=True, null=False)
	created_date = models.DateTimeField(default=timezone.now(), editable=False)

	def __unicode__(self):
		return unicode(self.name)

def upload_path_handler(instance, filename):
	return "./videos/%s/%s" % (instance.account.user.username, filename)

def upload_path_handler_reply(instance, filename):
	return "./videos/%s/%s" % (instance.parent.account.user.username, filename)

def make_thumbnail_and_compress(self, type):
	if type =='reply':
		vid = VideoReply.objects.get(pk=self.id)
	else:
		vid = Video.objects.get(pk=self.id)

	if not self.has_compressed:
		split = vid.file.path.split('/')
		newsplit = split[6].split('.')
		filename = newsplit[0]

		if type == 'reply':
			new_vid = vid.file.path.replace(split[8], "temp-" + str(self.parent.id) + ".mp4")
			new_thumb = vid.file.path.replace(split[8], str(self.parent.id) + "-" + str(self.id) + "-reply.jpg")
		else:
			new_vid = vid.file.path.replace(split[8], "temp-" + str(self.id) + ".mp4")
			new_thumb = vid.file.path.replace(split[8], str(self.id) + ".jpg")

		# internal server/external server
		thumbnail = new_thumb.replace("/srv/sites/pindev/project", "")


		#Make Thumbnail
		check_output(["ffmpeg", "-i", str(vid.file.path), "-ss", "00:00:00.100", "-f", "image2", "-vframes", "1", "-an", "-s", "320x240", str(new_thumb)])
		
		#Fix the God Damn Mutha Fucking Ass Reaming MetaData
		check_output(["ffmpeg", "-i", str(vid.file.path), "-metadata", "title=arbitrary", "-codec", "copy", str(new_vid)])
		check_output(["mv", str(new_vid), str(vid.file.path)])
		
		self.has_compressed = True
		self.save()
		
		fix_metadata.delay(vid.file.path)
		
	else:
		sp = self.file.path.split('/')
		if type =='reply':
			this = self.file.path.replace(sp[8], str(self.parent.id) + "-" + str(self.id) + '-reply.jpg')
		else:
			this = self.file.path.replace(sp[8], str(str(self.id) + '.jpg'))

		thumbnail = this.replace("/srv/sites/pindev/project", "")

	return thumbnail


class Video(models.Model):
	title = models.CharField(max_length=200)
	account = models.ForeignKey(Account)
	created_date = models.DateTimeField(default=timezone.now())
	note = models.TextField(blank=True, null=False)
	has_compressed = models.BooleanField(default=False,editable=False)
	video_type = models.ForeignKey(VideoType, blank=True, null=True)

	thumbnail_holder = models.CharField(max_length=200,null=True, blank=True)

	file = models.FileField(upload_to=upload_path_handler)

	def video(self):
		path = Video.objects.filter(pk=self.id)
		return path[0].file.path.replace("/srv/sites/pindev/project", "")

	def thumbnail(self):
		return make_thumbnail_and_compress(self, 'user')

	def videos(self):
		return Video.objects.filter(account=self.account)

	def replies(self):
		return VideoReply.objects.filter(parent=self.id)

	def photos(self):
		return PhotoReply.objects.filter(parent=self.id)

	def __unicode__(self):
		return unicode('[ %s %s ] %s' % (self.account.user.first_name, self.account.user.last_name, self.title))

	class Meta:
		ordering = ['-created_date']

	def save(self, *args, **kwargs):

		#### EMAIL NOTIFICATION ####
		account = self.account.user.first_name + ' ' + self.account.user.last_name
		now = timezone.now()

		title = "[Pinnacle Update] " + account + " Video Module"
		message = "Name: " + account + "\nUpdate: Video added or Updated\n@: " + str(now)

                send_the_email.delay(title, message)

		super(Video,self).save(*args, **kwargs)

class VideoReply(models.Model):
	parent = models.ForeignKey(Video)
	created_date = models.DateTimeField(default=timezone.now())
	note = models.TextField(blank=True, null=False)
	video_embed = models.CharField(max_length=200, blank=True, null=True)
	file = models.FileField(upload_to=upload_path_handler_reply)
	has_compressed = models.BooleanField(default=False,editable=False)

	def video(self):
		path = VideoReply.objects.filter(pk=self.id)
		return path[0].file.path.replace("/srv/sites/pindev/project", "")

	def replies(self):
		return VideoReply.objects.filter(account=self.parent.account)

	def thumbnail(self):
		return make_thumbnail_and_compress(self, 'reply')

	def __unicode__(self):
		return unicode('[ Video Reply ] %s' % (self.parent.title))

	class Meta:
		verbose_name_plural = "Video Replies"

class PhotoReply(models.Model):
	parent = models.ForeignKey(Video)
	created_date = models.DateTimeField(default=timezone.now())
	note = models.TextField(blank=True, null=False)
	file = models.FileField(upload_to=upload_path_handler_reply)

	def photo(self):
		photo = self.file.path
		return photo.replace('/srv/sites/pindev/project/', '/')

	def replies(self):
		return PhotoReply.objects.filter(account=self.parent.account)

	def __unicode__(self):
		return unicode('[ Photo Reply ] %s' % (self.parent.title))

	class Meta:
		verbose_name_plural = "Photo Replies"

