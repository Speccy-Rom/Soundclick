from django.urls import path
from .endpoint import views, auth_views

urlpatterns = [
    path("google/", auth_views.google_auth),
    path("", auth_views.google_login),
]
