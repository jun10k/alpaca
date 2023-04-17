from django.apps import AppConfig
from .digest import DigestThreadPool


class UploadsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'uploads'

    def ready(self):
        thread_pool = DigestThreadPool()
        thread_pool.start()
