from __future__ import unicode_literals

from django.db import models
from base.models import AbstractDateTimeModel


class Task(AbstractDateTimeModel):
    assignee = models.ForeignKey('users.User', related_name='assignee', null=True, on_delete=models.CASCADE)
    created_by = models.ForeignKey('users.User', related_name='created_by', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    money = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
