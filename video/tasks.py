from __future__ import absolute_import

from celery import shared_task

# from django.core.mail import send_mail
# from time import sleep

from django.conf import settings
#import smtplib

import json
import requests

# from subprocess import check_output

@shared_task
def send_the_email(subject, message):
        try:
		mail = {
	    		"key": settings.EMAIL_KEY,
    			"message": {
	        		"html": message,
        			"subject": subject,
        			"from_email": settings.EMAIL_HOST_USER,
        			"from_name": "Pinnacle",
        			"to": [
            				{
                			"email": "nrcrocker9@gmail.com",
                			"name": "Nick",
                			"type": "to"
            				}
        			],
        			"headers": {
            				"Reply-To": settings.EMAIL_HOST_USER
		        		},
		    		},
		    		"async": False
		}

		mail_json = json.dumps(mail)
		r = requests.post('https://mandrillapp.com/api/1.0/messages/send.json', data=mail_json)
        except Exception, e:
               print "Email send failed."


