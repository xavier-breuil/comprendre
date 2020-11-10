"""
Meeting serializers for version 1.
"""
from rest_framework import serializers

from comprendre.meetings.models import Conference, Volunteering


class ConferenceSerializerV1(serializers.ModelSerializer):
    """
    Version one of serializer for confenrence objects.
    """
    class Meta:
        """
        Serve all fields of conference object.
        """
        model = Conference
        fields = '__all__'


class VolunteeringSerializerV1(serializers.ModelSerializer):
    """
    Version one of serializer for volunteering objects.
    """
    class Meta:
        """
        Serve all fields of volunteering object.
        """
        model = Volunteering
        fields = '__all__'
