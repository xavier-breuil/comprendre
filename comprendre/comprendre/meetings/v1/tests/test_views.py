"""
Test v1 views.
"""
import json

from django.urls import reverse
from django.utils.http import urlencode
from rest_framework.test import APITestCase
from taggit.models import Tag

from comprendre.meetings.models import Conference, Volunteering


class MeetingViewTestCase(APITestCase):
    """
    Conference view test class.
    """
    fixtures = ['users', 'meetings', 'taggit']

    def setUp(self):
        """
        Associate tags to meetings.
        TODO: Find a cleaner way to do this, like in the fixtures for instance.
        """
        conf_1 = Conference.objects.get(pk=1)
        conf_1.tags.add(Tag.objects.get(pk=1))
        conf_2 = Conference.objects.get(pk=2)
        conf_2.tags.add(Tag.objects.get(pk=2))
        conf_2.tags.add(Tag.objects.get(pk=3))
        vol = Volunteering.objects.get(pk=3)
        vol.tags.add(Tag.objects.get(pk=4))

    def test_conference_pagination(self):
        """
        Ensure that view is paginated.
        """
        conference_url = '%s' % reverse('v1:conferences-list')
        response = json.loads(self.client.get(conference_url).content)
        self.assertTrue('results' in response.keys())
        self.assertTrue('next' in response.keys())
        self.assertTrue('previous' in response.keys())

    def test_conference_filtering(self):
        """
        Make sure conference can be filtered by tag, place and date.
        """
        filt_url = '%s?%s' % (reverse('v1:conferences-list'), urlencode({'place': 'toulouse'}))
        response = json.loads(self.client.get(filt_url).content)['results']
        self.assertTrue(len(response)==1)
        self.assertTrue(response[0]['id']==2)
        filt_url = '%s?%s' % (reverse('v1:conferences-list'), urlencode({'tags': 'iot'}))
        response = json.loads(self.client.get(filt_url).content)['results']
        self.assertTrue(len(response)==1)
        self.assertTrue(response[0]['id']==2)
        filt_url = '%s?%s' % (
            reverse('v1:conferences-list'),
            urlencode({'start_time': '1989-07-10T10:00:00Z'}))
        response = json.loads(self.client.get(filt_url).content)['results']
        self.assertTrue(len(response)==1)
        self.assertTrue(response[0]['id']==1)

    def test_volunteering_filtering(self):
        """
        Make sure volunteering can be filtered by tag, place and date.
        """
        filt_url = '%s?%s' % (reverse('v1:volunteerings-list'), urlencode({'place': 'toulouse'}))
        response = json.loads(self.client.get(filt_url).content)['results']
        self.assertTrue(len(response)==0)
        filt_url = '%s?%s' % (reverse('v1:volunteerings-list'), urlencode({'tags': 'help'}))
        response = json.loads(self.client.get(filt_url).content)['results']
        self.assertTrue(len(response)==1)
        self.assertTrue(response[0]['id']==3)
        filt_url = '%s?%s' % (
            reverse('v1:volunteerings-list'),
            urlencode({'start_time': '2020-11-10T10:47:30Z'}))
        response = json.loads(self.client.get(filt_url).content)['results']
        self.assertTrue(len(response)==1)
        self.assertTrue(response[0]['id']==3)
