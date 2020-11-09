"""
Urls for meeting app.
"""
from rest_framework import routers

from comprendre.meetings.v1.views import ConferenceViewSetV1, VolunteeringViewSetV1


comp_router_v1 = routers.SimpleRouter()
comp_router_v1.register(r'conferences', ConferenceViewSetV1, basename='conferences')
comp_router_v1.register(r'volunteerings', VolunteeringViewSetV1, basename='volunteerings')
