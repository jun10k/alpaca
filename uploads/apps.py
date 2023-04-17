import threading

from django.apps import AppConfig


class UploadsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'uploads'

    def ready(self):
        from .digest import DigestThreadPool
        pool = DigestThreadPool()
        pulling_thread = threading.Thread(target=pool.start)
        pulling_thread.daemon = True
        pulling_thread.start()


