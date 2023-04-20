from django.urls import path

from .views import model_form_upload, HomePageView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("uploads/form/", model_form_upload, name="model_form_upload"),
]
