from django.apps import AppConfig

class CommentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mysite.comments'  # <--- THIS MUST MATCH INSTALLED_APPS EXACTLY