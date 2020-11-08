"""
Module for user models.
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from comprendre.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    User model.
    """
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
