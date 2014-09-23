from __future__ import absolute_import

from celery.task import task
import subprocess
from django.core.mail import send_mail
from time import sleep
	

@task
def compress_video(filename, newpath, newthumb, id):

	args = ['/usr/bin/ffmpeg', '-i', str(filename), '-y', '-vf', 'scale=600:-1', '-vcodec', 'libx264', '-strict', '-2', str(newpath)]	
	
	p = subprocess.Popen(args)

	return newpath

	
	
@task
def compress_reply(filename, newpath, newthumb, id):

	args = ['/usr/bin/ffmpeg', '-i', str(filename), '-y', '-vf', 'scale=600:-1', '-vcodec', 'libx264', '-strict', '-2', str(newpath)]	
	
	p = subprocess.Popen(args)

	return newpath


@task
def compress_thumbnail(filename, newpath, newthumb, id):
	
	args = ['/usr/bin/ffmpeg', '-itsoffset', "-4", "-i", str(filename), '-y', '-vcodec', 'mjpeg', '-vframes', '1', '-an', '-f', "rawvideo", "-s", "320x240", str(newthumb)]
	
	p = subprocess.Popen(args)

	return newthumb
	
	
@task
def send_email(vid_id, vid_type):
	
	#### EMAIL NOTIFICATION ####
	account = self.account.user.first_name + ' ' + self.account.user.last_name
	now = timezone.now()

	title = "Video Update: " + account
	message = account + " has uploaded a new video. <a href='http://pinnacleprospects.net/admin/video/video/" + str(self.id) + "'>Click Here to view the changes</a><br />The update occured at " + str(now)
	from_email = 'ryan@hdvideoandwebdesign.com'
	to_email = 'rgordon@golfweek.com'
	#send_mail(title, message, from_email, [to_email], fail_silently=False)
	
	
	
@task
def get_er_done(vid_id, vid_type):
	
	from video.models import Video, VideoReply
	
	if vid_type == "Video":
		vid = Video.objects.get(pk=vid_id)
	else:
		vid = VideoReply.objects.get(pk=vid_id)
		
	split = vid.file.path.split('/')	
	newsplit = split[8].split('.')

	filename = newsplit[0]

	if vid_type == "Video":
		new_path = vid.file.path.replace(filename, str(vid.account.id) + "-" + str(vid.id))
	else:	
		new_path = vid.file.path.replace(filename, str(vid.account.id) + "-" + str(vid.id) + '-reply')

	if vid_type == "Video":
		new_thumb = vid.file.path.replace(split[8], str(vid.account.id) + "-" + str(vid.id) + ".jpg")
	else:
		new_thumb = vid.file.path.replace(split[8], str(vid.account.id) + "-" + str(vid.id) + "-reply.jpg")
	
	if vid_type == "Video":
		thumb_status = compress_thumbnail.delay(vid.file.path, new_path, new_thumb, vid_id)
		video_status = compress_video.delay(vid.file.path, new_path, new_thumb, vid_id)
	else:
		thumb_status = compress_thumbnail.delay(vid.file.path, new_path, new_thumb, vid_id)
		video_status = compress_reply.delay(vid.file.path, new_path, new_thumb, vid_id)

	#return video_status
	