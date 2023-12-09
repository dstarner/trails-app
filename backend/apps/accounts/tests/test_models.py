from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import User


class UserManagerTestCase(TestCase):

    def test_create_user__no_email(self):
        with self.assertRaises(ValidationError):
            User.objects.create_user(None)

    def test_create_user__empty_email(self):
        with self.assertRaises(ValidationError):
            User.objects.create_user(None)

    def test_create_user__without_password(self):
        email = 'test@localhost'
        user: User = User.objects.create_user(email)

        self.assertEqual(type(user), User)
        self.assertEqual(email, user.email)
        self.assertFalse(user.has_usable_password())

    def test_create_user(self):
        email = 'test@localhost'
        password = 'hunter2'
        user: User = User.objects.create_user(email, password=password)

        self.assertEqual(type(user), User)
        self.assertEqual(email, user.email)
        self.assertTrue(user.has_usable_password())
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.first_name, '')  # make sure we do not set attributes
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_user__extra_kwargs(self):
        email = 'test@localhost'
        password = 'hunter2'
        kwargs = {'first_name': 'Hello', 'last_name': 'World'}
        user: User = User.objects.create_user(email, password=password, **kwargs)

        self.assertEqual(type(user), User)
        self.assertEqual(email, user.email)
        self.assertTrue(user.has_usable_password())
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.first_name, kwargs['first_name'])
        self.assertEqual(user.last_name, kwargs['last_name'])

    def test_create_superuser(self):
        email = 'test@localhost'
        password = 'hunter2'
        kwargs = {'first_name': 'Hello', 'last_name': 'World'}
        user: User = User.objects.create_superuser(email, password=password, **kwargs)

        self.assertEqual(type(user), User)
        self.assertEqual(email, user.email)
        self.assertTrue(user.has_usable_password())
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.first_name, kwargs['first_name'])
        self.assertEqual(user.last_name, kwargs['last_name'])
