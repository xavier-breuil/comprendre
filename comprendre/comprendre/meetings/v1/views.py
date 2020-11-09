"""
Meeting API for version 1.
"""
from rest_framework import viewsets

from comprendre.meetings.models import Conference
from comprendre.meetings.v1.serializers import ConferenceSerializerV1


class ConferenceViewSetV1(viewsets.ModelViewSet): # pylint: disable=too-many-ancestors
    """
    Viewset for conference objects.
    """
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializerV1
