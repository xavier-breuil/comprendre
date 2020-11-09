"""
Meeting serializers for version 1.
"""
from rest_framework import serializers

from comprendre.meetings.models import Conference


class ConferenceSerializerV1(serializers.ModelSerializer):
    """
    Version one of seriializer for confenrence objects.
    """
    class Meta:
        """
        Serve all field of conference object.
        """
        model = Conference
        fields = '__all__'
