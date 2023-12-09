from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models

from backend.utils.db.models import UUIDPrimaryKeyMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        """Create a custom user with the given fields."""
        if not email:
            raise ValidationError('Email must be provided')
        user = self.model(email=self.normalize_email(email), **kwargs)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        """Create a custonm superuser with the given fields."""
        kwargs['is_superuser'] = True
        user = self.create_user(email, password=password, **kwargs)
        return user


class User(AbstractBaseUser, UUIDPrimaryKeyMixin, PermissionsMixin):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField('Primary Email', max_length=100, unique=True, null=False, blank=False)

    first_name = models.CharField(max_length=128)

    last_name = models.CharField(max_length=128)

    is_active = models.BooleanField(
        default=True,
        help_text='Inactive accounts are removed from background tasks and other computations.',
    )

    email_verified = models.BooleanField(
        default=False,
        help_text='Users must verify their emails before fully joining the platform.',
    )

    objects = UserManager()

    class Meta:
        db_table = 'users'
        default_related_name = 'users'
        ordering = ['email']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self) -> str:
        return self.email

    @property
    def is_staff(self):
        return self.is_superuser
