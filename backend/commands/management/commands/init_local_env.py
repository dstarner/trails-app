import time

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    EMAIL = 'admin@localhost'
    PASSWORD = 'hunter2'

    def handle(self, *args, **options):
        self.stdout.write('Sleeping for 10 seconds to wait for migrations')
        time.sleep(10)

        User = get_user_model()

        user = None if User.objects.filter(email=self.EMAIL).exists() else User.objects.create_superuser(
            email=self.EMAIL, password=self.PASSWORD, first_name='Admin', last_name='McAdmin',
        )
        self.stdout.write(
            f"!! '{self.EMAIL}:{self.PASSWORD}' user already exists !!",
        ) if not user else self.stdout.write(self.style.SUCCESS(
            f"!! '{self.EMAIL}' user created with password '{self.PASSWORD}' !!",
        ))
