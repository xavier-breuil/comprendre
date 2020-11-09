"""
Comprendre URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from comprendre.meetings.v1.urls import comp_router_v1


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^v1/', include((comp_router_v1.urls, 'v1'), namespace='v1'))
]
