from django.urls import path

from .views import simple_upload, model_form_upload, home

urlpatterns = [
    path("", home, name="home"),
    path("uploads/simple/", simple_upload, name="simple_upload"),
    path("uploads/form/", model_form_upload, name="model_form_upload"),
]
