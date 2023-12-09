
from django.apps import AppConfig
from django.conf import settings

# TODO: needed only if we use an API like django-ninja
# def autoreload_watch(sender, **kwargs):
#     """Add any non-Python files to autoreload the server on
#     """
#     sender.watch_dir(path.dirname(settings.NINJA_DOCS_DESCRIPTION_PATH), '*.md')
#     sender.watch_dir(path.dirname(settings.NINJA_DOCS_DESCRIPTION_PATH), '*.yaml')


class CommandsConfig(AppConfig):
    name = f'{settings.LOCAL_APP_IMPORT_ROOT}.commands'
    default = True

    # def ready(self):
    #     autoreload_started.connect(autoreload_watch)
