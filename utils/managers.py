from django.db import models
from django.db.models.query import QuerySet
from utils.models import AbstractSubmissionModel


'''
Custom managers and querysets
'''

# TODO: starting with django 1.7 this is simplified, see
#       https://docs.djangoproject.com/en/1.7/topics/db/managers/#creating-manager-with-queryset-methods


class SubmissionQuerySet(QuerySet):
    def accepted(self):
        return self.filter(status=AbstractSubmissionModel.STATUS_ACCEPTED)

    def pending(self):
        return self.filter(status=AbstractSubmissionModel.STATUS_PENDING)


class SubmissionManager(models.Manager):
    use_for_related_fields = True

    def get_queryset(self):
        return SubmissionQuerySet(self.model, using=self._db)

    def accepted(self):
        return self.get_queryset().accepted()

    def pending(self):
        return self.get_queryset().pending()
