from django.urls import path
from .endpoint import views, auth_views

urlpatterns = [
    path("", auth_views.login_google),
]
