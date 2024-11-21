from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_boilerplate.apps.my_apps'
