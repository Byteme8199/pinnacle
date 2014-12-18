from __future__ import absolute_import

from celery import shared_task

# from django.core.mail import send_mail
# from time import sleep

# from video.models import Video

from django.conf import settings
#import smtplib

import json
import requests

from subprocess import check_output

@shared_task
def send_the_email(subject, message, from_email, to_email):
        #msg =  "From: PinnacleProspects <pinnacleprospects@gmail.com>\n"
        #msg += "To: Ryan <ryan@hdvideoandwebdesign.com>\n"
        #msg += "MIME-Version: 1.0\n"
        #msg += "Content-type: text/html\n"
        #msg += "Subject: " + subject + "\n"
        #msg += "\n\n" + message
        try:
		mail = {
	    		"key": settings.EMAIL_KEY,
    			"message": {
	        		"html": message,
        			"subject": subject,
        			"from_email": settings.EMAIL_HOST_USER,
        			"from_name": "Jason",
        			"to": [
            				{
                			"email": "ryan@hdvideoandwebdesign.com",
                			"name": "Ryan",
                			"type": "to"
            				}
        			],
        			"headers": {
            				"Reply-To": "jason@notthatjason.com"
		        		},
		    		},
		    		"async": False
		}

		mail_json = json.dumps(mail)
		r = requests.post('https://mandrillapp.com/api/1.0/messages/send.json', data=mail_json)
               #server = smtplib.SMTP(settings.EMAIL_HOST + ":" + str(settings.EMAIL_PORT))
               #print 'starting tls'
               #server.starttls()
               #print 'logging in'
               #server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
               #print 'sending mail'
               #server.sendmail(from_email, to_email, msg)
               #server.quit()
        except Exception, e:
               print "Connection failed"



@shared_task
def make_thumbnail(path, new_name):

    # Make Thumbnail
    check_output(["ffmpeg", "-itsoffset", "-4", "-i", str(path), "-y", "-vcodec", "mjpeg", "-vframes", "1", "-an", "-f", "rawvideo", "-s", "320x240", str(new_name)])
    print 'WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'
