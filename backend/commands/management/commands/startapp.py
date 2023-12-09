import os
from typing import Any

from django.conf import settings
from django.core.management.commands import startapp


class Command(startapp.Command):
    """Override the default 'startapp' command to dump it under 'api/apps'."""

    DIRECTORY_FLAG = 'directory'

    def handle(self, *args: Any, **options: Any) -> str | None:
        """Update the 'directory' option to create the app under 'api/apps'."""
        app_name = options.get('name', 'null')
        if not options.get(self.DIRECTORY_FLAG, None):
            options[self.DIRECTORY_FLAG] = str(settings.BASE_DIR / 'apps' / app_name)
            if not os.path.isdir(options[self.DIRECTORY_FLAG]):
                os.mkdir(options[self.DIRECTORY_FLAG])

        return super().handle(*args, **options)
