from django.db import models
from django.utils.translation import ugettext_lazy as _

#from core.models import License


'''
Abstract model classes
'''


class AbstractLicenseModel(models.Model):
    '''
    Abstract class that adds license information to a model
    '''

    class Meta:
        abstract = True

    #license = models.ForeignKey(License,
    #                            verbose_name=_('License'),
    #                            default=1)
    #'''The item's license'''

#    license_author = models.CharField(verbose_name=_('Author'),
#                                      max_length=50,
#                                      blank=True,
#                                      null=True,
#                                      help_text=_('If you are not the author, enter the name or '
#                                                  'source here. This is needed for some licenses '
#                                                  'e.g. the CC-BY-SA.'))
#    '''The author if it is not the uploader'''


class AbstractSubmissionModel(models.Model):
    '''
    Abstract class used for model for user submitted data.

    These models have to be approved first by an administrator before they are
    shows in the website. There is also a manager that can be used:
    utils.managers.SubmissionManager
    '''

    class Meta:
        abstract = True

    STATUS_PENDING = '1'
    STATUS_ACCEPTED = '2'
    STATUS_DECLINED = '3'

    STATUS = (
        (STATUS_PENDING, _('Pending')),
        (STATUS_ACCEPTED, _('Accepted')),
        (STATUS_DECLINED, _('Declined')),
    )

    status = models.CharField(max_length=2,
                              choices=STATUS,
                              default=STATUS_PENDING,
                              editable=False)
    '''Status of the submission, e.g. accepted or declined'''
