from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'posts'

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Personal-Blog'