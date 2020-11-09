"""
Module to register classes in admin interface.
"""
from django.contrib import admin

from .models import Conference, Volunteering


admin.site.register(Conference)
admin.site.register(Volunteering)
