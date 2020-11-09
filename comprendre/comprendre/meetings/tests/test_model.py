"""
Model test case for app user.
"""
import datetime

from django.test import TestCase
from django.utils.timezone import now

from comprendre.meetings.models import Conference

class MeetingModelTestCase(TestCase):
    """
    Meeting models tests.
    """
    def test_conference_filtrable_by_tags(self):
        """
        Check that a tag can be added to a conference.
        """
        conf = Conference.objects.create(
            place='here',
            start_time=now(),
            stop_time=now() + datetime.timedelta(hours=2),
            description=('we will talk about farming'),
            title=('can we feed the country with small surface farms'))
        conf.tags.add('agriculture')
        self.assertTrue(conf in Conference.objects.filter(tags__name__in=['agriculture']))
        self.assertFalse(conf in Conference.objects.filter(tags__name__in=['telecom']))
