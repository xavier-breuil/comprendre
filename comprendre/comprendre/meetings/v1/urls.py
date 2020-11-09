"""
Urls for meeting app.
"""
from rest_framework import routers

from comprendre.meetings.v1.views import ConferenceViewSetV1


comp_router_v1 = routers.SimpleRouter()
comp_router_v1.register(r'^conference', ConferenceViewSetV1, basename='conferences')
