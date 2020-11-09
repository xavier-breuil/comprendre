"""
Module to register classes in admin interface.
"""
from django.contrib import admin

from .models import User


admin.site.register(User)
