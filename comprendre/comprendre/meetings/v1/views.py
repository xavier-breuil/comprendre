"""
Meeting API for version 1.
"""
from rest_framework import viewsets
import django_filters

from comprendre.meetings.models import Conference
from comprendre.meetings.v1.serializers import ConferenceSerializerV1


class ConferenceFilter(django_filters.FilterSet):
    """
    Custom filters for conferences and volunteerings.
    """
    tags = django_filters.CharFilter(field_name='tags', method='filter_tags')

    # required signature necessits to disable pylint.
    def filter_tags(self, queryset, name, value): # pylint: disable=unused-argument, no-self-use
        """
        Handle tags filtering.
        tags - Tags must be passed as a string, seperated with coma.
        it returns the conference that match at least one tag of the list.
        eg: ?tags=django,react return the conferences that are tags with either
        django or react or both.
        start_time - a UTC datetime string that matchs the format yyyy-mm-ddThh:mm:ssZ
        """
        tag_names = value.split(',')
        return queryset.filter(tags__name__in=tag_names)

    class Meta:
        """
        Allow filtering against place, tags and start_time.
        """
        model = Conference
        fields = ['place', 'tags', 'start_time']


class ConferenceViewSetV1(viewsets.ModelViewSet): # pylint: disable=too-many-ancestors
    """
    Viewset for conference objects.
    """
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializerV1
    filterset_class = ConferenceFilter
