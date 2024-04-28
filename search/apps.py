from django.apps import AppConfig


class SearchConfig(AppConfig):
    name = 'search'
    
class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Personal-Blog'