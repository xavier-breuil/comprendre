"""
Model test case for app user.
"""
from django.test import TestCase
from comprendre.users.models import User

class UserModelTestCase(TestCase):
    """
    User models tests.
    """
    def test_user_create(self):
        """
        Check that a user is created.
        """
        user_count = User.objects.count()
        user = User.objects.create_user(email='test@test.com', password='test')
        self.assertTrue(User.objects.count() == user_count + 1)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        with self.assertRaises(ValueError, msg='The email must be provided'):
            User.objects.create_user(email='', password='test')

    def test_superuser_create(self):
        """
        Check that a superuser is created.
        """
        user_count = User.objects.count()
        super_user = User.objects.create_superuser(email='test@test.com', password='test')
        self.assertTrue(User.objects.count() == user_count + 1)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
        with self.assertRaises(ValueError, msg='Superuser must have is_staff=True'):
            User.objects.create_superuser(email='test@test.com', password='test', is_staff=False)
        with self.assertRaises(ValueError, msg='Superuser must have is_superuser=True'):
            User.objects.create_superuser(
                email='test@test.com',
                password='test',
                is_superuser=False)
