from django.apps import AppConfig


class ContactConfig(AppConfig):
    name = 'contact'

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Personal-Blog'