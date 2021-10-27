from django.urls import path

from .endpoint import views, auth_views

urlpatterns = [
    path('me/', views.UserView.as_view({'get': 'retrieve', 'put': 'update'})),

    path("google/", auth_views.google_auth),
    path("", auth_views.google_login),
]
