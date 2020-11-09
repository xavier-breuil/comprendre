"""
Test v1 views.
"""
import json

from django.urls import reverse
from rest_framework.test import APITestCase


class MeetingViewTestCase(APITestCase):
    """
    Conference view test class.
    """
    fixtures = ['users', 'meetings']

    def test_conference_pagination(self):
        """
        Ensure that view is paginated.
        """
        conference_url = '%s' % reverse('v1:conferences-list')
        response = json.loads(self.client.get(conference_url).content)
        self.assertTrue('results' in response.keys())
        self.assertTrue('next' in response.keys())
        self.assertTrue('previous' in response.keys())
