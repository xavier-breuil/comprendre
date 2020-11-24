"""
Models for meetins app.
"""
from django.db import models

from taggit.managers import TaggableManager

from comprendre.users.models import User


class Meeting(models.Model):
    """
    Generic meeting model.
    """
    place = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()
    description = models.TextField()
    tags = TaggableManager()
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        """
        Meta for meetings
        """
        ordering = ['-start_time']


class Conference(Meeting):
    """
    Specificities for a conference.
    """
    speaker_group = models.ManyToManyField(User, related_name='conf_as_speaker')
    attender_group = models.ManyToManyField(User, related_name='conf_as_attender')
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=400, blank=True, null=True)


class Volunteering(Meeting):
    """
    Specificities for volunteering.
    """
    title = models.CharField(max_length=100)
    host = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=True,
        related_name='volunteering_as_host')
    helper_group = models.ManyToManyField(User, related_name='volunteering_as_helper')
